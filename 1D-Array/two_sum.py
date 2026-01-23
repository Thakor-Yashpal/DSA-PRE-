nums = [2,7,11,15]

target = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

result = two_sum(nums, target)
print(result)


# Find Target Indices After Sorting Array

nums = [2,7,11,15,12,3,4,6,8,9,21,14]

target = 9

def target_indices(self,nums, target):
    
        count_smaller = 0  # Initialize count for elements smaller than target
        count_same = 0     # Initialize count for elements equal to target
        for num in nums:
            if num == target:
                count_same += 1
            elif num < target:
                count_smaller += 1
        return list(range(count_smaller, count_smaller + count_same))

result = target_indices(0,nums, target)
print(result)




# Single Number

nums = [3,2,2,3]

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

result = single_number(nums)
print(result)



nums = [4,3,2,7,8,2,3,1]

def find_disappeared_numbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    return result



# this is the two sum 


Number = [2,7,11,15,12,3,4,6,8,9,21,14]