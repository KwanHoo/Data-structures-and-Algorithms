## DFS(Depth-First Search)
## 깊이우선탐색: 멀리있는 노드 우선 탐색, 스택 이용
## 구현 방법 : 재귀 함수 이용

##* DFS 메서드 정의
def dfs(graph, v, visited):
    ##* 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    ##* 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in  graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2D 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각노드가 방문된 정보를 리스트 자료형으로 표현 (1D 리스트)
visited = [False] * 9
print(visited)
# 정의된 DFS 함수 호출로
dfs(graph, 1, visited)
print(visited)