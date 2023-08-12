class Vehicle:
    def __init__(vehicleType, make, model, year, reg, cylinders):
        self.type = vehicleType
        self.make = make
        self.model = model
        self.year = year
        self.reg = reg

        self.engine = Engine(cylinders)
        self.oil = Oil()
        

    def setMileage(self, mielage):
        self.setMileage = mielage

    def setLastMot(self, motDate):
        self.lastMot = motDate

    def setMotInterval(self, interval):
        self.motInterval = interval

    def motDate(self):
        return self.lastMot + self.motInterval

class GenericComponent:
    def __init__(self, name):
        self.name = name

    def setLastService(self, lastService):
        self.lastService = lastService

    def setServiceInterval(self, interval):
        self.serviceInterval = interval

    def nextService(self):
        return self.lastService + self.serviceInterval

class Engine:
    def __init__(self, cylinders):
        self.sparkPlugs = {}
        for i in range(1,cylinders):
            self.sparkPlugs[i] = GenericComponent("Spark Plug " + i)
    
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
            self.callipers[i] = GenericComponent("Brake Calliper " + i)
            self.disks[i] = GenericComponent("Break Disk " + i)

class Chain: 
    def __init__(self):
        self.tension = GenericComponent("Chain Tension")
        self.cleanLube = GenericComponent("Clean and Lube")


