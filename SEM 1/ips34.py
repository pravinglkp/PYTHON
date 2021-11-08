a=[]
c=0
n=int(input('total'))
w="unique"
for n in range(c,n,1):
   x=int(input("value"))
   if x in a:
       w="dublicate"
       break
   a.append(x)
   c=c+1
print(w)

       
