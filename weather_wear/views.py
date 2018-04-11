from flask import jsonify

from weather_wear import wearer, app
from weather_wear.openweather import Weather


@app.route('/<zipcode>/todays_forecast')
def get_todays_forecast(zipcode):
    """
    Get Todays forecast
    :param zipcode: zipcode of area you would like the forecast for
    :return: todays forecast for zip
    
    GET /20002/todays_forecast
    """
    weather = Weather(zipcode)
    return jsonify(weather.todays_forecast)


@app.route('/<zipcode>/forecast')
def get_forecast(zipcode):
    """
    Get Weekly forecast
    :param zipcode: zipcode of area you would like the weekly forecast for
    :return: weekly forecast
    
    GET /20002/forecast
    """
    weather = Weather(zipcode)
    return jsonify(weather.forecast)


@app.route('/<zipcode>/wear_forecast')
def get_wear(zipcode):
    """
    Get Wear Forecast
    :param zipcode: zipcode of area you would like to know what to wear for the week
    :return: weekly forecast with descriptions on what to wear for that day
    
    GET /20002/wear_forecast
    """
    weather_forecast = Weather(zipcode).forecast
    for forecast in weather_forecast["forecast"]:
        wearer.add_wear_information(forecast)

    return jsonify(weather_forecast)


@app.route('/<zipcode>/wear_today')
def get_wear_today(zipcode):
    """
    Get Wear Today
    :param zipcode: zipcode of area you would like to know what to wear today
    :return: todays forecast with description on what you should wear today
    
    GET /20002/wear_today
    """
    weather_forecast = Weather(zipcode).todays_forecast
    wearer.add_wear_information(weather_forecast)

    return jsonify(weather_forecast)




