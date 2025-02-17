function updatePrediction() {
  fetch('/api/prediction')
    .then(response => response.json())
    .then(data => {
      document.getElementById('trend').innerText = data.trend;
      document.getElementById('confidence').innerText = data.confidence;
      document.getElementById('time').innerText = data.time;
    })
    .catch(error => console.error('Error fetching prediction:', error));
}
updatePrediction();
setInterval(updatePrediction, 5000);
