x=input("Enter Amount")
def fibonnaci (x):
    a=0
    b=1
    if x==1:
        print(a)
    else:
        print(a)
        print(b)
        for y in range(2,int(x)):
            z=a+b
            a=b
            b=z
            print(z)
print(fibonnaci(int(x))) 
