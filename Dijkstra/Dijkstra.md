# 다익스트라

1. 시작 정점을 선택하고 시작 정점에서의 거리를 0으로 설정하고, 나머지 정점들의 거리를 무한대(INF)로 초기화한다.
2. 시작 정점에서 인접한 정점들을 탐색하며, 해당 정점으로 가는 거리를 업데이트한다. 시작 정점에서 인접한 정점으로 가는 거리는 간선의 가중치(비용)로 결정된다.
3. 아직 방문하지 않은 정점 중에서 거리가 가장 짧은 정점을 선택한다. 이를 위해 우선순위 큐나 최소 힙을 사용한다.
4. 선택한 정점을 방문하고, 해당 정점에서 인접한 정점들의 거리를 업데이트한다.
5. 위의 과정을 모든 정점을 방문할 때까지 반복
