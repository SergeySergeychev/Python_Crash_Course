"""
def solution(number):
    sum = 0
    for i in range(number):
        if(i % 3) == 0 or (i % 5) == 0:
            sum +=i
    return sum

print(solution(10))


def solution(number):
    return sum(i for i in range(number) if (i % 3) == 0 or (i % 5) == 0)
print(solution(10))


def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result
"""
