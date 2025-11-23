def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

print(is_automorphic(5))
print(is_automorphic(7))
print(is_automorphic(9))