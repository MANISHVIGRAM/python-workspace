class bike:
    def __init__(self):
        self.name=""
        self.cc=0
    def display(self):
        print("Bike name:",self.name)
        print("bike cc:",self.cc)
    @classmethod
    def info(cls):
        print("This is bike cls")
    @staticmethod
    def infor():
        print("Static class")
gt = bike()
gt.name = "gt"
gt.cc=650
gt.display()
gt.infor()
bike.info()
bike.infor()