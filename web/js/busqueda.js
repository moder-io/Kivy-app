const inputSearch = document.getElementById('searchInput');
const searchLink = document.getElementById('searchLink');

inputSearch.addEventListener('keyup', (e) => {
    if (e.key === 'Enter') {
        searchLink.href = `https://www.google.com/search?q=${inputSearch.value}`;
        searchLink.click();
    }
});