# Python
파이썬과 친해지기

## 자료구조

**Double-Ended Queue**
```python
# https://docs.python.org/ko/3/library/collections.html#deque-objects
# FIFO 큐 구현할 때 리스트 대신 사용한다.
# 리스트 객체의 pop(0)는 O(n)인 반면 `deque` 객체의 popleft()는 O(1)

from collections import deque

queue = deque(iterable_object)
queue.append(data) # Enqueue
queue.popleft()    # Dequeue
```

**Priority Queue, Heap**
```python
# https://docs.python.org/ko/3/library/heapq.html
# `deque`와 달리 새 객체를 생성해주는 게 아니라 기존 iterable을 heapify 해준다.

import heapq

queue = []
heapq.heappush(queue, (k, v))
key, value = heapq.heappop()
```

## 수학

**몫과 나머지**
```python
# 몫과 나머지를 한번에 구하는 방법
# num = p * q + r

q, r = divmod(num, p)
```

## 시스템

**Standard Input**
```python
# 개행 문자까지 받아오지만 `input`보다 빠르다

import sys
line = sys.stdin.readline()
```

**Recursion Limit**
```python
# https://docs.python.org/ko/3/library/sys.html#sys.setrecursionlimit
# 최대 재귀 한도를 늘려야 할 때

import sys
sys.setrecursionlimit(num)
```