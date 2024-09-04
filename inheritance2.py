class dad:
    def money(self):
        print("Dad's money")
class mom(dad):
    def education(self):
        print("Mom's education")
class son(mom):
    iin= "MULTI LEVEL INHERITANCE"
vigram = son()
print(vigram.iin)
vigram.education()
vigram.money