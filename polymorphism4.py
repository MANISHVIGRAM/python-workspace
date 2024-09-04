class vehicle:
    def start(self):
        print("Vehicle started")
class car(vehicle):
    def start(self):
        print("Car stARTED")
car = car()
car.start()