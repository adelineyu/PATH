from app import app

# before running this file, run
#   pip install uber-rides
# in command line
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token='ZaorUL2L_CCILlRtjHBrLz93-hTPIIBJHExq4C5m')
client = UberRidesClient(session)

def price_estimate(slat, slong, elat, elong, seats):
    response = client.get_price_estimates(
        start_latitude=slat,
        start_longitude=-slong,
        end_latitude=elat,
        end_longitude=-elong,
        seat_count=seats
    )
