import sys

input_line = int(input())

for i in range(input_line):
    line = sys.stdin.readline().split()
    print(int(line[0]) + int(line[1]))