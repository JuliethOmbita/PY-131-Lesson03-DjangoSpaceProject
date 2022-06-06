import requests as rqs
from dotenv import dotenv_values

ENV = dotenv_values()  
def get_coordinates(address):
    """
    Queries Location API and get's coordinates
    """

    data = {
      'key': ENV['PRIVATE_TOKEN'],
      'q': address,
      'format': 'json'
      }
    try:
       response = rqs.get(ENV['URL'], params=data)
    except Exception as e:
       raise e

    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    res = {'lat': lat, 'lon': lon, 'address': address}
    return res