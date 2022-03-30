import urllib3 as urllib3
from flask import Flask
import json
http = urllib3.PoolManager()
# from routes.hotel import configure_routes


app = Flask(__name__)

def test_list_hotels():

    client = app.test_client()
    print("client", client)
    url = 'http://127.0.0.1:8089/hotels'

    r = http.request('get', 'http://127.0.0.1:8089/hotels', timeout=7)

    assert r.status == 200


def test_create_hotels():
    client = app.test_client()
    print("client", client)
    example = {
        "name": "HotelBoston",
        "email": "example@gmail.com",
        "city": "Boston",
        "address": "av 45 # 24 62",
        "url_picture": "https://www.boston.com"
    }
    url = 'http://127.0.0.1:8089/create_hotel'

    r = http.request('post', url, example)
    print(r.data)

    assert r.status == 200


def test_retrieve_hotel():

    client = app.test_client()
    print("client", client)
    url = 'http://127.0.0.1:8089/hotels/6243e62d9bd099545c1531cf/'

    r = http.request('get', url, timeout=7)

    assert r.status == 200
