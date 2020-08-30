N = 2

# def fib(n):
#     i = 0
#     j = 1
#     result = 1
#     for k in range(n+1):
#         result = i + j
#         i = j
#         j = result
#     return result
# print(fib(N))


def solution(S):
    if len(S) % 2 != 0:
        return 0

    flg = True
    while flg:
        flg = False
        if S.find('()') > -1:
            S = S.replace('()', '')
            flg = True
        if S.find('[]') > -1:
            S = S.replace('[]', '')
            flg = True
        if S.find('{}') > -1:
            S = S.replace('{}', '')
            flg = True
        if len(S) < 1:
            return 1
    return 0
print(solution(')(' * 100000000))