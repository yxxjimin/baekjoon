# 05. DFS/BFS

> [!NOTE]
> 그래프/배열에서 어떻게 탐색할까?

## 이론
### 그래프
- 인접 행렬(Adjacency Matrix) 혹은 인접 리스트(Adjacency List)로 구현한다.
- **인접 행렬**: $V \times V$ 2차원 배열에 인접 노드 간 거리를 기록한다. 
    - 인접하지 않는 노드의 거리는 무한대로 설정한다.
        - Python `sys.maxsize`, C++ `std::INT_MAX` 등
- **인접 리스트**: $V$개의 '연결 리스트(Linked list)'로 구성된 배열로 구현한다.
    - 각 연결 리스트는 특정 노드와 연결되어 있는 노드들을 나타낸다.

| |인접 행렬|인접 리스트|
|-|-|-|
|**장점**✅|- 두 노드의 인접성을 $O(1)$에 확인 가능|- 희소(sparse)할 수록 메모리 측면에서 효율적 </br> - 특정 노드와 인접한 모든 노드들을 얻기 쉬움|
|**단점**❌|- 공간 복잡도가 $O(V^2)$| - 두 노드의 인접성을 확인하기 어려움 </br> - 밀집(dense)될수록 비효율적|

- 어떻게 하면 그래프의 모든 노드들을 빠짐없이 탐색할 수 있을까?
    1. 시작점을 탐색 후보군에 넣는다.
    2. 탐색 후보군에서 노드를 하나 선택한다.
    3. 선택한 노드의 인접 노드들을 확인한다.
    4. 이 인접 노드들 중 이전에 탐색하지 않았던 것이 있다면 탐색 후보군에 넣어둔다.
    5. 반복

### Depth-First Search
- 최대한 깊숙하게 들어가서 탐색한 후 다시 돌아와서 다른 경로로 탐색하는 알고리즘이다.
    - 한 경로를 끝까지 탐색하고 이전 노드로 돌아오는 과정을 *백트래킹*이라고 한다.
- 가장 최근에 발견한(Last in) 인접 노드 중 하나를 바로 다음 시점에서 탐색하기 때문에 LIFO 스택(혹은 재귀)을 사용한다.
    1. 시작점을 스택에 삽입한다.
    2. 스택에서 노드를 꺼내고 방문하지 않았다면 방문 처리한다.
    3. 꺼낸 노드의 인접 노드들을 확인한다.
    4. 이 인접 노드들 중 이전에 탐색하지 않았던 것들을 모두 스택에 삽입한다.
    5. 반복

```
# 재귀
procedure DFS(G, v) is
    label v as discovered
    for all edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

```
# 스택
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

### Breadth-First Search
- 시작점으로부터 가까운 노드부터 탐색하는 알고리즘이다.
    - 트리 구조라면 깊이가 $d$인 노드를 모두 탐색하고 나서 깊이가 $d + 1$인 노드들을 탐색하는 것이다.
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

- 혹은 아래와 같은 형태로 짜면 현재 시점의 깊이를 기록할 수 있다.
    - 최단 경로 문제처럼 경로의 길이(깊이) 값을 구해야되는 문제에서 잘 활용하자.

```python
distance = 0
while not queue.empty():
    # 동일한 깊이의 노드들은 for 루프 안에서 처리하자
    for _ in range(len(queue)):
        v = queue.pop(0)
        ...
    distance += 1
```

### DFS와 BFS의 차이점
- BFS와 스택을 사용한 DFS의 구현 차이점은 크게 두 가지이다.
    - 스택 대신 큐를 사용한다.
    - DFS는 실제로 탐색을 시작할 때 방문 처리를 하고 BFS는 큐에 삽입될 때 방문 처리한다.
        - 다만 DFS도 이코테 본문에서처럼 스택에 노드를 한 번에 하나씩만 삽입하면 삽입 시점에 방문 처리해도 무관하다.
- 방문 처리되는 시점이 다른 이유[^1]
    - 큐/스택에 삽입되는 순서와 실제로 노드를 탐색하는 순서(방문 처리되어야 할 순서)는 별개이다.
    - 따라서 스택을 사용하는 DFS에서는 실제로 노드를 탐색하기 시작하는 시점에 방문 처리를 해준다.
    - 다만 큐에서는 들어오는 순서와 나가는 순서가 같기 때문에 삽입되는 순서와 실제로 탐색한 노드의 순서가 동일할 것이다.
        - 따라서 삽입되는 순서대로 방문 처리를 해주어도 문제가 되지 않는다.
        - 오히려 큐에 삽입되는 시점에 방문 처리를 해주면 한 번 삽입되어 "처리될" 노드가 다시 삽입되는 것을 방지해준다.
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