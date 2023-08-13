from Components import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from Util import nullCheck

class Vehicle:
    def __init__(self, 
                 vehicleType: str,
                  make: str,
                  model: str, 
                  year: int, 
                  reg: str, 
                  cylinders: int, 
                  **kwargs):
        self.type = vehicleType
        self.make = make
        self.model = model
        self.year = year
        self.reg = reg

        self.engine = Engine(cylinders)
        self.oil = Oil()
        self.battery = GenericComponent("Battery")

        if "wheelNumber" in kwargs and kwargs["wheelNumber"] != 0:
            self.brakes = Brakes(kwargs["wheelNumber"])
            self.tyres = Tyres(kwargs("wheelNumber"))
        elif self.type == "Car":
            self.brakes = Brakes(4)
            self.tyres = Tyres(4)
        elif self.type == "Motorcycle":
            self.brakes = Brakes(2)
            self.tyres = Tyres(2)

        if self.type == "Motorcycle":
            self.chain = Chain()
        
        self.setMotInterval(years=1)

        self.mileage = None
        self.lastMot = None

    def setMileage(self, mileage):
        self.mileage = mileage
    def getMileage(self):
        return nullCheck(self.mileage)
    
    def getLastMot(self):
        return nullCheck(self.lastMot)

    def setLastMot(self, year:int, month: int, day: int):
        self.lastMot = date(year,month,day)

    def setMotInterval(self, years=0, months=0, days=0):
       self.motInterval = relativedelta(years=years,months=months,days=days)

    def getNextMot(self):
        return self.lastMot + self.motInterval
    
    def printAllVehicleData(self):
        outString = f'''
        Type: {self.type}
        Make: {self.make}
        Model: {self.model}
        Year: {self.year}
        Registration: {self.reg}
        Mileage: {self.getMileage()}
        Last MOT: {self.getLastMot()}
        Next MOT: {self.getNextMot()}
        '''
        print(outString)