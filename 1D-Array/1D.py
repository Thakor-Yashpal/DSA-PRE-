class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1
        return ''.join(result)

sol = Solution()
print(sol.mergeAlternately("abc", "pqr")) 



# redoing the code

class another_soluction(object):
    def one_more (slef,word01,word02):
        result = []
        i,j = 0,0
        
        for i in range((len(word01) + len(word02))):
            if i <len(word01):
                result.append(word01[i])
            if j < len(word02):
                result.append(word02[j])
                j += 1
        return ''.join(result)

sol = another_soluction()
print(sol.one_more("abc", "pqr"))



# buble sort

# we have a number of arrays and we want to sort them in ascending order
arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr [j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)



# linear search of  an element in an array

def linear_search(list0, target):
    for i in range(len(list0)):
        if list0[i] == target:
            return i
    return -1  # Target not found

list0 = [10, 23, 45, 70, 11, 15]
target = 70

if linear_search(list0, target) != -1:
    print("Element found at index:", linear_search(list0, target))
else:
    print("Element not found in the list.")
    
    
    

# binary search of an element in an array

def binary_search(binary_list, target):
    left, right = 0, len(binary_list) - 1
    
    while left <= right:
        mid =  left + (right - left) // 2
        
        if binary_list[mid] == target:
            return mid
        elif binary_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3

if binary_search(binary_list, target) != -1:
    print("Binary Element found at index:", binary_search(binary_list, target))
else:
    print("Binary Element not found in the list.")
    

# Check if age allows entry to the club

# def can_enter_club(age):
#     if age >= 18:
#         return "You can enter the club."
#     else:
#         return "You cannot enter the club."

# age = int(input("Enter your age: "))
# print(can_enter_club(age))



# so how can wr print the * this pattern

def pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end = "")
        print() 
n = 5
pattern(n)



#

# but wht is you wan t create like this like pyramid

def pyrmid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end = "")
        for k in range(i + 1):
            print("*", end = "")
        
        print()
n = 5
pyrmid(n)




