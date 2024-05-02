N, M = map(int,input().split())
list = [i for i in range(1,N+1)]
# print(list)

for i in range(M):
    A, B = map(int,input().split())
    a = list[A-1]
    b = list[B-1]
    list[A-1] = b
    list[B-1] = a
    # print(list)

result = ' '.join(map(str,list))

print(result)