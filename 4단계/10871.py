A, B = map(int,input().split())
listA = list(map(int,input().split()))
listB = []

for i in listA:
    if i < B:
        listB.append(i)

print(*listB)