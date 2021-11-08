print("enter the time in 12 hours format")
H=int(input("HH"))
M=int(input("MM"))
S=int(input("SS"))
x=input("A.M or P.M or noon or midnight")
if x== "A.M":
    if H<8:
      print(H,":",M,":",S,"A.M")
    elif H==8:
      print(H,":",M,":",S,"midmorning")
    else:
      print(H-8,":",M,":",S,"B.M")
if x== "noon":
    print(H-8,":",M,":",S,"B.M")
if x== "P.M":
    if H<4:
        print(H+4,":",M,":",S,"B.M")
    elif H==4:
        print(H+4,":",M,":",S,"midevening")
    else:
        print(H-4,":",M,":",S,"C.M")
if x== "midnight":
      print(H,":",M,":",S,"midnight")
    
