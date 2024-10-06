n = int(input())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))

seq_A.sort()

# B를 정렬하면 안된다고 되어있다.
# 그러면 (정렬된 A[i]) * (B의 i번째 최댓값)을 n번 해줘야 하는데
# i번째 최댓값을 n번 탐색하는 과정 자체가 선택 정렬과 완전히 동일한 프로세스이다.
# 따라서 이 방식으로 수행하면 시간 복잡도가 O(n**2)이 된다.
# 그래서 B도 그냥 O(n logn)으로 정렬해서 풀었다.
seq_B.sort(reverse=True)
sum_ = sum([seq_A[i] * seq_B[i] for i in range(n)])

print(sum_)
