import httplib2
import json

from keys import GOOGLE_API_KEY

def getGeocodeLocation(inputString):
    key = GOOGLE_API_KEY
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (
            locationString, key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    # print "response header: %s \n \n" % response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
