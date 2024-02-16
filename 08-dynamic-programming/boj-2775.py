import sys

test_cases = int(sys.stdin.readline())
answer = []

for _ in range(test_cases):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    
    # 0층 거주민 수
    residents = [i for i in range(15)]

    for _ in range(floor):
        # 각 층 거주민 수
        for i in range(1, room + 1):
            residents[i] += residents[i - 1]
    
    answer.append(residents[room])

print(*answer, sep='\n')
