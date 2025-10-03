# Problem: Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:
#   Input: nums = [3,2,1]
#   Output: 1
#   Explanation:
#   The first distinct maximum is 3.
#   The second distinct maximum is 2.
#   The third distinct maximum is 1.

# Example 2:
#   Input: nums = [1,2]
#   Output: 2
#   Explanation:
#   The first distinct maximum is 2.
#   The second distinct maximum is 1.
#   The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
#   Input: nums = [2,2,3,1]
#   Output: 1
#   Explanation:
#   The first distinct maximum is 3.
#   The second distinct maximum is 2 (both 2's are counted together since they have the same value).
#   The third distinct maximum is 1.

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
#   + Input: an integer array nums
#   + Output: the third distinct maximum number in this array. P/s: distinct: khác biệt, if the third maximum does not exist, return the MAXIMUM number.
#
#- Design solutions
#   + Solution 1: Sort array and use for loop to find the third distinct maximum number
#     * Time complexity: sort is O(n log n), for loop is O(n) => total is O(n log n)
#
#   + Solution 2: Use 3 for loops to find the first, second, third maximum number
#     * Time complexity: first loop is O(n), second loop is O(n), third loop is O(n) but they are not nested (lồng nhau) => total is O(3n) = O(n) => better than O(n log n)
#
#   + Solution 3: use 3 variables to store the first, second, third maximum number
#     * Example: nums = [8,4,6,2,7,5]
#     * Suppose: the array has no negative numbers
#     * Initialize: first = second = third = -1 (we can use -1 because the array has no negative numbers)
#     * Loop through the array:
#       - i = 0 => nums[0] = 8 => first = 8, second = -1, third = -1
#       - i = 1 => nums[1] = 4 => first = 8, second = 4, third = -1
#       - i = 2 => nums[2] = 6 => first = 8, second = 6, third = 4 because 8 > 6 > 4 and 4 > third = -1
#       - i = 3 => nums[3] = 2 => first = 8, second = 6, third = 4
#       - i = 4 => nums[4] = 7 => first = 8, second = 7, third = 6 because 8 > 7 > 6 and 6 > third = 4
#       - i = 5 => nums[5] = 5 => first = 8, second = 7, third = 6
#     * After loop, we have first = 8, second = 7, third = 6 
#       => return third = 6
#     * Time complexity: O(n)
#
#=======================================================================================
#                                       Implement
#=======================================================================================

# Solution 1: Sort array and use for loop to find the third distinct maximum number
inputFile = "D:\\Projects\\leetcode\\(Leetcode_414)Third_Maximum_number\\input.txt"
outputFile = "D:\\Projects\\leetcode\\(Leetcode_414)Third_Maximum_number\\output.txt"

def run1(in_p: str, out_p: str):
    with open(in_p, "r", encoding = "utf-8") as fin, open(out_p, "w", encoding = "utf-8") as fout:
        for line in fin:
            line = line.split() #kiểu dữ liệu hiện tại là list
            array = [int(x) for x in line] #chuyển thành kiểu dữ liệu mảng
            print(thirdMax1(array))
            print()

def thirdMax1(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return array[0] if array[0] >= array[1] else array[1]
    array = sorted(array)
    print(array)
    change = 0
    thirdMax = array[len(array)-1]
    for i in reversed(array):
        if i < thirdMax:
            thirdMax = i
            change += 1
        if change == 2:
            return i
    return array[len(array)-1]

run1(inputFile, outputFile)

#Solution 2: Use 3 for loops to find the first, second, third maximum number
def run2(in_p: str, out_p: str):
    with open(in_p, "r", encoding = "utf-8") as fin, open(out_p, "w", encoding = "utf-8") as fout:
        for line in fin:
            line = line.split() #kiểu dữ liệu hiện tại là list
            array = [int(x) for x in line] #chuyển thành kiểu dữ liệu mảng
            print(thirdMax2(array))
            print()

def thirdMax2(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return array[0] if array[0] >= array[1] else array[1]
    run1(inputFile, outputFile)
    first = second = third = float('-inf')
    for x in array:
        if x > first:
            first = x
    for x in array:
        if x > second and x < first:
            second = x
    for x in array:
        if x > third and x < second:
            third = x
    return third if third > float('-inf') else first

run2(inputFile, outputFile)

