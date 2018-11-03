import Tuple

def get_car_cost_estimate(distance, mpg, gas_price):
    return distance / mpg * gas_price

def get_car_tuple(distance, time, mpg, gas_price):
    return trip_info('car', get_car_cost_estimate(distance, mpg, gas_price), time)
