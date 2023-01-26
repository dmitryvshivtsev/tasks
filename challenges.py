'''
= Maximum subarray sum =

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

'''

def max_sequence(arr):
    max_num, current = 0, 0
    for num in arr:
        current += num
        if current < 0: current = 0
        if max_num < current: max_num = current
    return max_num 

#==========================================================================#

'''
= Pete, the baker =

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

'''

def cakes(recipe, available):
    res_list = []
    for elem in recipe_list:
        if elem[0] in available:
            avail_price = available.get(elem[0])
            res_list.append(avail_price // elem[1])
        else:
            return 0
    return min(res_list)


#==========================================================================#

'''

Two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_sum = 0
        result = []
        for i, num in enumerate(nums):
            tmp_sum += num
            result.append(i)
            if tmp_sum == target:
                return result
            else:
                if tmp_sum > target:
                    tmp_sum -= result.pop(i - 1)
                    if tmp_sum == target:
                        return result