# 6. Factorial of a number
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = 5
print("Factorial of", num, "is:", fact(num))


# 7. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = 5
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")


# 8. Sum of first n natural numbers
def sumOfN(n):
    return n * (n + 1) // 2
num = 10
print("Sum of first", num, "natural numbers is:", sumOfN(num))


# 9. Reverse a number
def revNum(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
num = 1234
print("Reverse of", num, "is:", revNum(num))


# 10. Count number of digits
def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
num = 98765
print("Number of digits in", num, "is:", count_digits(num))
