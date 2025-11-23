def is_deficient(n):
   sum_div = 0
   for i in range(1, n):
     if n%i== 0:
        sum_div += i
     return sum_div < n
print(is_deficient(8))
print(is_deficient (12))

#Loop through all numbers less than n

#Check if i divides n evenly

#Add divisor to the sum

#Return True if sum of divisors is less than