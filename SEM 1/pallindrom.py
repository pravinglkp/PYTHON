a="Was it a car or a cat I saw"
a=a.lower()
print(a)
a=a.replace(" ","")
print(a)
if a==a[::-1]:
    print("Yes")
else:
    print("No")
