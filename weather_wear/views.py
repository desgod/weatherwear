from flask import render_template
from weather_wear import openweather, wearer, app


zip_code = 20002

week_forecast = openweather._get_weather_local()

forecast_info = []
for forecast in week_forecast['list']:
    wear_object = wearer.WeatherWearer(forecast)
    forecast_info.append(wear_object)


@app.route('/')
def index():

    return render_template('index.html', location_name=week_forecast['city']['name'],
                           current_forecast=forecast_info[0],
                           day="Today",
                           forecast_list=forecast_info)


@app.route('/_get_forecast/<zipcode>', methods=['POST'])
def _get_forecast(zipcode):
    forecast_data = openweather.get_weather_forecast(zipcode)
    location_name = forecast_data['city']['name']

    weather_wearers = _get_populated_list(forecast_data)
    current_forecast = weather_wearers[0]

    return "hello, success" # weather_wearers


def _get_populated_list(forecast_data):
    weather_wearers = []
    for forecast_json in forecast_data['list']:
        populated_ww = wearer.WeatherWearer(forecast_json)
        weather_wearers.append(populated_ww)

    return weather_wearers




