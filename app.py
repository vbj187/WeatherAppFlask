from flask import Flask, render_template
import requests

app = Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static"
)


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' +\
        city+'&units=metric&appid=59e0ab2e8daad5a2ee361b329adf4b3f'
    json_response = requests.get(url).json()
    weather_description = json_response["weather"][0]["description"]
    temp = json_response["main"]["temp"]
    return {"description": weather_description, "temp": temp}


@app.route("/")
def weather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=59e0ab2e8daad5a2ee361b329adf4b3f'
    city = 'Tiruchirappalli'

    r = requests.get(url.format(city)).json()
    # print(r)

    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(weather)

    return render_template("weather.html", weather=weather)


app.run(port=5000)
