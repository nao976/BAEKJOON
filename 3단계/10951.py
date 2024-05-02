while True:
    try:
        inpAB = input()
        A, B = map(int,inpAB.split())
        print(A+B)
    except:
        break