# Example01

N = 14345           # Input number
num = N             # Copy of the number for manipulation
node = len(str(N))  # Count of digits
total = 0           # Variable to hold sum of digits raised to the power of node

# Loop to calculate the sum of each digit raised to the power of the number of digits
while node > 0:
    last_di = num % 10
    total = total + (last_di ** len(str(N)))  
    num = num // 10
    node -= 1

if total == N:
    print("This is an Armstrong Number")
else:
    print("This is not an Armstrong Number")

# -----------------------------------------
# Time Complexity: O(d)
# - 'd' is the number of digits in the number N
# - Each digit is processed once with a power operation (constant time)

# Space Complexity: O(1)
# - Only a fixed number of variables are used regardless of input size
# -----------------------------------------



# Example02

N1 = 45784           # Input number
num1 = N1             # Copy of the number for manipulation
node1 = len(str(N))  # Count of digits
total1 = 0           # Variable to hold sum of digits raised to the power of node


while node1 > 0:
    last_di1 = num1 %10
    total1 = total1 + (last_di1 ** len(str(N)))  
    num1 = num1 // 10
    node1 -= 1

if total1 == N1:
        print("This is an Armstrong Number")
else:
    print("This is not an Armstrong Number")
    
# Time Complexity: O(d)
# - 'd' is the number of digits in the number N
# - Each digit is processed once with a power operation (constant time)

# Space Complexity: O(1)
# - Only a fixed number of variables are used regardless of input size
# -----------------------------------------



N2 = 153
num2 = N2
node2 = len(str(N2))  # d = number of digits
total2 = 0

while node2 > 0:
    last_di2 = num2 % 10
    total2 += last_di2 ** len(str(N2))
    num2 = num2 // 10
    node2 -= 1

if total2 == N2:
    print("This is an Armstrong Number",total2)
else:
    print("This is not an Armstrong Number", node2)


# Time Complexity: O(d)
# - 'd' is the number of digits in the number N
# - Each digit is processed once with a power operation (constant time)

# Space Complexity: O(1)
# - Only a fixed number of variables are used regardless of input size
# -----------------------------------------
