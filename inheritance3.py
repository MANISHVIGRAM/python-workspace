class dad:
    def car(self):
        print("dad's car is BMW")
class mom:
    def scooty(self):
        print ("mom's is vespa")
class son(dad,mom):
    iin="MULTIPLE INHERITANCE"

manish = son()
print(manish.iin)
manish.car()
manish.scooty()