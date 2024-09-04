eng=int(input("Enter english mark: "))
tamil=int(input("Enter tamil mark: "))
maths=int(input("Enter maths mark: "))
science=int(input("Enter science mark: "))
social=int(input("Enter social mark: "))
total = eng + tamil + maths + science + social
average = total / 5
if(average<35):
    print("Additional class is required")
else:
    print("Your good to go")