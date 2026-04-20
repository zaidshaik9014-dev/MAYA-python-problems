n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print("")

print("Perfect Number")
nc = int(input("Enter a number: "))
sum = 0
for i in range(1, nc):
    if(nc%i==0):
        sum=sum + i
        
if(sum==nc):
     print("Perfect Number")
else:
    print("Not a perfect")
    
