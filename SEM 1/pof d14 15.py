N=0
while N<=50:
 if 0<=N<=50:
  if 2<=N<=50:
    for i in range(N,0,-1):
        a=2*N+1-2*i
        print('*'*i,end=' '*a)
        print('*'*i)
    for i in range(2,N+1):
        b=2*N+1-2*i
        print('*'*i,end=' '*b)
        print('*'*i)
  else:
        print("impossible")
 N=N+1
