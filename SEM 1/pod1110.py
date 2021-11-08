while True:
    w=input()
    w=[i for i in w]
    l1,l2=[chr(i+97) for i in range(13)],[chr(i+97) for i in range(13,26)]
    for i in w:
        if i in l1:
            if not l2[l1.index(i)] in w:
                print("Lost")
                break
        if i in l2:
            if not l1[l2.index(i)] in w[:w.index(i)]:
                print("Lost")
                break
        if i in l1:
            if not l2[l1.index(i)] in w[w.index(i)+1]:
                if not (l2[l1.index(i)] in w[0] or l2[l1.index(i)] in w[len(w)-1]):
                    print("Lost")
                    break
    else:
        print("Won")
    print("..........")
