nums = [5, 6, 2, 2, 1, 1, 2, 3, 4, 5, 7, 8, 3, 111, 5, 6, 7, 3, 4, 9, 100]
freq_map = dict()

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map[2])  # Output: 3 

# Time Complexity: O(n) where n is the length of nums.
# We iterate through the list once, and dictionary operations (insert/check) are O(1) on average.

# Space Complexity: O(k), where k is the number of unique elements in nums.
# In the worst case (all elements are unique), the dictionary stores all n elements.



from collections import Counter

nums = [5, 6, 2, 2, 1, 1, 2, 3, 4, 5, 7, 8, 3, 111, 5, 6, 7, 3, 4, 9, 100]
freq_map = Counter(nums)

print(freq_map[2])  # Output: 3

# Time Complexity: O(n), where n is the length of nums.
# Internally, Counter also goes through the list once.

# Space Complexity: O(k), where k is the number of unique elements.
# The Counter stores each unique number as a key with its count.


num = [5, 6, 2, 2, 1, 1, 2, 3, 4, 5, 7, 8, 3, 111, 5, 6, 7, 3, 4, 9, 100]

n = len(num)
has_map = dict()

for i in range(n):
    has_map[num[i]] = has_map.get(num[i], 0) + 1

# Print frequency of 2 and 4 separately
print("Frequency of 2:", has_map[2])
print("Frequency of 4:", has_map[4])

# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(k), where k is the number of unique elements.

for k in [2, 4]:
    print(f"Frequency of {k}:", has_map.get(k, 0))