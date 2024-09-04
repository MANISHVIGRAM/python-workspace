class dad:
    def money(self):
        print("dad's money")
class land :
    def property(self):
        print("s1 property")
class son1(dad,land):
    pass
class son2(dad):
    pass
s1 = son1()
s2 = son2()
s1.money()
s1.property()
s2.money()