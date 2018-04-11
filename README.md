# telling you what to wear 

## To run:
__* Use python3__
* `$ pip install -r requirements.txt`
* `$ python3 runserver.py`

## API:
* `GET` <zipcode>/todays_forecast --> returns Todays forecast for given zip
* `GET` <zipcode>/forecast        --> returns Weekly forecast for given zip
* `GET` <zipcode>/wear_forecast   --> returns Weekly forecast with a description on what to wear for each day for given zip
* `GET` <zipcode>/wear_today      --> returns Todays forecast with a description on what to wear for the given zip