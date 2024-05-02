X = int(input())

for i in range(X):
    listStr = list(input())
    output = listStr[0]
    output += listStr[len(listStr)-1]
    print(output)