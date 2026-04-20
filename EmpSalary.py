salary = float(input())
hra = float(input())
da = float(input())
pf = salary * 0.12
gross = salary + hra + da + pf
print(f"{pf:.2f}")
print(f"{gross:.2f}")