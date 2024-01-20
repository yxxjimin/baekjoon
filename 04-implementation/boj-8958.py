num = int(input())

for _ in range(num):
    quiz_input = list(input())
    aggregate_point = 0
    total_point = 0
    for ch in quiz_input:
        if ch == "O":
            aggregate_point += 1
        else:
            aggregate_point = 0
        total_point += aggregate_point
    print(total_point)
