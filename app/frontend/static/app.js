function predictLength() {
    var word = document.getElementById('word').value;

    // Send a POST request to the API endpoint
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'word': word })
    })
    .then(response => response.json())
    .then(result => {
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = 'Length: ' + result.length;
    })
    .catch(error => console.error('Error:', error));
}