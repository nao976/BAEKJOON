N, M = map(int,input().split())
list = [0 for _ in range(N)]
# N = 5の場合、list → [0, 0, 0, 0, 0]
# print(list)
# result = ""
for i in range(M):
    A, B, C = map(int,input().split())
    for j in range(A-1,B):
        list[j] = C
result = ' '.join(map(str,list))
# for i in list:
#     result += str(list[i])
print(result)
    # if B-A == 1:
        # list[B-1] = C
    # else:
# print(list)
# list2 = [i for i in range(M)]
# print(list1)
# print(list2)


# if B-A == 0:
    #     list[A-1] = C
    # elif B-A == 1:
    #     list[A-1] = C
    #     list[B-1] = C
    # elif B-A == 2:
    #     list[A-1] = C
    #     list[A] = C
    #     list[B-1] = C
    # elif B-A == 3:
    #     list[A-1] = C
    #     list[A] = C
    #     list[B-1] = C
    #     list[B-2] = C
    # elif B-A == 4:
    #     list[A-1] = C
    #     list[A] = C
    #     list[B-1] = C
    #     list[B-2] = C
    #     list[B-3] = C