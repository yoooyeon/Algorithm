# 백준 1991

tree = {}
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]


# 전위, 중위, 후위 순회
def pre_order(a):
    global ans
    if a == ".":
        return
    ans += a
    if tree[a]:
        left, right = tree[a]
        pre_order(left)
        pre_order(right)


def post_order(a):
    global ans

    if a == ".": return
    if tree[a]:
        left, right = tree[a]
        post_order(left)
        post_order(right)
    ans += a


def in_order(a):

    global ans

    if a == ".": return
    if tree[a]:
        left, right = tree[a]
        in_order(left)
        ans += a
        in_order(right)


ans = ''
pre_order('A')
print(ans)

ans = ''
in_order('A')
print(ans)

ans = ''
post_order('A')
print(ans)
