from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

from keys import FOURSQUARE_CLIENT_ID, FOURSQUARE_CLIENT_SECRET
foursquare_id = FOURSQUARE_CLIENT_ID
foursquare_secret = FOURSQUARE_CLIENT_SECRET


def findARestaurant(mealType,location):
    #1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    lat, lng = getGeocodeLocation(location)

    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20171026&ll=%s,%s&query=%s' % (
            foursquare_id, foursquare_secret, lat, lng, mealType))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    #3. Grab the first restaurant
    venue = result['response']['venues'][0]
    venue_id = venue['id']
    venue_name = venue['name']
    venue_address = venue['location']['formattedAddress']

    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    picUrl = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20171026' % (
               venue_id, foursquare_id, foursquare_secret))
    picResponse, picContent = h.request(picUrl, 'GET')
    picResult = json.loads(picContent)

    #5. Grab the first image
    if picResult['response']['photos']['items']:
        firstPic = picResult['response']['photos']['items'][0]
        venue_image = firstPic['prefix'] + '300x300' + firstPic['suffix']

    #6. If no image is available, insert default a image url
    else:
        venue_image = "http://placekitten.com/300/300"

    #7. Return a dictionary containing the restaurant name, address, and image url
    venue_info = {
        'name': venue_name,
        'address': venue_address,
        'image': venue_image
    }
    # print "Name: %s" % venue_info['name']
    # print "Address: %s" % venue_info['address']
    # print "Image: %s\n" % venue_info['image']
    return venue_info

if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")
