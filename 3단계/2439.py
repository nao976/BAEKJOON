X = int(input())
countX = 0
for i in range(X):
    countX +=1
    star = "*"*countX
    print(star.rjust(X))