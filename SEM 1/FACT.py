def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
while True:
    x=int(input("Enter a number to find factorial : "))
    print ("Factorial of ",x," is : ",fact(x))
