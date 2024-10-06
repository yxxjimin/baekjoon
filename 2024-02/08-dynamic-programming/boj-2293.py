import sys


def main():
    num_coins, target = map(int, sys.stdin.readline().split())

    coins = []
    for _ in range(num_coins):
        coins.append(int(sys.stdin.readline()))

    dp_table = [0] * (target + 1)
    dp_table[0] = 1
    
    for coin in coins:
        for num in range(coin, target + 1):
            if num - coin >= 0:
                dp_table[num] += dp_table[num - coin]
    
    print(dp_table[-1])
            

if __name__ == "__main__":
    main()
