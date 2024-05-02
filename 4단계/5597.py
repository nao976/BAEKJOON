list = [i+1 for i in range(30)]
for i in range(28):
    A = int(input())
    del list[list.index(A)]

print(list[0])
print(list[1])