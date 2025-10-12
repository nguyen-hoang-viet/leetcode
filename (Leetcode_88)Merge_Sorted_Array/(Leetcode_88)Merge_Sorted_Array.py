#Problem: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#           Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#           The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
#           where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
#   Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#   Output: [1,2,2,3,5,6]
#   Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#   The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.\
#
# Example 2:
#   Input: nums1 = [1], m = 1, nums2 = [], n = 0
#   Output: [1]
#   Explanation: The arrays we are merging are [1] and [].
#   The result of the merge is [1].
#
# Example 3:
#   Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#   Output: [1]
#   Explanation: The arrays we are merging are [] and [1].
#   The result of the merge is [1].
#
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
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
#   + Input: nums1 and nums2 are non-decreasing integer arrays, m and n are length of nums1 and nums2. 
#           But the number of elements of nums1 is m + n because we will merge them into nums1
#   + Requipment: The final sorted array should not be returned by the function
#                   Be stored inside the array nums1
#                   The first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored
#   + Output: a single array sorted in non-decreasing order (nums1)
#
#- Define solution
#   + Solution 1: Copy elements of nums2 to nums1 after that use sorted function for nums1
#       * Time complexity: sort is O(nlogn)
#
#   + Solution 2: Create a new array with length is m + n
#                   Use 2 pointer i and j for nums1 and nums2 to get elements of them into new array with the rule
#                   the element that have the value smaller will go first
#       * Time complexity: O(m + n) -> that good
#       * Space: m + n -> that bad because it wastes storage resources
#
#   + Solution 3: Use 2 pointer i and j for nums1 and nums2.
#                   Pointer i start from 0 to m-1, j start from 0
#                   If nums1[i] > nums2[j] -> swap(nums1[i], nums2[j]) and i+=1
#       * Time complexity: O(m + n)
#
#   + Solution 4: The same with solution 3 but start from the end of nums1
#       * Time complexity: O(m + n)
#
#=======================================================================================
#                                       Implement
#=======================================================================================

# Solution 1: Copy elements of nums2 to nums1 after that use sorted function for nums1
#
# from typing import List
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         for i in range (m, m+n):
#             nums1[i] = nums2[i-m]
#         nums1 = sorted(nums1) # Tạo ra một mảng mới rồi gán ngược lại vào nums1 nên không tính là in-place

# Solution 2: Create a new array with length is m + n
#
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merge_arr = []
        i = j = 0
        while i < m or j < n:
            if nums1[i] <= nums2[j]:
                merge_arr.append(nums1[i])
                i+=1
            else:
                merge_arr.append(nums2[j])
                j+=1
            if i == m and j < n:
                while j < n:
                    merge_arr.append(nums2[j])
                    j+=1
            if i < m and j == n:
                while i < m:
                    merge_arr.append(nums1[i])
                    i+=1
        nums1 = merge_arr

# Solution 3: Use 2 pointer i and j for nums1 and nums2 and swap elements
#
# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i = j = 0
#
#         while j < n:
#             if i <= m + n - 2 and nums1[i] <= nums2[j]:
#                 j+=1
#             else:
#                 nums1[m+n-2] = nums1[i]
#                 nums1[i] = nums2[j]
#                 nums2[j] = nums1[m+n-2]
#                 i+=1

# Solution 4: The same with solution 3 but start from the end of nums1
#
# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i = m - 1
#         j = n - 1
#         k = m + n - 1
#         while(j >= 0):
#             if (i >= 0 and nums1[i] > nums2[j]):
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1

