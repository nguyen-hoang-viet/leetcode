# Problem: Write a function that reverses a string. The input string is given as an array of characters s.
#          You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#   Input: s = ["h","e","l","l","o"]
#   Output: ["o","l","l","e","h"]
#
# Example 2:
#   Input: s = ["H","a","n","n","a","h"]
#   Output: ["h","a","n","n","a","H"]
#
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

#- Understand the proble
#   + Input: an array of characters s
#   + Requipment: reverses a string, in-place with O(1) extra memory
#
#- Define solutions
#   + Solution 1: create a new array
#       * Time complexity: O(n)
#       * Space complexity O(n) -> not in-place with O(1) extra memory
#   + Solution 2: use 2 point "l" and "r", start from the begin and the end of array
#       * Time complexity: O(n)
#       * Space complexity: O(1) -> that good, because it not create anything new
#   + Solution 3: the same with solution 2 but combine with recursion (đệ quy) -> do this for practise about recursion
#       * Time complexity: O(n)
#       * Space complexity: O(n) -> because ...
#   + Solution 4: create a stack because stack is FILO -> do this for practise about stack