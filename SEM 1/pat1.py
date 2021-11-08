s=6
x=int(input("distance of sameland:"))
y=int(input("distance of upwordland:"))
z=int(input("distance of downland:"))
m1=int(input("being time in Andrews home"))
t1=x/50+y/(100/3)+z/100
t2=t1+m1+x/50+y/100+z/(100/3)
if t1<60:
    print("reaching Andrews home at:",int(s),"hours",int(t1),"minutes")
else:
    h1=t1//60
    m1=t1%60
    print("reaching Andrews home at:",int(s+h1),"hours",int(m1),"minutes")
if t2<60:
    print("reaching back his home at:",int(s),"hours",int(t2),"minutes")
else:
    h2=t2//60
    m2=t2%60
    print("reaching back his home at:",int(s+h2),"hours",int(m2),"minutes
