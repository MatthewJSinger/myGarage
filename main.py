from Vehicle import Vehicle
from datetime import date

if __name__ == '__main__':
    vehicle = Vehicle(
        "Motorcycle",
        "Kawasaki",
        "ER-6F",
        date(2016,7,1),
        "NB16 LYU",
        2
        )
    vehicle.setMileage(3000)
    vehicle.setLastMot(2023,7,22)
    vehicle.battery.setLastService(2022,7,22,600)
    vehicle.battery.setServiceInterval(9,0,6000)
    vehicle.printAllVehicleData()
    print(vehicle.battery)
    vehicle.battery.logNextService(vehicle.mileage)