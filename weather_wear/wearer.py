
OUTFIT_DICT = {
    90: 'It\'s hot out today! Wear as little clothes as possible',
    80: 'It\'s pretty warm out. I would wear a t-shirt and wearable bottom.',
    70: 'Not too bad. You could pull off a t-shirt and jeans, but might want a sweater to throw on.',
    60: 'Time to start layering! It\'s definitely okay to wear boots',
    50: 'Honey, please put on your sweater! -- love Mom',
    40: 'Wear a coat today, with warm layers underneath',
    30: 'It\'s cold outside. Bundle up like a burrito',
    20: 'Put on the warmest clothes you have. ',
    10: 'Brrr! Your face will hurt. Please stay warm',
    0: 'Oh no. Just stop. Why is this happening. Stay home. Call in sick. Stay in bed!'
               }


WEAR = { 'Clear': 'Perfect day for those cool sunnies you have. Or wear a hat! Don\'t forget your sunblock!',
         'Humid': 'Sticky icky. Bad hair day ahead. All my curly heads one word: GEL! ',
         'Rain':  'Don\'t forget your umbrella!',
         'Clouds':'The sun seems to be playing a game of hide and seek today, so it might be a tad chilly.',
         'Snow': 'Snow day! Get the hot cocoa ready!',
         'Fog': 'Drive slowly!'
         }


def add_wear_information(forecast):
    """
    Populate forecast json with what to wear information
    :param forecast: Forecast json  
    """
    forecast["wear_description_temp"] = get_description_for_temp(forecast["current_temp"])
    forecast["wear_description_weather"] = WEAR.get(forecast["description"], "")


def get_description_for_temp(temperature):
    """
    Get what to wear info from current temperature
    :param temperature: current temperature
    :return: description of what to wear
    """
    # Need a way to account for high and low temps for the day
    rounded_temp = (temperature // 10) * 10
    return OUTFIT_DICT[rounded_temp]


