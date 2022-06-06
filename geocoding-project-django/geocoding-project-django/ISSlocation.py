import requests
import json

req = requests.get("http://api.open-notify.org/iss-now.json")
response = req.json()

print ('International Space Station Current Location:\n')
print(f"The timestamp of this request is: {response['timestamp']}")
print(f"The latitude of ISS is: {response['iss_position']['latitude']}")
print(f"The longitude of ISS is: {response['iss_position']['longitude']}")
print("Thanks for using this script")

PRIVATE_TOKEN="pk.bdc39850c09d1181d3996409b618be89"
URL="https://us1.locationiq.com/v1/reverse.php?key=pk.bdc39850c09d1181d3996409b618be89&lat=&lon=&format=json" 

data = {
    'key': PRIVATE_TOKEN,
    'lat': response['iss_position']['latitude'],
    'lon': response['iss_position']['longitude'],
    'format': 'json'
}
loc_response = requests.get(URL, params=data)
print(f"Over {loc_response.json()['address']['country']}")

