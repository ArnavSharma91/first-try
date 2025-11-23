def is_harshad(n):
    sum_digits = 0
    temp = n
    while temp > 0:
        digit = temp % 10           # Extract the last digit
        sum_digits += digit         # Add it to sum
        temp //= 10                 # Remove the last digit
    return n % sum_digits == 0      # Check if n is divisible by sum of its digits

print(is_harshad(18))   # True (because 1 + 8 = 9 and 18 % 9 == 0)
print(is_harshad(19))   # False 