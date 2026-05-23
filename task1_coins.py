from collections import defaultdict
from time import perf_counter

# coin denominations in descending order
COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    coins_used = defaultdict(int)
    for coin in COINS:
        count, amount = divmod(amount, coin)
        if count:
            coins_used[coin] = count
    return dict(coins_used)


def find_min_coins(amount: int) -> dict:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    coins_used = defaultdict(int)

    for lesser_amount in range(1, amount + 1):
        for coin in COINS:
            if (
                coin <= lesser_amount
                and dp[lesser_amount - coin] + 1 < dp[lesser_amount]
            ):
                dp[lesser_amount] = dp[lesser_amount - coin] + 1
                coin_used[lesser_amount] = coin

    lesser_amount = amount
    while lesser_amount > 0:
        coin = coin_used[lesser_amount]
        if coin > 0:
            coins_used[coin] += 1
            lesser_amount -= coin

    return dict(coins_used)


if __name__ == "__main__":
    amount = 113
    large_amount = 99991

    print(f"Greedy result for {amount}:", find_coins_greedy(amount))
    print(f"Dynamic programming result for {amount}:", find_min_coins(amount))

    start = perf_counter()
    find_coins_greedy(large_amount)
    greedy_time = perf_counter() - start

    start = perf_counter()
    find_min_coins(large_amount)
    dp_time = perf_counter() - start

    print(f"Greedy time for {large_amount}: {greedy_time:.8f} seconds")
    print(f"Dynamic programming time for {large_amount}: {dp_time:.8f} seconds")
