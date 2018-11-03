class Sorter: 

    def __init__(self, pathList):
        self.pathList = pathList
        self.cheapest = [None] * 3
    
    def make_priceSorter(self):
        sortedList = sorted(self.pathList)

        for i in range(0, 3):
            self.cheapest[i] = sortedList[i]

        return self.cheapest


test = Sorter([92, 4, 2, 1, 5, 3, 0])
print(test.make_priceSorter())