SumAll = int(input())
input_line = int(input())
CheckSum = 0

for i in range(input_line):
    A,x = map(int,input().split())
    CheckSum += (A*x)

if SumAll==CheckSum:
    print("Yes")
else:
    print("No")