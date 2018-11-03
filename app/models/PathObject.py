class PathObject:
    method = ""
    time = 0
    price = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, method, price, time):
        self.method = method
        self.price = price
        self.time = time

    def make_path(self, method, price, time):
        path = PathObject(method, price, time)
        return path

    def get_time(self):
        return self.time

    def get_price(self): 
        return self.price
