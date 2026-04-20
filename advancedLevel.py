#whether a number is palindrome.
def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(121)


#largest among three numbers
def largest(a, b, c):
    if a > b and a > c:
        print("Largest:", a)
    elif b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)
largest(10, 25, 15)


#calculate simple interest (P, T, R).
def simple_interest(P, T, R):
    SI = (P * T * R) / 100
    print("Simple Interest:", SI)
simple_interest(1000, 2, 5)


#multiplication table of a number.
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
table(5)


#whether a number is Armstrong number
def armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10
    if temp == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")
armstrong(153)
