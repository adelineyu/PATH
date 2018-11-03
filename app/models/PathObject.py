class PathObject:
    method = ""
    time = 0
    price = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, method, time, price):
        self.method = method
        self.time = time
        self.price = price

def make_path(method, time, price):
    path = PathObject(method, time, price)
    return path

def get_time():
    return self.time

def get_price(): 
    return self.price

test = PathObject("Bike", 3, 4.3)
test.method = "Walk"

print(test.method)