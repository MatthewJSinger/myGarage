from Components import *

class Vehicle:
    def __init__(self, vehicleType, make, model, year, reg, cylinders):
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