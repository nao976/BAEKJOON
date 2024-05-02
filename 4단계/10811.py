import math

N, M = map(int,input().split())
list = [i for i in range(1,N+1)]

for i in range(M):
    A, B = map(int,input().split())
    for j in range(math.ceil((B-A)/2)): #math.ceil切り上げ
        tmp=list[B-1-j]
        list[B-1-j]=list[A-1+j]
        list[A-1+j]=tmp

result = ' '.join(map(str,list))

print(result)