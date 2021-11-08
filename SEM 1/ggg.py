n=int(input())
x=len(str(n))
y=[int(i)**x for i in str(n)]
if n==sum(y):
    print("armstrong")
else:
    print("not armstrong")
