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
= Calculating with Functions =

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be integer division. For example, this should return 2, not 2.666666...:

'''

def zero(func_oper=None): return int(func_oper(0)) if func_oper else 0
def one(func_oper=None): return int(func_oper(1)) if func_oper else 1
def two(func_oper=None): return int(func_oper(2)) if func_oper else 2
def three(func_oper=None): return int(func_oper(3)) if func_oper else 3
def four(func_oper=None): return int(func_oper(4)) if func_oper else 4
def five(func_oper=None): return int(func_oper(5)) if func_oper else 5
def six(func_oper=None): return int(func_oper(6)) if func_oper else 6
def seven(func_oper=None): return int(func_oper(7)) if func_oper else 7
def eight(func_oper=None): return int(func_oper(8)) if func_oper else 8
def nine(func_oper=None): return int(func_oper(9)) if func_oper else 9

def plus(func_num): return lambda x: x + func_num
def minus(func_num): return lambda x: x - func_num
def times(func_num): return lambda x: x * func_num
def divided_by(func_num): return lambda x: x / func_num


#==========================================================================#

'''

= Roman to integer =

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:

Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

'''

def romanToInt(self, s: str) -> int:
    roman_nums = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), 
                 (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    result = 0
    for num, roman_num in roman_nums:
        while s.startswith(roman_num):
            result += num
            s = s[len(roman_num):]
    return result


#==========================================================================#



#==========================================================================#



#==========================================================================#



#==========================================================================#



#==========================================================================#
