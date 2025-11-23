def is_abundant(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total > n

number = int(input("Enter a positive integer: "))
result = is_abundant(number)
print("The number is abundant:", result)
