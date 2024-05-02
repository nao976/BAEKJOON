H,M = map(int,input().split())
T = int(input())

# if (M+T)<60:
#     print(print(H, (M+T)))
# elif (M+T)>=60:
#     a = 60-M
#     M = T-a
#     if M<60:
#         print((H+1), M)

# if (M+T)<60:
#     print(print(H, (M+T)))
# else:
#         if T>60:
#             a = T//60
#             b = T - (60*a)
#             H = H + a
#             T = M + b
#             if T ==60:
#                 H = H + 1
#                 T = 0
# print(H, T)

if (M+T)<60:
    print(H, (M+T))
elif (M+T)==60:
    H = H + 1
    M = 60-T
    print(H, T)
elif (M+T)>60:
    while T > 60:
        H += 1
        T -= 60
        # M = (M+T)-60
    M = (M+T)
    if M==60:
        H += 1
        M = 0
    if H >=24:
        H -=24    
    print(H, M)


