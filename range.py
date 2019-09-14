n = int(input("Enter"))
p = int(input("Enter"))
k = int(input("Enter a number to be divided by"))

for i in range(n,p+1):
    if(i%k==0):
        print(i)
