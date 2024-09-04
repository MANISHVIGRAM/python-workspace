class Student:
    def __init__(self):
        self.name=""
        self.regno=0
    def display(self):
        print("NAME:",self.name)
        print("REGISTER NO:",self.regno)
std1=Student()
std1.name="MANISH"
std1.regno=19106069
std1.display()
print()
std2=Student()
std2.name="MAHESH"
std2.regno=19106066
std2.display()