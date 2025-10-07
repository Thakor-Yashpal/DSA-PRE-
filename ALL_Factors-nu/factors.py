
# Example 01: Summing All Divisors of a Number
'''
Example 01: Summing All Divisors of a Number
------------------------------------------------------------
Description:
- This example calculates the **sum of all divisors** of a given number `num = 40`.
- It loops from 1 to `num`, checking if each number divides `num` evenly.
- If so, it adds the number to a cumulative sum and prints each divisor.

Time Complexity: 
- O(n), where n is the value of `num`, since we iterate through all numbers from 1 to `num`.

Space Complexity: 
- O(1), as we only use a single integer variable (`result`) for accumulation.

'''

num = 40
result = 0

for i in range(1, num + 1):
    if num % i == 0:
        result += i
        print(i)

print("Sum of divisors of", num, "is:", result)



num1 = 41 
result = 0

for i in range(1, num1 +1):
    if num % i ==0:
        result += i
        print(i)

# Example 02: Finding Divisors of a Number

num = 230 
result = []

for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)

"""
Example 02: Finding Divisors of a Number

This program finds all divisors of a given integer `num`.

Approach:
We iterate from 1 to `num`, checking if each number divides `num` without a remainder.
If it does, we append it to a list called `result`.

Time Complexity:
- O(n), where `n` is the value of `num`, because we check every number from 1 to `num`.

Space Complexity:
- O(k), where `k` is the number of divisors.
- In the worst case, this becomes O(n) if all numbers from 1 to `num` are divisors (rare).

Note:
While this approach works well for small inputs like 230, for large numbers, 
it can be optimized to O(√n) using a different technique.
"""



# Example 03: Optimized Divisor Collection (Partial Iteration)
num = 30 
result = []

for i in range(1,num //2):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)
'''
Example 03: Optimized Divisor Collection (Partial Iteration)
------------------------------------------------------------
- Collects all divisors of `num = 30`, but only loops up to `num // 2`.
- This works because no number greater than `num // 2` (except `num` itself) can divide `num`.
- The number itself is appended manually at the end.

- Time Complexity: O(n/2) ≈ O(n)
- Space Complexity: O(k), where k is the number of divisors

'''


# example -04 optimal solution
from math import sqrt
number = 25  # Input number
result = []  # List to store the divisors

# Loop from 1 to the integer square root of the number
for i in range(1, int(sqrt(number)) + 1):
    # Check if 'i' divides 'number'
    if number % i == 0:
        result.append(i)  # Add the divisor
        # Add the paired divisor if it's not the square root (to avoid duplication)
        if number // i != i:
            result.append(number // i)

# Sort the divisors in ascending order
result.sort()

# Output the final sorted list of divisors
print(result)

"""
Find all divisors of a given number using optimized iteration up to sqrt(n).

Time Complexity:
    - The loop runs up to √n → O(√n)
    - Appending is O(1) per operation
    - Sorting the result list of up to 2√n elements → O(√n log √n)
    - Overall: O(√n log n)

Space Complexity:
    - At most 2√n divisors are stored in the list → O(√n)
"""