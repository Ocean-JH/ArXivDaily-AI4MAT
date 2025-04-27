// Search functionality for a paper repository
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const papers = document.querySelectorAll('.paper');

function performSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    let resultsFound = false;

    papers.forEach(paper => {
        const title = paper.querySelector('h3').textContent.toLowerCase();
        const authors = paper.querySelector('.paper-info').textContent.toLowerCase();
        const summary = paper.querySelector('details').textContent.toLowerCase();

        if (title.includes(searchTerm) || authors.includes(searchTerm) || summary.includes(searchTerm)) {
            paper.style.display = 'block';
            resultsFound = true;
        } else {
            paper.style.display = 'none';
        }
    });

    // Display search results info
    const resultsInfo = document.getElementById('search-results-info');
    if (resultsInfo) {
        if (searchTerm === '') {
            resultsInfo.style.display = 'none';
        } else {
            resultsInfo.style.display = 'block';
            resultsInfo.textContent = resultsFound ?
                `Find papers containing "${searchTerm}"` :
                `No papers were found containing "${searchTerm}"`;
        }
    } else {
        const infoElement = document.createElement('div');
        infoElement.id = 'search-results-info';
        infoElement.className = 'search-results-info';
        if (searchTerm !== '') {
            infoElement.textContent = resultsFound ?
                `Find papers containing "${searchTerm}"` :
                `No papers were found containing "${searchTerm}"`;
        } else {
            infoElement.style.display = 'none';
        }
        document.querySelector('.search-container').after(infoElement);
    }
}

searchButton.addEventListener('click', performSearch);
searchInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        performSearch();
    }
});