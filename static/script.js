// Toggle between stock symbol and file input
document.getElementById('stock_option').addEventListener('change', function() {
    document.getElementById('stock-input').style.display = 'block';
    document.getElementById('file-input').style.display = 'none';
});

document.getElementById('file_option').addEventListener('change', function() {
    document.getElementById('stock-input').style.display = 'none';
    document.getElementById('file-input').style.display = 'block';
});

// Handle form submission
document.getElementById('input-form').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    // Make the POST request to upload
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    
    // Parse the JSON response
    const data = await response.json();

    // Display classification result
    const resultDiv = document.getElementById('result');
    resultDiv.innerText = `Classification: ${data.classification_label}`;

    // Display key stats if available
    const statsDiv = document.getElementById('key-stats');
    if (data.key_stats) {
        let statsHtml = '<h3>Key Stats:</h3><ul>';
        for (let [key, value] of Object.entries(data.key_stats)) {
            statsHtml += `<li>${key}: ${value}</li>`;
        }
        statsHtml += '</ul>';
        statsDiv.innerHTML = statsHtml;
    } else {
        statsDiv.innerHTML = '';
    }
};
