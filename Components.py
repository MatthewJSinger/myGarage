from datetime import date
from dateutil.relativedelta import relativedelta
from Util import nullCheck


class ServiceRequirement:
    def __init__(self, date, miles):
            self.date = date
            self.miles = miles


class GenericComponent:
    def __init__(self, name):
        self.name = name
        self.lastService = ServiceRequirement(None,None)
        self.serviceInterval = ServiceRequirement(None,None)

    def __repr__(self):
        repString = f'''
-----{self.name}-----
--Last Service--
Date: {self.lastService.date}
Mileage: {self.lastService.miles}
'''
        return repString

    def setCurrentMileage(self,miles):
        self.currentMileage = miles

    def setLastService(self, year:int,month:int,day:int, miles: int):
        lastServiceDate = date(year=year,month=month,day=day)
        self.lastService  = ServiceRequirement(lastServiceDate,miles)

    def setServiceInterval(self,miles, years=0, months=0):
        time = relativedelta(years=years,months=months)
        self.serviceInterval = ServiceRequirement(time, miles)


    def nextService(self,currentMileage: int):
        if self.lastService.date == None or self.serviceInterval.date == None:
            date = None
        else:
            date = self.lastService.date + self.serviceInterval.date
        if self.lastService.miles == None or self.serviceInterval.miles == None:
            miles = None
        else:
            miles = self.serviceInterval.miles - currentMileage + self.lastService.miles
        
        return ServiceRequirement(date,miles)
    def logNextService(self, currentMileage):
        nextService = self.nextService(currentMileage)
        print(
f'''
-----{self.name} Due-----
Date Due: {nullCheck(nextService.date)}
Miles Until Due: {nullCheck(nextService.miles)}
''')


class Engine:
    def __init__(self, cylinders):
        self.sparkPlugs = {}
        for i in range(0,cylinders):
            self.sparkPlugs[i] = GenericComponent("Spark Plug " + str(i))
    
    def getSparkPlug(self, id):
        return self.sparkPlugs[id]


class Oil:
    def __init__(self):
        self.filter = GenericComponent("Oil Filter")
        self.fluid = GenericComponent("Oil")

class Brakes:
    def __init__(self, number):
        self.fluid = GenericComponent("Break Fluid")
        self.callipers = {}
        self.disks = {}
        for i in range(0,number):
            self.callipers[i] = GenericComponent("Brake Calliper " + str(i))
            self.disks[i] = GenericComponent("Break Disk " + str(i))
    def getCalliper(self, num):
        return self.callipers[num]
    def getDisk(self, num):
        return self.disks[num]

class Chain: 
    def __init__(self):
        self.tension = GenericComponent("Chain Tension")
        self.cleanLube = GenericComponent("Clean and Lube")

class Tyres:
    def __init__(self, number):
        self.tyres = {}
        if number == 4:
            self.tyres["F-Left"] = GenericComponent("Front Left Tyre")
            self.tyres["F-Right"] = GenericComponent("Front Right Tyre")
            self.tyres["B-Left"] = GenericComponent("Back Left Tyre")
            self.tyres["B-Right"] = GenericComponent("Back Right Tyre")
        elif number == 2:
            self.tyres["Front"] = GenericComponent("Front Tyre")
            self.tyres["Rear"] = GenericComponent("Rear Tyre")
        else:
            for i in range (0,number):
                self.tyres[i] = GenericComponent("Tyre" + i)

    def getTyre(self, tyrePos):
        return self.tyres[tyrePos]

