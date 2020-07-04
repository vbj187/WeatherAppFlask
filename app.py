from flask import Flask, render_template
import requests

app = Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static"
)


@app.route('/')
def hello_world():
    return 'Hello World'


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' +\
        city+'&units=metric&appid=59e0ab2e8daad5a2ee361b329adf4b3f'
    json_response = requests.get(url).json()
    weather_description = json_response["weather"][0]["description"]
    temp = json_response["main"]["temp"]
    return {"description": weather_description, "temp": temp}


@app.route("/<location>")
def weather(location):
    weather_details = get_weather(location)
    return weather_details


app.run(port=5000)
