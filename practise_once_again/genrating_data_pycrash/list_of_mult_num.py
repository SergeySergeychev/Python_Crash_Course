from random import choice
s = set()

for i in range(1, 7):
    for j in range(1, 7):
        s.add(i*j)

list_of_num = list(s)
list_of_num.sort()

s =sorted(list(set((i*j) for i in range(1, 7) for j in range(1, 7))))
# print(s)
x_nums = [1, 2, 3, 4, 5, 6]
y_nums = [1, 2, 3, 4, 5, 6]
nums = [(x, y) for x in x_nums for y in y_nums]
print(nums)
