x, y = map(int, input().split())
profit = ((y - x) / x) * 100
print(f"{profit:.2f}")