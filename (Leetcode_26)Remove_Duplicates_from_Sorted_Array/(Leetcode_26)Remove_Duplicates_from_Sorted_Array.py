#Problem: Given an integer array nums sorted in non-decreasing order, 
#   remove the duplicates in-place such that each unique element appears only once.
#   The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.

# Return k.

# Example 1:
#   Input: nums = [1,1,2]
#   Output: 2, nums = [1,2,_]
#   Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#   It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
#   Input: nums = [0,0,1,1,1,2,2,3,3,4]
#   Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
#   It does not matter what you leave beyond the returned k (hence they are underscores).

#---------------------------------------------------------------------------------------

# Define steps to solve the problem
# - Understand the problem
#   + Read the question carefully or ask the interviewer to understand the requirements
# - Design solutions
#   + Brainstorming: list different approaches for the interviewer
#   + Analyze time and space complexity of each solution
#   + Choose the best solution based on time and space complexity
# - Implement
#   + Implement the chosen solutions
# - Test => manually walk them
#   + Test with the implemented methods
# - Optimize
#   + Optimize the solution if necessary

#---------------------------------------------------------------------------------------

#- Understand the problem
#   + Input: a non-decreasing sorted nums array
#   + Requipment: remove the duplicates in-place (in-place được hiểu là làm trực tiếp trên mảng đó luôn không tạo ra mảng khác)
#   + Output: return the number of unique elements in nums (k) with k elements of nums after remove duplicates
#
#- Define solution
#   + Solution: use 2 pointer, one to find duplicates numbers and one to save the position of unique number
#       * I have 2 pointer i and j, i to save the position of unique number, j moves from the beginning to the end of the array.
#         If nums[J] > nums[j-1] then nums[i] = nums[j] and i+=1
#       * Time complexity: O(n) because just use for loop to do it
#
#=======================================================================================
#                                       Implement
#=======================================================================================

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1 #because nums[0] always unique
        for j in range(0, len(nums)):
            if nums[j] > nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i
