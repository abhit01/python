def function():
    sum = M+E+S+H+C
    if(sum>450):
        print("A")
    elif(sum<450 and sum>350):
        print("B")
    elif(sum<350 and sum>250):
        print("C")
    elif(sum<250 and sum>150):
        print("D")
    else:
        print("E")
        




M = int(input("Enter marks obtained in maths"))
E = int(input("Enter marks obtained in english"))
S = int(input("Enter marks obtained in science"))
H = int(input("Enter marks obtained in hindi"))
C = int(input("Enter marks obtained in computer"))

if(M>100 or E>100 or S>100 or H>100 or C>100):
    print("Enter marks out of hundered")
else:
    function()
    
        
    
    

