# Example 01

n = [2, 3, 5, 6, 8, 1, 3, 3, 9, 10, 10]
m = [10, 11, 23, 1, 1, 6, 8, 5, 1, 25]

# Brute-force approach: For each number in m, count its occurrences in n
for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(count)

# Time Complexity: O(n * m)
#   - Outer loop runs m times
#   - Inner loop runs n times for each m → Total: O(n * m)
#
# Space Complexity: O(1)
#   - No extra space used that grows with input size




# Example 02

n1 = [2, 3, 5, 6, 8, 1, 3, 3, 9, 10, 10]
m1 = [10, 11, 23, 1, 1, 6, 8, 5, 1, 25]

# Create a frequency list for numbers 1 through 10
has_list = [0] * 11  # Index 0 is unused; indices 1-10 track counts

# Count frequency of each number in n1
for x1 in n1:
    if 1 <= x1 <= 10:
        has_list[x1] += 1

# For each number in m1, print how many times it appeared in n1
for num in m1:
    if num < 1 or num > 10:
        print(0)
    else:
        print(has_list[num])

# Time Complexity: O(n + m) where n = len(n1), m = len(m1)
# Space Complexity: O(1), since has_list size is fixed (11 elements)


# Example 03

n2 = [2, 3, 5, 6, 8, 1, 3, 3, 9, 10, 10]
m2 = [10, 11, 23, 1, 1, 6, 8, 5, 1, 25]

has_list = dict()  # Dictionary to store frequency of numbers in n2

# Count frequencies
for i in range(len(n2)):
    has_list[n2[i]] = has_list.get(n2[i], 0) + 1

# Output frequencies for each number in m2
for x2 in m2:
    print(has_list.get(x2, 0))

# Time Complexity:
#   - Building the frequency dictionary: O(n), where n = len(n2)
#   - Querying for each m2 element: O(m), where m = len(m2)
#   → Total: O(n + m)

# Space Complexity:
#   - O(k), where k is the number of unique elements in n2 (for the dict)
