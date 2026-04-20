n = int(input())
if n % 2 != 0:
    print("weird")
elif 2 <= n <= 5:
    print("not weird")
elif 6 <= n <= 20:
    print("weird")
else:
    print("not weird")