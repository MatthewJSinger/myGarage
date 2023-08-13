from datetime import date
from dateutil.relativedelta import relativedelta


class ServiceRequirement:
    def __init__(self, date, miles):
            self.date = date
            self.miles = miles


class GenericComponent:
    def __init__(self, name):
        self.name = name

    def setCurrentMileage(self,miles):
        self.currentMileage = miles

    def setLastService(self, year:int,month:int,day:int, miles: int):
        lastServiceDate = date(year=year,month=month,day=day)
        self.lastService  = ServiceRequirement(lastServiceDate,miles)

    def setServiceInterval(self, years,months, miles):
        time = relativedelta(years=years,months=months)
        self.serviceInterval = ServiceRequirement(time, miles)


    def nextService(self,currentMileage: int):
        date = self.lastService.date + self.serviceInterval.date
        miles = self.serviceInterval.miles - currentMileage + self.lastService.miles
        return ServiceRequirement(date,miles)
    def logNextService(self, currentMileage):
        nextService = self.nextService(currentMileage)
        print(
f'''
-----{self.name} Due-----
Date Due: {nextService.date}
Miles Until Due: {nextService.miles}
''')


class Engine:
    def __init__(self, cylinders):
        self.sparkPlugs = {}
        for i in range(1,cylinders):
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
        for i in range(1,number):
            self.callipers[i] = GenericComponent("Brake Calliper " + str(i))
            self.disks[i] = GenericComponent("Break Disk " + str(i))

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

