#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#A = int(input())
#B = int(input())
#print(A+B)

#for文使用
A,B = (int(x) for x in input().split())
print(A+B)

#↑for文詳細（testの中身は文字列）
# test = input().split()
# print(test)

#模範解答（map関数）
# a, b = map(int, input().split())
# print(a+b)