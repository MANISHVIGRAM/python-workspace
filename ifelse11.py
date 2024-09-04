salary=int(input("Enter the salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25 ):
    amount=int(input("Enter loan amount: "))
    if(amount<=50000):
        print("Eligible for loan")
    else:
        print("Maximum limit of loan amount is 50000")
else:
    print("not eligible for loan")