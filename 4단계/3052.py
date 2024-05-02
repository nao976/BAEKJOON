list = []
list2 = []
for i in range(10):
    list.append(input())

for i in list:
    a = int(i)%42
    list2.append(a)
# print(list2)

s = set(list2)
# print(s)
print(len(s))