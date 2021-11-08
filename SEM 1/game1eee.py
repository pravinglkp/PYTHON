import random
print("......................................PRAVIN~G.........Game.............................")
print(".......Are you ready to play with me..........")
print("......Enter yes or no.......")
x=input()
if x=="yes":
    L=1
    U=10
    print("Find a number 'X' which Pravin G's programme think ")
    T=random.randint(L,U)
    found=False
    i=0
    while not found:
        X=False
        while X==False:
            print("That number is between", L,"<=X<=",U)
            trail=int(input("Enter your guess:"))
            x=L<=trail<=U
            if x:
                break
            else:
                print("You entered wrong number")
                print("Try once again")
                continue
        i=i+1
        if trail==T:
            found==True
            print("Congrats,you succed in ",i,"attempts")
            break
        elif trail> T:
            U=trail
            print("your guess is wrong")
        else:
            L=trail
            print("your guess is wrong")
elif x=="no":
    print("ok ,no problem")
else:
    print("Sorry your answer is wrong")
    print("Can you tell once again")
print(".............bye,bye....................")
