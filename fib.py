def fibonacci(n):
    x=0
    y=1
    if n==1:
        print(x)
    else:
        print(x)
        print(y)
        for f in range(2,n):
            k=x+y
            x=y
            y=k
            print(k)
print(fibonacci(15))