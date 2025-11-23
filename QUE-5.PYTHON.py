def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
print(prime_factors(60))   # Output: [2, 2, 3, 5]
print(prime_factors(84))   # Output: [2, 2, 3, 7]