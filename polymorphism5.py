class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
class Mnager(employee):
    def __init__(self,name,sal,department):
        super().__init__(name,sal)
        self.department=department
    def display(self):
        print("NAME:",self.name)
        print("SALARY:",self.sal)
        print("DEPARTMENT:",self.department)
m1 = Mnager("Manish",100000,"DEVELOPER")
m1.display()