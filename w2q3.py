def mean_of_digits(n):
    if n == 0:
        return 0.0
    n = abs(n)  
    sum_digits = 0
    count = 0
    while n > 0:
        digit = n % 10
        sum_digits += digit
        count += 1
        n = n // 10
    return sum_digits / count
