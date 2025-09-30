# Learning dsa with python | python data structures and algorithms

# what is time complexity 
# -> the amount of time an algorithm takes to run as a function of the length of its input. 
# -> It's essentially a measure of how the algorithm's execution time grows as the input size increases. 


# Tc -> big 0n notation -> 0(n)

# ->  Alaways calute tme complecity in terms of worst case scenario 
# ->  Avoid the constant value
# ->  Avoide a lower bound 

# n = 12
# for i in range(1,n+1):
#     print("0")

 
# what is space complexity
# -> Space complexity refers to the amount of memory space an algorithm requires 
# -> to execute and solve a problem, as a function of the input size
    

n = 5 

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("0", end=" ")
        else:
            print("*", end=" ")
    print()
    
    
# The time complexity of the provided nested loop code is O(n²), which is read as "Big O of n squared".

# Here's why:

# Outer loop: The outer for loop iterates n times (from 1 to n inclusive).
# Inner loop: For each iteration of the outer loop, the inner for loop also iterates n times (from 1 to n inclusive).
# Operations inside the inner loop: Inside the inner loop, there's a conditional check (if i == j) and a print() statement. These operations take constant time, which we denote as O(1).
# Since the inner loop runs n times for each of the n iterations of the outer loop, the total number of times the operations inside the inner loop are executed is proportional to n×n=n 
# 2
#  .

# Therefore, the dominant factor determining the execution time of this code as the input size n grows is n 

# 2 .This makes its time complexity quadratic, or O(n²).

# In simpler terms, if you double the value of n, the execution time of this code will roughly quadruple.

# import numpy as np

# a = np.array([1, 2, 3, 5])
# i = 0

# for _ in range(100):
#     if i >= len(a): # time complixety jut for this is o(1)
#         break
    
#     if a[i] >= 5:
#      a = np.append(a,a[-1] + 1 )
     
    
#     if 50 in a:
#         break
#     i += 1

# print(a)    



# For example, for n = 5, the output should be:
# * * * * 0 
# * * * 0 * 
# * * 0 * * 
# * 0 * * * 
# 0 * * * * 
L =  5

for i in range(1, L + 1):
  for j in range(1 , L + 1):
    if i + j == L + 1:
      print(0, end = " ")
    else:
      print("*", end = " ")
  print()
  
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Added a script that iterates over a string and counts the frequency of each character.
# It then prints characters that appear more than once, showing how many times they appear.
# Useful for simple text analysis or debugging repeated characters.

s = "abcaadefrqrqeqrqasasaeafaff"
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    if count > 1:
        print(f"Character '{char}' appears {count} times.")
        
    