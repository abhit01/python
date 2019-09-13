n=int(input("Enter a number to reverse it"))
rev = 0
while(n>0):
    dig=dig%10
    rev=rev*10+dig
    n=n//10
print(rev)  
