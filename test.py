

import openrouteservice
from openrouteservice import convert
import shapely
import geojson
import os
import json
'''
install ors library:
https://openrouteservice-py.readthedocs.io/en/latest/

get your api key:
https://openrouteservice.org/dev/#/home

paste it into key.txt (keep your key to yourself!)
'''
print(os.getcwd())

routes = []

start = (8.34234,48.23424)
end = (8.34423,48.26424)
coords = (start, end)
keyfile = open('key.txt', 'r')
key = keyfile.read()
client = openrouteservice.Client(key=key) # Specify your personal API key
# decode_polyline needs the geometry only

profile = 'cycling-regular'
extra_info = ['steepness', 'suitability', 'surface', 'waycategory', 'waytype']
response = client.directions(coords, profile = 'cycling-regular', extra_info = extra_info)
print(response)
geometry = response['routes'][0]['geometry']
routes.append(geometry)

with open('response.json', 'w') as outfile:
    json.dump(response, outfile)


decoded = convert.decode_polyline(geometry)
with open('route.geojson', 'w') as outfile:
    json.dump(decoded, outfile)
#print(decoded)
