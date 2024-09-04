class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,grade,name):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(self.name,self.grade)
std1 = student("A","Manish")
std1.display()