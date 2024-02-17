import sys, bisect

seq_len = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

# lis_len = [0] * seq_len
# for i in range(seq_len):
#     lis_len[i] = 1
#     for j in range(i):
#         if sequence[j] < sequence[i] and lis_len[j] + 1 > lis_len[i]:
#             lis_len[i] = lis_len[j] + 1

# print(max(lis_len))

answer = [-1]
for num in sequence:
    if num > answer[-1]:
        answer.append(num)
    else:
        answer[bisect.bisect_left(answer, num)] = num

print(len(answer) - 1)
