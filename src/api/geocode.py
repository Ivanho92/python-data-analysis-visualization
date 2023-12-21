import json
import urllib.parse
import urllib.request

import config


def get_coordinates(endpoint, api_key, location):
    if config.MOCK_API_RESPONSE:
        response = '{"results": [{"address_components": [{"long_name": "Brussels", "short_name": "Brussels", "types": ["locality", "political"]}, {"long_name": "Brussels", "short_name": "Brussels", "types": ["administrative_area_level_1", "political"]}, {"long_name": "Belgium", "short_name": "BE", "types": ["country", "political"]}], "formatted_address": "Brussels, Belgium", "geometry": {"bounds": {"northeast": {"lat": 50.9139024, "lng": 4.437065899999999}, "southwest": {"lat": 50.7963456, "lng": 4.3137683}}, "location": {"lat": 50.8476424, "lng": 4.3571696}, "location_type": "APPROXIMATE", "viewport": {"northeast": {"lat": 50.9139024, "lng": 4.437065899999999}, "southwest": {"lat": 50.7963456, "lng": 4.3137683}}}, "place_id": "ChIJZ2jHc-2kw0cRpwJzeGY6i8E", "types": ["locality", "political"]}], "status": "OK"}'
    else:
        query = endpoint + '?key=' + api_key + '&address=' + urllib.parse.quote(location)
        response = urllib.request.urlopen(query).read()

    json_parsed = json.loads(response)

    coordinates = json_parsed['results'][0]['geometry']['location']

    return coordinates
