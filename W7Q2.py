import time
import tracemalloc

def polygonal_number(s, n):
    return ((s - 2) * n * n - (s - 4) * n) // 2
s = int(input("Enter s (number of sides): "))
n = int(input("Enter n (term number): "))
tracemalloc.start()
start = time.time()
result = polygonal_number(s, n)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
exec_time = time.time() - start

print(f"\n{n}-th {s}-gonal number = {result}")
print(f"Execution Time: {exec_time:.6f} seconds")
print(f"Memory Used: {peak/1024:.2f} KB")

# Write a function Collatz Sequence Length collatz_length(n) that returns the number of steps for n to reach 1 in the Collatz conjecture.
import time
import sys
import math
def collatz_length(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return steps
if __name__ == "__main__":
    TEST_NUMBER = 27
    print(f"--- Running Collatz Sequence Length for N = {TEST_NUMBER} ---")  
    start_time = time.perf_counter()  
    try:
        collatz_result = collatz_length(TEST_NUMBER)
    except ValueError as e:
        collatz_result = f"Error: {e}"    
    end_time = time.perf_counter()
    if isinstance(collatz_result, int):
        print(f"\n1. Number of Steps (Collatz Length): {collatz_result}")
    else:
        print(f"\n1. Number of Steps: N/A ({collatz_result})")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"2. Time Taken (Execution Time): {elapsed_time_ms:.6f} milliseconds")
    input_memory = sys.getsizeof(TEST_NUMBER)
    output_memory = sys.getsizeof(collatz_result) 
    print(f"\n3. Memory Used (Bytes):")
    print(f"   - Input Number ({TEST_NUMBER}): {input_memory} bytes")
    print(f"   - Resulting Steps ({collatz_result}): {output_memory} bytes")
