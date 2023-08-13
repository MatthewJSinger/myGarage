from Vehicle import Vehicle
from datetime import date

if __name__ == '__main__':
    vehicle = Vehicle(
        vehicleType="Motorcycle",
        make="Kawasaki",
        model="ER-6F",
        dateReg=date(2016,7,1),
        reg="NB16 LYU",
        cylinders=2
        )
    vehicle.setMileage(3000)
    vehicle.setLastMot(2023,7,22)
    vehicle.battery.setLastService(2022,7,22,600)
    vehicle.battery.setServiceInterval(6000,years=9)
    vehicle.printAllVehicleData()
    print(vehicle.battery)
    vehicle.battery.logNextService(vehicle.mileage)