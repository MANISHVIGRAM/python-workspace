class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=100
        b=2
        return l*b
r1 = rectangle()
print(r1.area())