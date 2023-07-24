<!DOCTYPE html>
<html>
<head>
    <title>Weather Dashboard</title>
</head>
<body>
    <h1>Weather Dashboard</h1>
    {% if data %}
    <p>Date: <span id="date">{{ data.date }}</span></p>
    <p>Current Temperature: <span id="temperature">{{ data.temperature }}°C</span></p>
    <p>Feels Like: <span id="feelslike">{{ data.feelslike }}°C</span></p>
    <p>Humidity: <span id="humidity">{{ data.humidity }}%</span></p>
    <p>Sunrise: <span id="sunrise">{{ data.sunrise }}</span></p>
    <p>Sunset: <span id="sunset">{{ data.sunset }}</span></p>
    <p>Meridian: <span id="meridian">{{ data.meridian }}</span></p>
    <!-- Add more elements to display other weather data as needed -->
    {% else %}
    <p>Error fetching weather data.</p>
    {% endif %}
    
    <script>
        function fetchData() {
            fetch('/weather')
            .then(response => response.json())
            .then(data => {
                document.getElementById('date').innerText = data.date;
                document.getElementById('temperature').innerText = data.temperature + "°C";
                document.getElementById('feelslike').innerText = data.feelslike + "°C";
                document.getElementById('humidity').innerText = data.humidity + "%";
                document.getElementById('sunrise').innerText = "Sunrise: " + data.sunrise;
                document.getElementById('sunset').innerText = "Sunset: " + data.sunset;
                document.getElementById('meridian').innerText = "Meridian: " + data.meridian;
                // Update other elements as needed
            })
            .catch(error => {
                console.error("Error fetching weather data:", error);
            });
        }

        fetchData(); // Fetch data once on page load

        // Update data every 60 seconds
        setInterval(fetchData, 60000);
    </script>
</body>
</html>
