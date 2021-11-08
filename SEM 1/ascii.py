a="ab"
i=0;
total1=0
while i<(len(a)):
    c=a[i]
    print("ascii value of",a[i],ord(c))
    total1=total1+ord(c)
    i=i+1
else:
    avg=total1/len(a)
    print(avg)
