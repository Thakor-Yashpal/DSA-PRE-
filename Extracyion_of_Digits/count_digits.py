# Example 01
n = 5785
num = n

# Time Complexity: O(log n), where n is the input number
# - Each iteration removes one digit (via integer division by 10)
# - Number of digits in n is approximately log₁₀(n)

# Space Complexity: O(1)
# - Only a constant amount of extra space is used (no additional data structures)

while num > 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)
    

    
# Example 02
N1 = 55787
NUm01 = N1

# Time Complexity: O(log n)
# - Same logic: iterates once per digit of the number

# Space Complexity: O(1)
# - Only uses simple variables, no lists or other structures

while NUm01 > 0:
    last_numbers = NUm01 % 10
    NUm01 = NUm01 // 10
    print(f"{last_numbers} is the last number in the number")
    
 



# Example 03

N1 = 23481       # Initial number
count = 0        # Counter to track the number of digits
NUm02 = N1       # Copy of N1 to manipulate

# Loop to count digits and extract the last digit in each iteration
while NUm02 > 0:
    count += 1
    last_digit = NUm02 % 10     # Get the last digit
    NUm02 = NUm02 // 10         # Remove the last digit
    print("Count value:", count, "Last digit:", last_digit)

# -----------------------------------------
# Time Complexity: O(d)
# - 'd' is the number of digits in the number N1
# - Each iteration processes one digit

# Space Complexity: O(1)
# - Uses only a fixed number of variables regardless of input size
# -----------------------------------------