# 05. DFS/BFS

> [!NOTE]
> 그래프/배열 탐색하기

## 이론
### 그래프
- 인접 행렬(Adjacency Matrix) 혹은 인접 리스트(Adjacency List)로 구현한다.
- **인접 행렬**: $V \times V$ 2차원 배열에 인접 노드 간 거리(가중치) 혹은 연결 여부를 기록한다. 
    - 가중치가 있는 그래프에서는 인접하지 않은 노드의 거리를 무한대로 설정한다.
        - Python `sys.maxsize`, C++ `std::INT_MAX` 등
    - 가중치가 없는 그래프에서는 인접한 노드의 거리를 1, 인접하지 않은 노드의 거리를 0으로 설정한다.
    - ✅ **장점**
        - 특정 간선의 존재 여부를 $O(1)$에 확인할 수 있다.
    - ❌ **단점**
        - 공간 복잡도가 $O(V^2)$이다.
            - 특히 간선의 개수가 적을수록 낭비되는 공간이 많아진다.
        - 모든 인접 노드를 방문하려면 인접 노드의 개수와 상관없이 $O(V)$가 걸린다.

- **인접 리스트**: $V$개의 '연결 리스트(Linked list)'로 구성된 배열로 구현한다.
    - 각 연결 리스트는 특정 노드와 연결되어 있는 노드들을 나타낸다.
    - ✅ **장점**
        - 희소(sparse)할 수록 메모리 측면에서 효율적이다.
        - 인접한 모든 노드를 방문해야할 때 유리하다.
    - ❌ **단점**
        - 특정 간선의 존재 여부를 확인하려면 연결 리스트를 순회해야 한다(최대 $\Theta (V)$).
    
```python
# 리스트 중첩 방식
# [
#   [1, 2, 4],
#   [0, 2],
#   [0, 1, 3, 4],
#   [2, 4],
#   [0, 2, 3]
# ]
adjacency_list = [[] for _ in range(num_v)]
for src, dst in all_edges:
    adjacency_list[src].append(dst)

# 노드를 키(key), 인접 노드들을 값(value)으로 갖는 딕셔너리 방식
# {
#   0: {1, 2, 4},
#   1: {0, 2},
#   2: {0, 1, 3, 4},
#   3: {2, 4},
#   4: {0, 2, 3}
# }
adjacency_list = {}
for src, dst in all_edges:
    if src not in adjacency_list:
        adjacency_list[src] = set()
    adjacency_list[src].add(dst)
```

- 어떤 방식으로 탐색을 해야 할까?
    1. 시작점을 탐색 후보군에 넣는다.
    2. 탐색 후보군에서 노드를 하나 선택한다.
    3. 선택한 노드의 인접 노드들을 확인한다.
    4. 이 인접 노드들 중 이전에 탐색하지 않았던 것이 있다면 탐색 후보군에 넣어둔다.
    5. 반복

### Depth-First Search
- 최대한 깊숙하게 들어가서 탐색한 후 다시 돌아와서 다른 경로로 탐색하는 알고리즘이다.
    - 한 경로를 끝까지 탐색하고 이전 노드로 돌아오는 과정을 *백트래킹*이라고 한다.
- 모든 간선을 조회하므로 인접 리스트에서는 $O(V + E)$, 인접 행렬에서는 $O(V^2)$이다.
    - 따라서 일반적으로 인접 리스트를 사용한다.
- 가장 최근에 발견한(Last in) 인접 노드 중 하나를 바로 다음 시점에서 탐색하기 때문에 LIFO 스택(혹은 재귀)을 사용한다.
    1. 시작점을 스택에 삽입한다.
    2. 스택에서 노드를 꺼내고 방문하지 않았다면 방문 처리한다.
    3. 꺼낸 노드의 인접 노드들을 확인한다.
    4. 이 인접 노드들 중 이전에 탐색하지 않았던 것을 스택에 삽입한다.
    5. 반복

**1. 재귀 함수를 이용한 구현**
```
procedure DFS(G, v) is
    label v as discovered
    for all edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

```python
def dfs(node: int):
    visited[node] = True
    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            dfs(adj_node)

dfs(root_node)
```

**2. 명시적인 스택을 이용한 구현**
```
procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                if w is not labeled as discovered then 
                    S.push(w)
```

```python
stack = [root_node]
while stack:
    node = stack.pop(0)
    if not visited[node]:
        visited[node] = True
        for adj_node in adj_list[node]: # 방문하지 않은 모든 인접 노드 한꺼번에 삽입
            if not visited[adj_node]:
                stack.append(adj_node)
