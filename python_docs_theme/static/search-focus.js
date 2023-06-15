document.addEventListener('keydown', function(event) {
  if (event.key === '/') {
     // Prevent "/" from being entered in the search box
    event.preventDefault();

    // Set the focus on the search box
    let searchBox = document.getElementById('search-box');
    searchBox.focus();
  }
});
