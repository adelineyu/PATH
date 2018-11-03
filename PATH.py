from app import app
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import requests

session = Session(server_token='ZaorUL2L_CCILlRtjHBrLz93-hTPIIBJHExq4C5m')
client = UberRidesClient(session)

def get_json_data(slat, slong, elat, elong):

    headers = {'Authorization': 'Token ZaorUL2L_CCILlRtjHBrLz93-hTPIIBJHExq4C5m',
    'Accept-Language': 'en_US',
    'Content-Type': 'application/json'
    }

    resp = requests.get(
    'https://api.uber.com/v1.2/estimates/price?start_latitude=' + str(slat)
    + '&start_longitude=' + str(slong)
    + '&end_latitude=' + str(elat)
    + '&end_longitude=' + str(elong),
    headers=headers
    )

    # returns price data for UberX
    return resp.json().get('prices')[7]

print("hello")
print(get_json_data(37.770,-122.411,37.791,-122.405))
