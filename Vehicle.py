from Components import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from Util import nullCheck, BColours

class Vehicle:
    def __init__(self, 
                 vehicleType: str,
                  make: str,
                  model: str, 
                  dateReg: date, 
                  reg: str, 
                  cylinders: int, 
                  **kwargs):
        self.type = vehicleType
        self.make = make
        self.model = model
        self.dateReg = dateReg
        self.year = dateReg.year
        self.reg = reg
        
        self.cylinders = cylinders
        self.engine = Engine(cylinders)
        self.oil = Oil()
        self.battery = GenericComponent("Battery")
        self.wheelNumber = 0
        if "wheelNumber" in kwargs and kwargs["wheelNumber"] != 0:
            self.wheelNumber = kwargs["wheelNumber"]
        elif self.type == "Car":
            self.wheelNumber = 4
        elif self.type == "Motorcycle":
            self.wheelNumber = 2
    
        self.brakes = Brakes(self.wheelNumber)
        self.tyres = Tyres(self.wheelNumber)

        if self.type == "Motorcycle":
            self.chain = Chain()
        dateRegDelta = relativedelta(
            years=dateReg.year,
            months=dateReg.month,
            days=dateReg.day)

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
        if ((datetime.today().date() - self.dateReg).days)/365 < 3:
            return self.dateReg + relativedelta(years=+3)
        elif(self.lastMot != None):
            return self.lastMot + self.motInterval
        else:
            return "Unknown"
    
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
    
    def logComponent(self,component : GenericComponent):
        component.logNextService(self.mileage)

    def logComponents(self):

        self.logComponent(self.battery)

        print('------Engine------')
        for i in range(1,self.cylinders+1):
            self.logComponent(self.engine.getSparkPlug(i))
        print('------Oil------')
        self.logComponent(self.oil.filter)
        self.logComponent(self.oil.fluid)

        print('------Brakes------')
        for i in range(1,self.wheelNumber+1):
            self.logComponent(self.brakes.getCalliper(i))
            self.logComponent(self.brakes.getDisk(i))
        self.logComponent(self.brakes.fluid)

        print("------Tyres------")
        if self.wheelNumber == 4:
            self.logComponent(self.tyres.getTyre("F-Left"))
            self.logComponent(self.tyres.getTyre("F-Right"))
            self.logComponent(self.tyres.getTyre("B-Left"))
            self.logComponent(self.tyres.getTyre("B-Right"))
        elif self.wheelNumber == 2:
            self.logComponent(self.tyres.getTyre("Front"))
            self.logComponent(self.tyres.getTyre("Rear"))
        else:
            for i in range(1,self.wheelNumber+1):
                self.logComponent(self.tyres.getTyre(i))

        


