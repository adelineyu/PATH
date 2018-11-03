from PathObject import PathObject

class Sorter: 

    # pathList: list of PathObjects
    # best:     3 best travel options
    def __init__(self, pathList):
        self.pathList = pathList
        self.best = [None] * 3
    
    # def get_value(sortByTime):
    #     if sortByTime:
    #         return self.pathList

    def make_sorter(self, sortByTime):
        
        new_list = []
        for x in self.pathList:
            new_list.append(x[0])

        if sortByTime:
            new_list.sort(key=lambda x: x.get_time())
        else:
            new_list.sort(key=lambda x: x.get_price())

        for i in range(0, 3):
            self.best[i] = new_list[i]

        import pdb; pdb.set_trace()
        return self.best


a = PathObject("Bike", 1, 23),
b = PathObject("Walk", 54, 53),
c = PathObject("Car", 3, 1),
d = PathObject("Horse", 2958, 65),

test = Sorter([a, b, c, d])
print(test.make_sorter(True))