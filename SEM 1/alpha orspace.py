a="abcdefghijklmnopqrstuvwxyz "
z=input()
for i in z:
    if i not in a:
        print("No")
        break
else:
    print("Yes")
