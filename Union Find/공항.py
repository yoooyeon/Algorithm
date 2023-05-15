# 백준 10775
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]
parent = [i for i in range(G+1)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


cnt = 0

for plane in planes:
    temp = find(plane)
    if temp == 0:
        break
    parent[temp] = parent[temp - 1]
    cnt += 1

print(cnt)
