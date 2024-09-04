count = 0
for i in range (1,101):
    if(i%3==0 and i%5==0):
        count = count + 1
        print(i,"is divisible by 3 and 5")
print ("No of i's divisible by 3 and 5 =",count)