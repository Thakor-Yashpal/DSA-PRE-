
# Example01

n = 12345        # Original number
Num = n          # Copy of the number for manipulation
result = 0       # Variable to store the reversed number

# Loop to reverse the number
while Num > 0:
    Last_di = Num % 10                 # Extract the last digit
    result = (result * 10) + Last_di   # Append digit to the reversed number
    Num = Num // 10                    # Remove the last digit

# Check if the reversed number is equal to the original
if result == n:
    print(result)           # If equal, it's a palindrome
else:
    print("Not a palindrome")

# ----------------------------
# Time Complexity: O(d)
# - Where d is the number of digits in the number n
# - Each digit is processed once in the loop

# Space Complexity: O(1)
# - Only a fixed amount of memory is used (variables: n, Num, result, Last_di)
# - No additional memory that grows with input size



# Exampel02


N = 111111111111      # Original number
Num0 = N              # Copy of the number for manipulation
result0 = 0           # Variable to store the reversed number

# Loop to reverse the number
while Num0 > 0:
    Last_di0 = Num0 % 10                      # Extract the last digit
    result0 = (result0 * 10) + Last_di0       # Append digit to reversed number
    Num0 = Num0 // 10                         # Remove the last digit

# Check if the reversed number is equal to the original
if result0 == N:
    print(result0)                            # It's a palindrome
else:
    print("Not a palindrome")

# -----------------------------------------
# Time Complexity: O(d)
# - 'd' is the number of digits in the number N
# - The loop runs once per digit

# Space Complexity: O(1)
# - Uses a constant amount of extra memory (N, Num0, result0, Last_di0)
# - No memory usage increases with input size
# -----------------------------------------
    
    



# Exampel03 same time and sapce compliexity as the example two


S = 2222222

var = S

result1 = 0

while var > 0:
    Last_di1 = var % 10
    result1 = (result1 * 10) + Last_di1
    var = var // 10

if result1 == S:
    print(result1)
else:
    print("Not a palindrome")
    
    
# -----------------------------------------
# Time Complexity: O(d)
# - 'd' is the number of digits in the number N
# - The loop runs once per digit

# Space Complexity: O(1)
# - Uses a constant amount of extra memory (S, var, result1, Last_di1
# - No memory usage increases with input size
# -----------------------------------------    