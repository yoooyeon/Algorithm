from collections import deque


def solution(edges):
    answer = [0, 0, 0, 0]  # 생성한 정점, 도넛, 막대, 8자
    cnt_map = {}  # value = [in, out]
    graph = {}
    generate_node = 0

    # in 2, out 2 -> 8
    # in 1, out 1 or (out 1 or in 1) -> 막대
    # in 1, out 1 -> 도넛

    #8자, 막대, 도넛 중 어느 그래프인지 찾는 메서드 
    def check(start):
        nonlocal answer
        q = deque([])
        q.append(start)
        visited = [start]
        if start not in graph:
            answer[-2] += 1
            return
        while q:
            node = q.popleft()
            in_, out = cnt_map[node]
            if in_ == 2 and out == 2:
                answer[-1] += 1
                return
            if (in_ == 0 and out == 1) or (in_ == 1 and out == 0):
                answer[-2] += 1
                return
            for next_node in graph[node]:
                if next_node not in visited and next_node not in q:
                    q.append(next_node)
        answer[-3] += 1

    for a, b in edges:
        if a not in cnt_map:
            cnt_map[a] = [0, 1]
        else:
            cnt_map[a][1] += 1
        if b not in cnt_map:
            cnt_map[b] = [1, 0]
        else:
            cnt_map[b][0] += 1
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    # 생성 정점 찾기
    for k, v in cnt_map.items():
        if v[0] == 0 and v[1] > 1:
            answer[0] = k
            generate_node = k
            break
    start_nodes = graph.pop(generate_node)
    # 그래프에서 생성 정점으로 가서 정점, 간선 확인
    for start_node in start_nodes:
        # 생성 노드와 연결된 간선은 제거
        cnt_map[start_node][0] -= 1 
        check(start_node)

    return answer
