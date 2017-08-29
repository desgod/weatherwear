from flask import render_template
from weather_wear import openweather, outfit_picker, app



zip_code = 20002

week_forecast = openweather._get_weather_local()

forecast_info = []
for forecast in week_forecast['list']:
    wear_object = outfit_picker.WeatherWearer(forecast)
    forecast_info.append(wear_object)



@app.route('/')
def index():

    return render_template('index.html', location_name=week_forecast['city']['name'],
                           current_forecast= forecast_info[0],
                           day="Today",
                           forecast_list=forecast_info)