// Toggle Theme
document.getElementById('theme-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark');
});

// Sample Market Prediction Chart
const ctx = document.getElementById('predictionChart').getContext('2d');
const predictionChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
        datasets: [{
            label: 'Market Trend',
            data: [100, 110, 105, 115, 120],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});
