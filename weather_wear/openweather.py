import requests

APP_ID = '309a71cbbf880f70a5d7f9673a43b3fa'
# REST_CALL = 'http://http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID={}&lang=en-US'
OPEN_API_URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'
LANG = 'en-US'
UNITS = 'imperial'  # make configurable
COUNT = 7

PARAMS = {'appid': APP_ID,
          'lang': LANG,
          'units': UNITS,
          'cnt': COUNT
          }


def get_weather_forecast(zip_code):
    PARAMS['zip'] = zip_code
    response = requests.get(OPEN_API_URL, params=PARAMS)
    response_json = response.json()
    return response_json



def _get_weather_local():
    import json
    import os
    with open(os.path.join(os.path.dirname(__file__),'test_dc.json') )as json_data:
        return json.load(json_data)


# print(get_weather_forecast(20002))