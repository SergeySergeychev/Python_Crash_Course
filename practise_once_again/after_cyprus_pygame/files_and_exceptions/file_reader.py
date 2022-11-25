# with open(r'C:\Users\sserg\after_cyprus_pygame\files_and_exceptions\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# file_name = r'C:\Users\sserg\after_cyprus_pygame\files_and_exceptions\pi_digits.txt'
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string +=line.strip()
#
# print(pi_string)
# print(len(pi_string))
# print(lines)
#
# filename = r'C:\Users\sserg\after_cyprus_pygame\programming.txt'
# with open(filename, 'w', encoding = 'UTF=8') as file_object:
#     file_object.write(str(1))
# with open(filename, 'r', encoding = 'UTF=8') as file_object:
#     nums = file_object.readlines()
# for num in nums:
#     print(type(int(num.rstrip())))
# f = open('test.txt', 'r')
# print(f.mode)
# f.close()

#
# with open('test.txt', 'r') as f:
#     size_to_read = 10
#
#     contents = f.read(size_to_read)
#     print(f.tell())
    # while len(contents) > 0:
    #     print(contents, end='*')
    #     contents = f.read(size_to_read)
    # for line in f:
    #     print(line, end='')
    # contents = f.readline()
    # print(contents, end='')
    #
    # contents = f.readline()
    # print(contents, end='')

# for lines in contents:
#     print(lines)

# print(file.closed)
with open ('test.txt', 'r') as rf:
    with open ('test_copy.txt', 'w') as wf:
    f
