import sys
while True:
    A=input("Do you want to check flames y(yes)/n(no):")
    if A=='y' or A=='yes':
        X,Y=input("Enter First Name:"),input("Enter Second Name:")
        X=X.lower();Y=Y.lower()
        X1,Y1=[i for i in X],[i for i in Y]
        f="FLAMES"
        for i in X1[:]:
            if i in Y1:
                X1.remove(i);Y1.remove(i)
        l1=len(X1)+len(Y1)
        l=l1
        while len(f)>1:
            while l>len(f):
                    l=l-len(f)
            else:
                l=l
            f=f[l::]+f[:l-1]
            l=l1
        R={'F':"FRIENDS",'L':"LOVERS",'A':"ADORE",'M':"MARRIAGE",'E':"ENEMIES",'S':"SISTER"}
        print(R[f])
    elif A=='n' or A=='no':
        print("bye bye")
        sys.exit()
    else:
        print("invalid input","Try once again")
        continue
