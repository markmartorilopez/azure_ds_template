function predictMetrics() {
    var name = document.getElementById('name').value;

    // Send a POST request to the /metrics endpoint
    fetch('/metrics', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'name': name })
    })
    .then(response => response.json())
    .then(metrics => {
        var metricsDiv = document.getElementById('metrics');
        metricsDiv.innerHTML = '';

        // Display each metric in the metrics dictionary
        for (var key in metrics) {
            var metricValue = metrics[key];
            var metricElement = document.createElement('p');
            metricElement.innerHTML = key + ': ' + metricValue;
            metricsDiv.appendChild(metricElement);
        }
    })
    .catch(error => console.error('Error:', error));
}