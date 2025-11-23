# Function to check if a number is Pronic
def is_pronic(number):
    for i in range(1, int(number**0.5) + 1):
        if i * (i + 1) == number:
            return True
    return False

# Range to check for Pronic numbers
start_range = 1
end_range = 20

# Display Pronic numbers in the specified range
pronic_numbers = [num for num in range(start_range, end_range + 1) if is_pronic(num)]

print(f"Pronic Numbers in the range {start_range} to {end_range}:\n{' '.join(map(str, pronic_numbers))}")
