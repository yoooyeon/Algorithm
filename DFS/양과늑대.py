from collections import defaultdict


def solution(info, edges):
    answer = 0
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    # print(tree)
    visited = [0 for _ in range(len(info))]

    def dfs(sheep, wolf):
        nonlocal answer
        # print(num, sheep, wolf)

        if wolf < sheep:
            answer = max(sheep, answer)
        else:
            return
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            is_wolf = info[child]
            if not visited[child] and visited[parent]:
                visited[child] = 1
                dfs(sheep + (is_wolf == 0), wolf + (is_wolf == 1))
                visited[child] = 0

    visited[0] = 1
    dfs(1, 0)
    return answer

