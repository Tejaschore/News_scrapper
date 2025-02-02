document.addEventListener('DOMContentLoaded', function() {
    // Select all the news items
    const newsItems = document.querySelectorAll('.news-item');

    // Iterate through each news item
    newsItems.forEach(item => {
        // Add a click event listener to each news item
        item.addEventListener('click', function() {
            // Find the content element within the clicked item
            const content = item.querySelector('.news-content');
            
            // Toggle visibility of the content
            if (content) {
                if (content.style.display === 'block') {
                    content.style.display = 'none'; // Hide it if it is already visible
                } else {
                    content.style.display = 'block'; // Show it if it is hidden
                }
            }
        });
    });
});
