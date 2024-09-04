a=[]
sum=0
count=0
for i in range (1,11):
    num = int(input("Enter the number "))
    a.append(num)
    count=count+1
for i in a:
    sum = sum + i
    count = count+1
avg = sum/count
print("SUM =",sum)
print("AVERAGE =",avg)