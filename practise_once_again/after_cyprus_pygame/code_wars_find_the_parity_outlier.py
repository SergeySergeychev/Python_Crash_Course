"""
def find_outlier(nums):
    odd_num_quant = 0
    even_num_quant = 0
    for num in nums[0:3]:
        if num % 2 == 0:
            even_num_quant += 1
        elif num % 2 != 0:
            odd_num_quant += 1
    for num in nums:
        if even_num_quant > odd_num_quant and num % 2 != 0:
            return num
        elif even_num_quant < odd_num_quant and num % 2 == 0:
            return num


nums = [2, 8, 9, 10, 12, 14, -20]
print(find_outlier(nums))
"""
"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0] # return list_comprehension of odd num.
    evens = [x for x int if x%2==0] # return list_comprehension of even num.
    # return odd if quant. of odds is less then evens.
    # return even if quant. of evens is less then odds.
    return odds[0] if len(odds)<len(evens) else evense[0]
int = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(int))
"""
"""
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
integers = [2, 8, 9, 10, 12, 14, -20]
print(find_outlier(integers))
"""
"""
def find_outlier(nums):
    base_parity = sum(x%2 for x in nums[:3]) // 2
    for i in range(len(nums)):
        if nums[i] % 2 != base_parity:
            return nums[i]

integers = [12, 14, 16, 18, 9, 22, -20]
print(find_outlier(integers))
"""
"""
numbers_divisible_by_three = [3, 6, 9, 12, 15]
for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f'{num} divided by 3 is {int(quotient)}.')
"""

"""
for i in range(3, 16, 3):
    quotient = i / 3
    print(f'{i} divided by 3 is {int(quotient)}.')
"""

"""
# NOT PYTHONIC

captains = ['Janeway', 'Picard', 'Sisko']

for i in range(len(captains)):
    print(captains[i])
"""

"""
# range(stop) takes one argument.
for i in range(3):
    print(i)
# range(start, stop) takes two arguments.
for i in range(1, 8):
    print(i)
# range(start, stop, step)

for i in range(1, 8, 2):
    print(i)
"""
"""
# incrementing with range().

for i in range(3, 100 , 25):
    print(i)
"""

"""
# decrementing with range().

for i in range(10, -6, -2):
    print(i)
"""
"""
# Print in reverse order.
for i in reversed(range(5)):
    print(i)
"""
"""
# Access items in a range() by index.
print(range(3)[1])
print(range(3)[2])
(print(type(range(3)[0])))
print(range(6)[2:5])
"""
"""
print((lambda x: (x % 2 and 'odd' or 'even'))(2))
"""

# Ex. Preserve order of elements which is > 0 , 0 put at the end of the list.
# def  move_zeros(nums):
#     num_list = []
#     zero_list = []
#     for num in nums:
#         if num > 0 or num < 0:
#             num_list.append(num)
#         elif num == 0:
#             zero_list.append(num)
#     num_list.extend(zero_list)
#     return num_list
# nums = [1, 0, 1, 2, 0, 1, 3]
# print(move_zeros(nums))
#
# def move_zeros(nums):
#
#     for i in range(len(nums)):
#         if nums[i] > 0 or nums[i] < 0 :
#
#
#
#
#     return nums
# nums = [1, 0, 1, 2, 0, 1, 3]
#
# print(move_zeros(nums))
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     print(l)
#     # return l+[0]*(len(arr)-len(l))
# arr = [1, 0, 1, 2, 0, 1, 3]
# l = [i for i in arr if isinstance(i, bool) or i!=0]
# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)
array = [1, 0, 1, 2, 0, 1, 3]
print(list(sorted(array, key= lambda x: x==0)))


number = (lambda x: x*2)(12)
print(number)
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x%2!=0, list_1)))
print(list(map(lambda x: pow(x,3), list_1)))
