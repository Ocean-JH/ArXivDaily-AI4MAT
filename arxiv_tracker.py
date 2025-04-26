import arxiv
import datetime
import os
import json
import argparse
import logging
from typing import List, Dict, Any, Optional

# Configure logging  
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("arxiv-tracker")


class ArxivTracker:
    """Periodically track new papers on arXiv"""

    def __init__(self,
                 query: str,
                 max_results: int = 30,
                 output_dir: str = "./data/results",
                 known_papers_file: str = "./data/known_papers.json",
                 templates_dir: str = "./templates"):
        """
        Initialize ArxivMonitor

        Parameters:
            query: Search query string
            max_results: Maximum number of results per search
            output_dir: Directory to save results
            known_papers_file: File to store known paper IDs
            templates_dir: Directory for HTML templates
        """
        self.query = query
        self.max_results = max_results
        self.output_dir = output_dir
        self.known_papers_file = known_papers_file
        self.templates_dir = templates_dir
        self.client = arxiv.Client()
        self.known_papers = self._load_known_papers()

        # Create directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.dirname(known_papers_file), exist_ok=True)
        os.makedirs(templates_dir, exist_ok=True)

    def _load_known_papers(self) -> set:
        """Load the set of known papers from file"""
        if os.path.exists(self.known_papers_file):
            try:
                with open(self.known_papers_file, 'r', encoding='utf-8') as f:
                    return set(json.load(f))
            except Exception as e:
                logger.error(f"Error loading known papers: {e}")
                return set()
        return set()

    def _save_known_papers(self):
        """Save the set of known papers to file"""
        try:
            with open(self.known_papers_file, 'w', encoding='utf-8') as f:
                json.dump(list(self.known_papers), f)
        except Exception as e:
            logger.error(f"Error saving known papers: {e}")

    def search_papers(self) -> List[arxiv.Result]:
        """Execute search and return results"""
        search = arxiv.Search(
            query=self.query,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        results = list(self.client.results(search))
        return results

    def paper_to_dict(self, paper: arxiv.Result) -> Dict[str, Any]:
        """Convert paper object to dictionary for saving"""
        return {
            "id": paper.entry_id,
            "title": paper.title,
            "authors": [str(author) for author in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "updated": paper.updated.isoformat(),
            "categories": paper.categories,
            "primary_category": paper.primary_category,
            "comment": paper.comment,
            "journal_ref": paper.journal_ref,
            "doi": paper.doi,
            "pdf_url": paper.pdf_url,
            "short_id": paper.get_short_id(),
            "url": paper.entry_id
        }

    def filter_new_papers(self, papers: List[arxiv.Result]) -> List[arxiv.Result]:
        """Filter out papers we've already seen"""
        new_papers = []
        for paper in papers:
            if paper.entry_id not in self.known_papers:
                new_papers.append(paper)
                self.known_papers.add(paper.entry_id)
        return new_papers

    def save_results(self, papers: List[arxiv.Result], timestamp: str) -> Optional[str]:
        """Save results to file"""
        if not papers:
            return None

        filename = f"arxiv_results_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump([self.paper_to_dict(paper) for paper in papers], f,
                      ensure_ascii=False, indent=2)

        return filepath

    def generate_markdown(self, papers: List[arxiv.Result], is_new: bool = False) -> str:
        """Generate markdown for papers"""
        if not papers:
            return f"No {'new ' if is_new else ''}papers found."

        status = "New " if is_new else ""
        md = f"## {status}Papers ({len(papers)})\n\n"
        md += f"*Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"

        for i, paper in enumerate(papers):
            md += f"### {i + 1}. {paper.title}\n\n"
            md += f"**Authors:** {', '.join(str(author) for author in paper.authors)}\n\n"
            md += f"**Published:** {paper.published.strftime('%Y-%m-%d')}\n\n"
            md += f"**Category:** {paper.primary_category}\n\n"
            md += f"**ID:** {paper.get_short_id()}\n\n"
            md += f"**Link:** [{paper.entry_id}]({paper.entry_id})\n\n"
            md += f"**Summary:** {paper.summary[:300]}...\n\n"
            md += "---\n\n"

        return md

    def update_readme(self, papers: List[arxiv.Result], readme_path: str = "README.md"):
        """Update the README.md with new papers"""
        if not papers:
            return

            # Generate markdown for new papers
        new_papers_md = self.generate_markdown(papers, is_new=True)

        # Read existing README  
        readme_content = ""
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()

                # Find the section marker or create it
        section_marker = "<!-- ARXIV_PAPERS_START -->"
        end_marker = "<!-- ARXIV_PAPERS_END -->"

        if section_marker in readme_content and end_marker in readme_content:
            # Replace the section  
            start_idx = readme_content.find(section_marker)
            end_idx = readme_content.find(end_marker) + len(end_marker)
            readme_content = (
                    readme_content[:start_idx] +
                    section_marker + "\n\n" +
                    new_papers_md +
                    "\n" + end_marker +
                    readme_content[end_idx:]
            )
        else:
            # Add the section at the end  
            if readme_content:
                readme_content += "\n\n"
            readme_content += f"{section_marker}\n\n{new_papers_md}\n{end_marker}"

            # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        logger.info(f"Updated README with {len(papers)} new papers")

    def generate_html(self, papers: List[arxiv.Result], is_new: bool = False) -> str:
        """Generate HTML for papers"""
        if not papers:
            return f"<p>No {'new ' if is_new else ''}papers found.</p>"

        with open("templates/paper_item.html", 'r', encoding='utf-8') as f:
            paper_template = f.read()

        status = "New " if is_new else ""
        html = f"<h2>{status}Papers ({len(papers)})</h2>\n"
        html += f"<p><em>Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>\n"

        for i, paper in enumerate(papers):
            paper_html = paper_template.format(
                index=i + 1,
                title=paper.title,
                authors=", ".join(str(author) for author in paper.authors),
                published_date=paper.published.strftime("%Y-%m-%d"),
                category=paper.primary_category,
                paper_id=paper.get_short_id(),
                url=paper.entry_id,
                summary=paper.summary[:300]
            )
            html += paper_html

        return html

    def create_index_html(self, papers: List[arxiv.Result], output_path: str = "index.html"):
        """Create an index.html file with all papers"""
        with open("templates/index.html", 'r', encoding='utf-8') as f:
            html_template = f.read()

        # Generate HTML content for papers
        content = self.generate_html(papers, is_new=True)

        # Fill in the template
        html_content = html_template.format(
            query=self.query,
            content=content,
            timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f"Created index.html with {len(papers)} papers")

    def create_archive_html(self, output_path: str = "archive.html"):
        """Create an archive.html file with all known papers"""
        # Load all saved results
        all_papers = []
        results_files = [f for f in os.listdir(self.output_dir) if f.endswith('.json')]

        for file in results_files:
            try:
                with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
                    papers_data = json.load(f)
                    all_papers.extend(papers_data)
            except Exception as e:
                logger.error(f"Error loading results file {file}: {e}")

                # Sort papers by published date (newest first)
        all_papers.sort(key=lambda p: p['published'], reverse=True)

        with open("templates/paper_item.html", 'r', encoding='utf-8') as f:
            paper_template = f.read()

            # Generate HTML content
        content = "<h2>All Papers</h2>\n"
        content += f"<p><em>Total: {len(all_papers)} papers</em></p>\n"

        for i, paper in enumerate(all_papers):
            paper_html = paper_template.format(
                index=i + 1,
                title=paper["title"],
                authors=", ".join(paper["authors"]),
                published_date=paper["published"][:10],
                category=paper["primary_category"],
                paper_id=paper["short_id"],
                url=paper["url"],
                summary=paper["summary"][:300]
            )
            content += paper_html

            # Fill in the template (reuse the same template as index.html)
        with open("templates/archive.html", 'r', encoding='utf-8') as f:
            html_template = f.read()

        html_content = html_template.format(
            query=self.query,
            content=content,
            timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f"Created archive.html with {len(all_papers)} papers")

    def run(self, update_readme: bool = True, create_html: bool = True):
        """Run the tracker once"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        logger.info(f"Searching for: {self.query}")

        try:
            # Get papers
            papers = self.search_papers()
            logger.info(f"Found {len(papers)} papers in total")

            # Filter new papers
            new_papers = self.filter_new_papers(papers)
            logger.info(f"Found {len(new_papers)} new papers")

            if new_papers:
                # Save results
                filepath = self.save_results(new_papers, timestamp)
                if filepath:
                    logger.info(f"Results saved to: {filepath}")

                    # Update README if requested
                if update_readme:
                    self.update_readme(new_papers)

                    # Create HTML if requested
                if create_html:
                    self.create_index_html(new_papers)

                    # Create Archive Page
                if create_html:
                    self.create_index_html(new_papers)
                    self.create_archive_html()

                    # Save known papers
            self._save_known_papers()

            return new_papers

        except Exception as e:
            logger.error(f"Error during search: {e}", exc_info=True)
            return []


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="arXiv Paper Tracker")
    parser.add_argument("--config", type=str, default="config.json", help="Path to config file")
    parser.add_argument("--query", type=str, help="Search query (overrides config)")
    parser.add_argument("--max-results", type=int, help="Maximum results (overrides config)")
    parser.add_argument("--no-readme", action="store_true", help="Don't update README")
    args = parser.parse_args()

    # Load config  
    config = {
        "query": "cat:cond-mat.mtrl-sci AND (cat:cs.AI OR cat:cs.LG) AND all:\"crystal structure\" ANDNOT ti:\"organic\" AND (all:\"machine learning\" OR all:\"materials design\" OR all:\"generative\")",
        "max_results": 30,
        "output_dir": "./data/results",
        "known_papers_file": "./data/known_papers.json"
    }

    if os.path.exists(args.config):
        try:
            with open(args.config, 'r', encoding='utf-8') as f:
                config.update(json.load(f))
        except Exception as e:
            logger.error(f"Error loading config: {e}")

            # Override with command line arguments
    if args.query:
        config["query"] = args.query
    if args.max_results:
        config["max_results"] = args.max_results

        # Create and run Tracker
    tracker = ArxivTracker(
        query=config["query"],
        max_results=config["max_results"],
        output_dir=config["output_dir"],
        known_papers_file=config["known_papers_file"]
    )

    tracker.run(update_readme=not args.no_readme)


if __name__ == "__main__":
    main()
