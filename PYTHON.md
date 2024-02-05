# Python
파이썬과 친해지기

## 자료구조
### Double-Ended Queue
[**`class collections.deque([iterable[, maxlen]])`**](https://docs.python.org/ko/3/library/collections.html#deque-objects)
- 리스트 자료형의 `pop(0)` 혹은 `insert(v, 0)`은 $O(n)$의 시간 복잡도를 갖는다.
    - 따라서 리스트로 FIFO 큐를 구현하면 값을 뺄 때마다 $O(n)$이 걸리게 된다.
- `deque`는 앞/뒤, 삽입/삭제 모두 $O(1)$으로 수행할 수 있다.
    - FIFO 큐를 구현할 때에는 `deque`를 사용하자.

```python
from collections import deque

queue = deque(iterable_object)
queue.append(data) # Enqueue
queue.popleft()    # Dequeue
```

## 시스템
### Read Line
**`sys.stdin.readline()`**
- 데이터를 한꺼번에 버퍼에 넣는다.
- 개행 문자까지 포함해서 값을 반환한다.
    - `strip()`, `split()`, `int()` 등을 통해 직접 처리해주자.
- `input()`이 느린 이유
    - 프롬프트 문자열을 출력한다.
    - 키를 누를 때 마다 데이터가 한 개씩 버퍼에 들어간다.
    - 개행 문자를 입력 종료로 간주하고 알아서 처리(제거)해준다.

### Recursion Limit
[**`sys.setrecursionlimit(limit)`**](https://docs.python.org/ko/3/library/sys.html#sys.setrecursionlimit)
- DFS와 같이 재귀함수를 사용할 때에는 최대 재귀 한도 깊이를 늘려주어야 한다.