```

### Breadth-First Search
- 시작점으로부터 가까운 노드부터 탐색하는 알고리즘이다.
    - 트리 구조라면 깊이가 $d$인 노드를 모두 탐색하고 나서 깊이가 $d + 1$인 노드들을 탐색하는 것이다.
- 인접 리스트로 구현한다.
- FIFO 큐를 사용하면 자연스럽게 가까운 노드부터 탐색하게 된다.
    1. 시작점을 FIFO 큐에 삽입하고 방문 처리한다.
    2. FIFO 큐에서 노드를 꺼낸다.
    3. 꺼낸 노드의 인접 노드들을 확인한다.
    4. 이 인접 노드들 중 이전에 탐색하지 않았던 것들을 모두 FIFO 큐에 삽입하고 방문 처리한다.
    5. 반복

```
procedure BFS(G, root) is
    let Q be a queue
    label root as explored
    Q.enqueue(root)
    while Q is not empty do
        v = Q.dequeue()
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as explored then
                label w as explored
                Q.enqueue(w)
```

```python
from collections import deque
queue = deque([root_node])
while queue:
    node = queue.popleft()
    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            queue.append(adj_node)
```

- 방문 처리를 삽입 시점에 하는 이유[^1]
    - 큐(BFS) 혹은 스택(DFS)에 삽입되는 순서와 실제로 노드를 탐색하는 순서(=방문 처리해야 할 순서)는 별개이다.
    - DFS에서는 스택에 들어오는 순서와 나가는 순서가 다르다(LIFO).
        - 따라서 실제로 노드를 탐색하는 시점에 방문 처리를 해준다.
    - BFS에서는 큐에 들어오는 순서와 나가는 순서가 같다(FIFO).
        - 그러므로 삽입되는 순서와 실제로 탐색한 순서가 동일할 것이다.
        - 따라서 삽입되는 순서대로 방문 처리를 해주어도 문제가 되지 않는다.
        - 오히려 큐에 삽입되는 시점에 방문 처리를 미리 해주면 한 번 삽입되어 "처리될" 노드가 다시 삽입되는 것을 방지해준다.
- 현재 시점의 깊이를 기록하고 싶다면 아래와 같이 `while`문 안에 `for`문을 추가적으로 중첩시키자.
    - 최단 경로 문제처럼 경로의 길이(깊이) 값을 구해야되는 문제에서 활용할 수 있을 것 같다.
- 큐에서 뽑을 때 `list.pop(0)`은 $O(N)$만큼 걸리기 때문에 $O(1)$인 `deque.popleft()`를 사용하자.

```python
distance = 0
while queue:
    # 동일한 깊이의 노드들을 for 루프 안에서 처리
    # while문의 각 iteration은 현재의 깊이를 나타냄
    #   Iter 0: distance = 0
    #   Iter 1: distance = 1
    #   ...
    for _ in range(len(queue)):
        node = queue.pop(0)
        for adj_node in adj_list[node]:
            ...
    distance += 1
```

### DFS와 BFS의 차이점
- 구현 방식
    - BFS는 FIFO 큐를 사용하고 DFS는 스택(재귀)를 사용한다.
- 목표 지점까지의 경로 찾아가기
    - BFS는 그래프의 깊이가 무한히 깊어져도 반드시 최단 경로를 찾아낼 수 있다.
        - 문제에서 *최단 경로*, *최소 길이* 등을 찾아보자.
        - 다만 목표 지점의 깊이가 깊어질수록 경로를 찾는 시간이 길어진다.
        - 따라서 노드 수가 적고 깊이가 얕은 해가 존재할 때 유리하다.
    - DFS는 목표 지점의 깊이가 깊어도 빠르게 경로를 찾을 수 있다.
        - 다만 최단 경로임을 보장할 수 없고
        - 해가 아닌 경로가 매우 깊을 때 빠져나오기 어렵다.
- 메모리
    - BFS는 노드 수가 많아질수록 큐에 저장할 노드도 많아져서 메모리가 많이 필요하다.
    - DFS는 현재 경로 상 백트래킹으로 돌아갈 노드들만 알아도 되기 때문에 메모리 부담이 적다.

[^1]: https://sungone-develop-study.tistory.com/entry/DFS-%EC%99%80-BFS%EC%9D%98-%EB%B0%A9%EB%AC%B8%EC%B2%98%EB%A6%AC-%EC%8B%9C%EC%A0%90%EC%9D%80-%EC%99%9C-%EB%8B%A4%EB%A5%BC%EA%B9%8C