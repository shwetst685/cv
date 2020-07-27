import urllib.request,urllib.parse,urllib.error
import ssl
import json

key = 'AIzaSy___IDByT70'

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

service_url = 'http://py4e-data.dr-chuck.net/json?'


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode =ssl.CERT_NONE

while True:
    address=input('enter the location')
    if len(address)<1:
        print('invalid address')
        break
    parms=dict()
    parms['address']=address
    parms['key']=key
    url=service_url+urllib.parse.urlencode(parms)

    connection=urllib.request.urlopen(url,context=ctx)
    data=connection.read().decode()
    print(data)
    print('retrieved',len(data),'character')
    js = json.loads(data)
    print(json.dumps(js,indent=2))
