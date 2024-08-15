import requests
from datetime import datetime

mylat = 51.507351
mylng = -0.127758
para = {'lat': mylat,
        'lng': mylng,
        'formatted': 0,
        }

response = requests.get('https://api.sunrise-sunset.org/json', params=para)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f'{sunrise}\n{sunset}')
