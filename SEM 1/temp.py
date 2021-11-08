x=int(input())
y=int(input())
if y==0:
  z=-1
elif x==0 and y!=0:
  z=0
else:
  x0=len(str(x))
  y0=len(str(y))
  x1=[]
  y1=[]
  for i in range(1,x0+1):
    if x>=1:
      x2=x//(10**(x0-i))
      x1.append(x2)
      x=x%(10**(x0-i))
    else:
      break
  for i in range(1,y0+1):
   if y>=1:
       y2=y//(10**(y0-i))
       y1.append(y2)
       y=y%(10**(y0-i))
   else:
       break
  print(x1,y1)
  for i in x1:
    if i in y1:
          x1.remove(i)
          y1.remove(i)
  print(x1,y1)
  a=1
  if len(x1)==0:
      x1.append(1)
  if len (y1)==0:
      y1.append(1)
  x3=0
  for i in x1:
      x3=x3+i*(10**(len(x1)-a))
      a=a+1
  a=1
  y3=0
  for i in y1:
      y3=y3+i*(10**(len(y1)-a))
      a=a+1
  if y3==0:
      z=-1
  else:
      z=x3/y3
z1=format(z,'0.2f')
print(z1)
