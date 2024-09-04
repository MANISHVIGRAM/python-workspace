class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("TEACHER NAME:",self.name)
        print("TEACHER REG NO:",self.regno)
t1 = teacher("mANISH",1)
t1.display()
t2= teacher("VIGRAM",2)
t2.display()
