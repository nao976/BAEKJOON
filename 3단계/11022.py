X = int(input())

for i in range(X):
    A, B = map(int,input().split())
    case = str(i+1)
    sum = str(A+B)
    print("Case #" + case + ": " + str(A) + " + " + str(B) +" = " + sum)