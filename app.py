from flask import Flask, render_template, request
import requests

app = Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static"
)


@app.route("/", methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=59e0ab2e8daad5a2ee361b329adf4b3f'
        r = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        print(weather)
        return render_template('weather.html', weather=weather)
    else:
        return render_template('weather.html')


app.run(port=5000)
