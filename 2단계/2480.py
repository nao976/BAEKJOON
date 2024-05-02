A,B,C = map(int,input().split())

if A==B and B==C and A==C:
    money = 10000+A*1000
elif A==B or B==C or A==C:
    if A==B:
        money = 1000+A*100
    elif B==C:
        money = 1000+B*100
    elif A==C:
        money = 1000+C*100
else:
    i = max([str(A),str(B),str(C)])
    money = int(i)*100

print(money)