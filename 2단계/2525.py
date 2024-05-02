H,M = map(int,input().split())
T = int(input())

if (M+T)<60:
    M += T
elif (M+T)>=60:
    a = T//60
    H += a
    M += T%60
    
    if M >=60:
        H += 1
        M -= 60
    if M==60:
        H += 1
        M = 0
    if H >=24:
        H -=24 
    
print(H, M)