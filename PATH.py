from app import app
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from collections import namedtuple
import requests

trip_info = namedtuple("Info", "option cost duration")

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

def get_trip_estimate(slat, slong, elat, elong):

    json = get_json_data(slat, slong, elat, elong)
    low = json.get('low_estimate')
    high = json.get('high_estimate')
    avg = (low + high)/2
    time = json.get('duration') / 60
    # dist = json.get('distance')

    return trip_info('uberx', avg, time)
