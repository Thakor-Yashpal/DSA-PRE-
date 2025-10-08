def make_change(traget_amount):
    denominations = [200, 100, 50, 20, 10, 5, 1]
    coin_count = 0
    values = []
    
    for coin in denominations:
        while traget_amount >= coin:
            traget_amount -= coin
            values.append(coin)
            coin_count += 1
    return coin_count,values


print(make_change(24))  # Expected output: [25, 10, 10, 1]
print(make_change(163))  # Expected output: [10, 10, 1, 1, 1]