A,B = map(int,input().split())

if B >= 45:
    print(A, (B-45))
elif B < 45 and A != 0:
    B = 45 - B
    print((A-1), (60-B))
elif B < 45 and A == 0:
    B = 45 - B
    print(23, (60-B))