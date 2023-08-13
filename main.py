from Vehicle import Vehicle

if __name__ == '__main__':
    vehicle = Vehicle(
        "Motorcycle",
        "Kawasaki",
        "ER-6F",
        2016,
        "NB16 LYU",
        2
        )
    vehicle.setMileage(3000)
    vehicle.setLastMot(2022,7,22)
    vehicle.battery.setLastService(2022,7,22,600)
    vehicle.battery.setServiceInterval(9,0,6000)
    vehicle.printAllVehicleData()
    vehicle.battery.logNextService(vehicle.mileage)