X = int(input())

for i in range(X):
    A, B = map(str,input().split())
    listStr = list(B)
    result = ""
    for j in listStr:
        result += j*int(A)
    
    print(result)