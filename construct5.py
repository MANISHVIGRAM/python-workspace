class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("ADD:",self.a+self.b)
    def sub(self):
        print("SUB",self.a-self.b)
    def mul(self):
        print("MUL:",self.a*self.b)
    def div(self):
        print("DIV:",self.a/self.b)
n1=calculator(10,2)
n1.add()
n1.sub()
n1.mul()
n1.div()
