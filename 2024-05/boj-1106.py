import sys


def main():
    num_customer, num_city = map(int, sys.stdin.readline().split())
    
    effects_of = dict()
    for _ in range(num_city):
        cost, effect = map(int, sys.stdin.readline().split())
        if cost in effects_of:
            effects_of[cost] = max(effect, effects_of[cost])
        else:
            effects_of[cost] = effect
    
    max_effect = max(effects_of.values())
    dp_table = [float('inf')] * (num_customer + max_effect)
    dp_table[0] = 0

    for i in range(1, num_customer + max_effect):
        dp_table[i] = min([dp_table[i - effects_of[cost]] + cost 
                           for cost in effects_of 
                           if i - effects_of[cost] >= 0] + [float('inf')])

    answer = [min(dp_table[i:i + max_effect]) for i in range(num_customer + 1)]

    print(answer[-1])


if __name__ == "__main__":
    main()
