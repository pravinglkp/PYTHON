m=input()
es=""
es1=""
r=""
i=0
while i<len(m):
    a=m[i]
    if a.isalpha():
        r=r+a
    elif a.isdigit():
            if es=="":
                es=es+a
            elif es[(len(es)-1)]<a:
                es=es+a
            elif es[(len(es)-1)]>=a:
                for j in range (len(es)-1,-1,-1):
                    r=r+es[j]
                es=""
                es=es+a
    elif a=='(':
        for j in range(m.find('(')+1,m.find(')')):
            a=m[j]
            if a.isalpha():
                r=r+a
            elif a.isdigit():
                if es1=="":
                    es1=es1+a
                elif es1[(len(es1)-1)]<a:
                    es1=es1+a
                elif es1[(len(es1)-1)]>a:
                    for j in range (len(es1)-1,-1,-1):
                        r=r+es1[j]
                    es1=""
                    es1=es1+a
        for j in range((len(es1)-1),-1,-1):
              a=es1[j]
              r=r+a
        i=m.find(')')
        continue
    i=i+1
a=es[::-1]
r=r+a
print(r)
