class dad:
    def phone(self):
        print("dad's phone")
class son(dad):
    def lap(self):
        print("SINGLE level INHERITANCE")
        print("son's lap")
manish = son()
manish.lap()
manish.phone()