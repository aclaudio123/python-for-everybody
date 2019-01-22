#
# Title:   geolocation finder using JSON API
# Author: Claudio Asangong
#
# In this assignment you will write a Python program that prompts for a
# location, contact a web service and retrieve JSON for the web service and
# parse that data, and retrieve the first place_id from the JSON. A place ID
# is a textual identifier that uniquely identifies a place as within Google
# Maps.
#
# API End Points
# To complete this assignment, you should use this API endpoint that has a
# static subset of the Google Data: http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also
# has no rate limit so you can test as often as you like. If you visit the URL
# with no parameters, you get "No address..." response.
# To call the API, you need to provide address that you are requesting as
# the address= parameter that is properly URL encoded using the
# urllib.urlencode() fuction.
#
# Concepts: geocoding, JSON, urllib
# commit msg: geolocation place_id finder

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    if api_key is not False:
        params['key'] = api_key
    # parse the dict() items into a nice format and add to end of serviceurl
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    # read and decode UTF-8 bytes into Python unicode strings
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except Exception:
        js = None
        continue

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4)) -- print json data for debugging
    place_id = js['results'][0]['place_id']
    print('place_id', place_id)
