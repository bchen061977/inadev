import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_temperature_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=38.9488&longitude=-77.4491&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['hourly']['temperature_2m'][0]

@app.route('/')
def index():
    temperature = get_temperature_data()
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

