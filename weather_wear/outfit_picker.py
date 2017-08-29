import datetime


OUTFIT_DICT = {
    90: 'It\'s hot out today! Wear as little clothes as possible',
    80: 'It\'s pretty warm out. I would wear shorts and a tank.',
    70: 'Not too bad. How about a t-shirt and jeans.',
    60: 'Time to start layering! It\'s definitely okay to wear boots',
    50: 'Honey, please put on your sweater! -- love Mom',
    40: 'Wear a coat today, with warm layers underneath',
    30: 'It\'s cold outside. Bundle up like a burrito',
    20: 'Put on the warmest clothes you have. ',
    10: 'Brrr! Your face will hurt. Please stay warm',
    0: 'Oh no. Just stop. Why is this happening. Stay home. Call in sick. Stay in bed!'
               }


SUNBLOCK = 'Don\'t forget your sunblock!'
SUNNY = 'Perfect day for those cool sunnies you have. Or wear a hat!'
HUMID = 'Sticky icky. Bad hair day ahead. All my curly heads one word: GEL! '
RAINY = 'Don\'t forget your umbrella!'
CLOUDY = 'The sun seems to be playing a game of hide and seek today, so it might be a tad chilly.'
SNOW = 'Snow day! Get the hot cocoa ready!'


WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class WeatherWearer(object):

    def __init__(self, weather_json):
        self.current_temperature = round(weather_json['temp']['day'])
        self.min_temperature = round(weather_json['temp']['min'])
        self.max_temperature = round(weather_json['temp']['max'])
        self.humidity = round(weather_json['humidity'])
        self.wear = []
        self.description = weather_json['weather'][0]['main']
        self._epochdate = weather_json['dt']
        self.day = self.get_date_information()

        self.get_description_for_temp()
        self.get_description_for_weather()


    def get_description_for_temp(self):
        # Need a way to account for high and low temps for the day
        rounded_temp = (self.current_temperature // 10) * 10
        description = OUTFIT_DICT[rounded_temp]
        self.wear.append(description)

    def get_description_for_weather(self):
        if self.description == 'Clouds':
            self.wear.append(CLOUDY)
        elif self.description == 'Clear':
            self.wear.append(SUNNY)
            self.wear.append(SUNBLOCK)
        elif self.description == 'Rain':
            self.wear.append(RAINY)
        elif self.description == 'Snow':
            self.wear.append(SNOW)

    def get_date_information(self):
        date = datetime.datetime.fromtimestamp(self._epochdate)
        return WEEK_DAYS[date.weekday()]


    def __repr__(self):
        import json
        return  json.dumps({
            'current_temperature': self.current_temperature,
            'min_temperature': self.min_temperature,
            'max_temperature': self.max_temperature,
            'humidity': self.humidity,
            'wear': self.wear,
            'description': self.description
                })


