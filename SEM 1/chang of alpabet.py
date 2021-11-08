w,d=input(),int(input())
W=[chr((ord('a')+(ord(i)-ord('a'))%26)+d) for i in w]
for i in W:print(i,end='')
