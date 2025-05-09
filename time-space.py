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
    

n = 5  # You can change the value of n to control the size of the pattern

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("0", end=" ")
        else:
            print("*", end=" ")
    print()