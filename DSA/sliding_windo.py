"""
group 2 total = G1 total - chocl left + enter
G2 = 12 -2 + 1
11
"""
def best_chocolates(prices, window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total

    print(f"Window 1: {prices[0:window_size]} = {current_total}")

    for i in range(window_size, len(prices)):
        left_chocolates = prices[i - window_size]
        right_chocolates = prices[i]

        current_total = current_total - left_chocolates + right_chocolates

        window = prices[ i - window_size +1:i +1]
        print(f"Window: {window} = {current_total}")

        if current_total > best_total:
            best_total = current_total

    return best_total
prices = [2,4,6,1,7,3,5]
answer = best_chocolates(prices, 3)
print("best total", answer)