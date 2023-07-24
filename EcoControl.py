from flask import Flask, jsonify, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Sonoran%20Desert/"

def fetch_weather_data():
    last_year_date = datetime.now() - timedelta(days=365)
    url = f"{BASE_URL}{last_year_date.strftime('%Y-%m-%d')}/{last_year_date.strftime('%Y-%m-%d')}?unitGroup=metric&key={API_KEY}&contentType=json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract weather data from JSON and do something with it
        day_data = data.get('days', [{}])[0]
        if 'hours' in day_data:
            hour_data = next((hour for hour in day_data['hours'] if hour['datetime'] == last_year_date.strftime('%H:00:00')), {})
            temperature = hour_data.get('temp')
            feelslike = hour_data.get('feelslike')
            humidity = hour_data.get('humidity')
            sunrise = day_data.get('sunrise')
            sunset = day_data.get('sunset')
            meridian = (datetime.strptime(sunrise, '%H:%M:%S') + (datetime.strptime(sunset, '%H:%M:%S') - datetime.strptime(sunrise, '%H:%M:%S')) / 2).strftime('%H:%M:%S')
            # Continue extracting other weather data as needed

            # Return the weather information as a dictionary
            return {
                "date": last_year_date.strftime('%Y-%m-%d %H:%M:%S'),
                "temperature": temperature,
                "feelslike": feelslike,
                "humidity": humidity,
                "sunrise": sunrise,
                "sunset": sunset,
                "meridian": meridian,
                # Continue returning other weather data as needed
            }

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/weather')
def get_weather_data():
    weather_data = fetch_weather_data()
    return jsonify(weather_data)

@app.route('/')
def dashboard():
    weather_data = fetch_weather_data()
    return render_template('dashboard.php', data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
