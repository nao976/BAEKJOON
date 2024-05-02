x = int(input())
y = list(map(int,input().split()))
M = max(y)
average = 0

for i in range(x):
    average += y[i]/M*100
print(average/x)