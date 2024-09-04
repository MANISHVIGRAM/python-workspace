class Bike:
    def __init__(self):
        print("Finally I bought a bike....")
        self.cc=0
        self.bhp=0
        self.name=""
        self.speed=0
    def Speed(self):
        print("Bike name:",self.name)
        print("Top speed:",self.speed)
GT = Bike()
GT.name="GT 650"
GT.bhp=47
GT.cc=648
GT.speed=190
GT.Speed()
rc = Bike()
rc.name="RC 390"
rc.bhp=42
rc.cc=368
rc.speed=185
rc.Speed()