import requests
import datetime

########################################
APP_ID = '309a71cbbf880f70a5d7f9673a43b3fa'
OPEN_API_URL_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast/daily'
OPEN_API_URL_TODAY = 'http://api.openweathermap.org/data/2.5/weather?'
LANG = 'en-US'
UNITS = 'imperial'  # make configurable
COUNT = 7  # number of forecast to return

PARAMS = {'appid': APP_ID,
          'lang': LANG,
          'units': UNITS,
          'cnt': COUNT
          }

WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class Weather(object):
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.actual = {}
        self.weather_data = self._get_openweather_response()

        self.forecast = self.get_weather_forecast()
        self.todays_forecast = self.get_todays_forecast()

    def _get_openweather_response(self):
        """
        Get forecast data from openweather
        :return: openweather json response
        """
        PARAMS['zip'] = self.zip_code
        response = requests.get(OPEN_API_URL_FORECAST, params=PARAMS)
        return response.json()

    def get_weather_forecast(self):
        """
        Get weather forecast data 
        :return: return forecast data
        """

        location = self.weather_data["city"]["name"]
        forecast_list = self.weather_data["list"]
        formatted_list = self._format_forecast_data(forecast_list)
        return {"location": location, "forecast": formatted_list}

    def get_todays_forecast(self):
        """
        Get's todays forecast from openweather api 
        :return: todays forecast
        """
        PARAMS["zip"] = self.zip_code
        todays_data = requests.get(OPEN_API_URL_TODAY, params=PARAMS).json()
        return self._format_todays_data(todays_data)

    def _format_todays_data(self, todays_forecast):
        """
        Formats todays weather data
        :param todays_forecast: todays forecast data
        :return: formatted data
        """
        return {"location": todays_forecast["name"],
                "day": self._format_date(todays_forecast["dt"]),
                "current_temp": todays_forecast["main"]["temp"],
                "min": todays_forecast["main"]["temp_min"],
                "max": todays_forecast["main"]["temp_max"],
                "description": todays_forecast["weather"][0]["main"]}

    def _format_forecast_data(self, forecast_list):
        """
        Formats weekly forecast data
        :param forecast_list: list of forecast for the week 
        :return: formatted forecast data
        """
        structured_list = []
        for forecast in forecast_list:
            date = self._format_date(forecast["dt"])
            structured_list.append({"day": date,
                                    "current_temp": forecast["temp"]["day"],
                                    "min": forecast["temp"]["min"],
                                    "max": forecast["temp"]["max"],
                                    "description": forecast["weather"][0]["main"]
                                    })
        return structured_list

    def _format_date(self, epoch_date):
        """
        Converts epoch data to day of week
        :param epoch_date: 
        :return: day of week
        """
        date = datetime.datetime.fromtimestamp(epoch_date).weekday()
        return WEEK_DAYS[date]




