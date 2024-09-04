class goa:
    name=""
    drink=""
    def party(self):
        print("Lets party..........")
    def beach(self):
        print("Enjoying the beach")
manish = goa()
vigram = goa()
manish.name="Manish"
vigram.name= "Vigram"
print(manish.name)
print(vigram.name)
vigram.drink="no"
manish.drink="yes"
print(manish.drink)
print( vigram.name,"DRINK :",vigram.drink)
manish.party()
vigram.beach()