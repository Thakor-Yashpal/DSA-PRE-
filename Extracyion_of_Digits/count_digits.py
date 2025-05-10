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
    print(last_numbers)