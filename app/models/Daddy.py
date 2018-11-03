import UberEstimate
import CarEstimate
import TransitEstimate
from PathObject import PathObject

class Daddy:

    def __init__(self):
        #UBER
        self.tripInfo = UberEstimate.get_uberx_estimate(33.9416, -118.4085, 34.0977, -117.7118)
        self.pathObj = PathObject(self.tripInfo[0],
                        self.tripInfo[1], self.tripInfo[2])
        self.pathObjLst = []
        self.pathObjLst[0] = self.pathObj

        #CAR
        # self.tripInfo2 = CarEstimate.get_car_tuple(None, None, None, None)
        # self.pathObj2 = PathObject(self.tripInfo2[0], self.tripInfo2[1], 
                       # self.tripInfo2[2])
        # self.pathObjList[1] = self.pathObj2

        #PUBLIC_TRANSIT
        self.tripInfo3 = TransitEstimate.get_transit_estimate(33.9416, -118.4085, 34.0977, -117.7118)
        self.pathObj3 = PathObject(self.tripInfo3[0], self.tripInfo3[1], 
                        self.tripInfo3[2])

        #WALKING
       



        self.cheap3 = []
        self.fast3 = []
        self.finalSix = []

        self.sortTime()
        self.sortPrice()

    def sortTime():

        timeLst = [None] * len(self.pathObjLst)

        for i in range(len(self.pathObjLst)):
            timeLst[i] = self.pathObjLst[i].get_time()
        
        self.sorter = Sorter(timeLst)
        
        self.fast3 = make_sorter()

    def sortPrice():

        priceLst = [None] * len(self.pathObjLst)

        for i in range(len(self.pathObjLst)):
            timeLst[i] = self.pathObjLst[i].get_price()
        
        self.sorter = Sorter(priceLst)

        self.cheap3 = make_sorter()

    def createFinalSix():
        index = 0
        for i in range(0, 5):
            finalSix.append(cheap3[index])
            finalSix.append(cheap3[index])
            index += 1
        return finalSix

test = Daddy()
print (test.createFinalSix())