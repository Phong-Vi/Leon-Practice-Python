# *** Flask Server App ***
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Kansas City"
    
    weather_data = get_current_weather(city)

    # In case of City is not found by API
    if not weather_data["cod"] == 200:
        return render_template('city_not_found.html', title = city)

    if weather_data.__contains__("name"):
        return render_template(
            "weather.html",
            title = weather_data["name"],
            status = weather_data["weather"][0]["description"].capitalize(),
            temp = f"{weather_data['main']['temp']:.1f}",
            feels_like = f"{weather_data['main']['feels_like']:.1f}"
        )
    else:
        return render_template(
            "weather.html",
            title = city,
            status = weather_data["cod"],
            temp = "🤔",
            feels_like = "🤔"
        )

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000)     #initial test before waitress
    serve(app, host="0.0.0.0", port=8000)