n, k = map(int, input().split())
input_number = input()

assert(n == len(input_number))

final_number = []
final_digit = n - k
for digit in input_number:
    while k > 0 and len(final_number) > 0 and digit > final_number[-1]:
        final_number.pop()
        k -= 1
    if len(final_number) < final_digit:
        final_number.append(digit)

print(''.join(final_number))
