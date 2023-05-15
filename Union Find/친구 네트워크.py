import sys

input = sys.stdin.readline
n = int(input())


def add_name(name):
    global no, network
    tmp = no
    if name not in name_map.keys():
        name_map[name] = no
        network[no] = 1
        no += 1
    return tmp


def union(x, y):
    global network
    x = find(x)
    y = find(y)
    if x == y:
        return network[x]
    if x > y:
        parents[x] = y
        tmp = network[y] + network[x]
        network[x] = tmp
        network[y] = tmp
    else:
        parents[y] = x
        tmp = network[y] + network[x]
        network[x] = tmp
        network[y] = tmp
    return network[x]

def find(x):  # 부모 찾기
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


for _ in range(n):
    f = int(input())
    no = 0
    parents = [i for i in range(200001)]
    network = {}
    name_map = {}
    for _ in range(f):
        a, b = input().split()
        add_name(a)
        add_name(b)
        print(union(name_map[a], name_map[b]))
