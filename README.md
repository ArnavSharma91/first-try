# first-try
1. factorial(n)

The factorial(n) function computes the factorial of a non-negative integer n, defined as the product of all positive integers up to n. It is commonly used in permutations, combinations, probability, and recursive mathematical definitions.

2. is_palindrome(n)

The is_palindrome(n) function checks whether a given number reads the same forward and backward. It converts the number to a string and compares it to its reverse, returning True for palindromic numbers like 121 or 1331.

3. mean_of_digits(n)

The mean_of_digits(n) function calculates the average value of the digits in a number. It extracts each digit, sums them, and divides by the total number of digits to compute the mean.

4. digital_root(n)

The digital_root(n) function repeatedly sums the digits of a number until a single-digit result is obtained. This concept is used in checksum calculations and modular arithmetic (especially mod 9).

5. is_abundant(n)

The is_abundant(n) function determines whether a number is abundant, meaning the sum of its proper divisors is greater than the number itself. Abundant numbers include 12, 18, and 20.

6. is_deficient(n)

The is_deficient(n) function checks whether the sum of a number’s proper divisors is less than the number. Many positive integers such as primes are deficient numbers.

7. is_harshad(n)

The is_harshad(n) function evaluates whether a number is divisible by the sum of its digits. Harshad numbers like 18 and 21 satisfy this property and are used in digital mathematics.

8. is_automorphic(n)

The is_automorphic(n) function determines if a number’s square ends in the number itself. For example, 5 → 25 and 76 → 5776 are automorphic numbers.
9. is_pronic(n)

The is_pronic(n) function checks if a number is the product of two consecutive integers, i.e.,
                            n=k(k+1)
10. prime_factors(n)

The prime_factors(n) function returns a list of prime numbers that multiply together to give n. It performs repeated division starting from the smallest primes.
11. count_distinct_prime_factors(n)

This function counts how many unique prime factors a number has. For example, 12 has distinct prime factors {2,3}, so the result is 2.
12. is_prime_power(n)

        
The is_prime_power(n) function checks if a number can be expressed as
                     n=p^k
    where p is prime and k ≥ 1. Examples include 8 = 2³ and 27 = 3³
13. is_mersenne_prime(p)

The is_mersenne_prime(p) function checks whether
                  2^p-1   
is a prime number, given that p itself is prime. Famous Mersenne primes start from p = 2, 3, 5, 7.    
14. twin_primes(limit)

The twin_primes(limit) function generates all pairs of twin primes up to a specified limit. Twin primes are pairs that differ by 2, such as (3, 5) and (11, 13).

15. count_divisors(n)

The count_divisors(n) function counts the total number of positive divisors of a number, including 1 and the number itself. This is useful in divisor-based classifications like perfect or highly composite numbers.

16. aliquot_sum(n)

The aliquot_sum(n) function computes the sum of all proper divisors of a number (divisors less than the number). It is a key part of determining perfect, deficient, and amicable numbers.
17. are_amicable(a, b)

The are_amicable(a, b) function checks whether two numbers are amicable pairs—i.e., the aliquot sum of a equals b, and the aliquot sum of b equals a. Example pair: (220, 284).

18. multiplicative_persistence(n)

This function computes how many steps are needed to repeatedly multiply a number’s digits until a single digit remains.
19. is_highly_composite(n)

The is_highly_composite(n) function checks if a number has more positive divisors than any smaller positive integer. Highly composite numbers include 1, 2, 4, 6, 12, etc.
20. mod_exp(base, exponent, modulus)
The mod_exp() function efficiently computes
                  (base^exponenet) mod modulus
using binary (fast) exponentiation. It is crucial in cryptography, number theory, and modular arithmetic operations.
21. mod_inverse(a, m)

The mod_inverse(a, m) function computes the modular multiplicative inverse of a under modulus m, which is a number x satisfying the congruence (a * x) ≡ 1 (mod m). This function is essential in modular arithmetic, cryptography, and applications like RSA, and typically uses the Extended Euclidean Algorithm.

22. crt(remainders, moduli)

The crt(remainders, moduli) function solves systems of simultaneous congruences using the Chinese Remainder Theorem. Given equations of the form x ≡ rᵢ (mod mᵢ), it computes the unique solution modulo the product of the moduli, assuming they are pairwise coprime.

23. is_quadratic_residue(a, p)

The is_quadratic_residue(a, p) function checks whether the congruence x² ≡ a (mod p) has a solution, meaning whether a is a quadratic residue modulo the prime number p. This often uses Euler’s Criterion or the Legendre Symbol.

24. order_mod(a, n)

The order_mod(a, n) function finds the smallest positive integer k such that aᵏ ≡ 1 (mod n). This multiplicative order is significant in group theory, primitive roots, and cryptography.

25. is_fibonacci_prime(n)

The is_fibonacci_prime(n) function checks if a number is both a Fibonacci number and a prime number. It first determines whether n belongs to the Fibonacci sequence, then applies primality testing.

26. lucas_sequence(n)

The lucas_sequence(n) function generates the first n numbers of the Lucas sequence, which is similar to the Fibonacci sequence but begins with values 2 and 1. Lucas numbers appear in combinatorics, primality tests, and number theory identities.

27. is_perfect_power(n)

The is_perfect_power(n) function determines if a number can be written in the form aᵇ where a > 0 and b > 1. Examples include 8 = 2³ and 81 = 3⁴. Perfect powers relate to exponential Diophantine equations and factorization.

28. collatz_length(n)

The collatz_length(n) function computes the number of steps required for a number n to reach 1 following the Collatz sequence rules. This famous unsolved problem uses the operations: even → n/2, odd → 3n + 1.

29. polygonal_number(s, n)

The polygonal_number(s, n) function returns the n-th s-gonal number, where s determines the shape: triangular (3), square (4), pentagonal (5), etc. Polygonal numbers appear in geometry and discrete math.
30. is_carmichael(n)

The is_carmichael(n) function checks whether a composite number n is a Carmichael number, meaning it satisfies aⁿ⁻¹ ≡ 1 (mod n) for all integers a that are coprime to n. These numbers are Fermat pseudoprimes to every base and are important in cryptography.
31. is_prime_miller_rabin(n, k)

The is_prime_miller_rabin(n, k) function performs the Miller–Rabin probabilistic primality test with k accuracy rounds. It efficiently determines whether a number is prime with very high reliability, used widely in cryptography.

32. pollard_rho(n)

The pollard_rho(n) function implements Pollard’s Rho Algorithm, a fast probabilistic method for integer factorization. It is especially effective for large composite numbers used in cryptographic systems.

33. zeta_approx(s, terms)

The zeta_approx(s, terms) function computes an approximation of the Riemann Zeta Function ζ(s) by summing the first terms of the infinite series. It is useful for numerical analysis, analytic number theory, and studying special values.

34. partition_function(n)

The partition_function(n) function calculates the number of distinct ways to express n as a sum of positive integers, disregarding order. This classical combinatorics function grows rapidly and is key in integer partitions, generating functions, and number theory.
