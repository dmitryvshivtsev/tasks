# calculating with functions

# def zero(func_oper=None): return int(func_oper(0)) if func_oper else 0 
# def one(func_oper=None): return int(func_oper(1)) if func_oper else 1
# def two(func_oper=None): return int(func_oper(2)) if func_oper else 2
# def three(func_oper=None): return int(func_oper(3)) if func_oper else 3
# def four(func_oper=None): return int(func_oper(4)) if func_oper else 4
# def five(func_oper=None): return int(func_oper(5)) if func_oper else 5
# def six(func_oper=None): return int(func_oper(6)) if func_oper else 6
# def seven(func_oper=None): return int(func_oper(7)) if func_oper else 7
# def eight(func_oper=None): return int(func_oper(8)) if func_oper else 8
# def nine(func_oper=None): return int(func_oper(9)) if func_oper else 9

# def plus(func_num): return lambda x: x + func_num
# def minus(func_num): return lambda x: x - func_num
# def times(func_num): return lambda x: x * func_num
# def divided_by(func_num): return lambda x: x / func_num


# print(eight(divided_by(three())))

#==========================================================================#
# subarray sum

# def max_sequence(arr):
#     max_num, current = 0, 0
#     for num in arr:
#         current += num
#         if current < 0: current = 0
#         if max_num < current: max_num = current
#     return max_num


# print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))    

#==========================================================================#
# pete, the baker

# def cakes(recipe, available):
#     recipe_list = recipe.items()
#     avail_list = available.items()
#     res_list = []

#     for elem in recipe_list:
#         if elem[0] in available:
#             avail_price = available.get(elem[0])
#             res_list.append(avail_price // elem[1])
#         else:
#             return 0
#     return min(res_list)

#==========================================================================#

# def high(x):
#     alphabet = ' abcdefghijklmnopqrstuvwxyz'
#     words = x.split()
#     result = ''
#     word_sum = 0
#     for word in words:
#         tmp = 0
#         for letter in word:
#             tmp += alphabet.find(letter)
#         if tmp > word_sum:
#             word_sum = tmp
#             result = word

#     return result

# print(high('d bb'))

#==========================================================================#

# def find_uniq(arr):
#     for i, s in enumerate(arr):
#         print(s)
#         act_set = set(s.lower())
#         print(act_set)
#         prev_set = set(arr[i - 1].lower())
#         print(prev_set)
#         pre_prev_set = set(arr[i - 2].lower())
#         print(pre_prev_set)
#         if act_set != prev_set and act_set != pre_prev_set: return arr[i]

# print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))

#==========================================================================#

def transpose(matrix):
    row = len(matrix[0])
    col = len(matrix)
    res = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(matrix[j][i])
        res.append(row)
    return res


matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(transpose(matrix))