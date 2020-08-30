# #
# #
# # # raw = ['1 1 3 4 5',
# # # '2 2 2 4 5',
# # # '3 3 0 1 1',
# # # '2 3 4 4 6']
# # #
# # # rows = [list(map(int, i.split(' '))) for i in raw]
# # #
# # # new_rows = []
# # # for row in rows:
# # #     new_column = row + [sum(row)]
# # #     print(' '.join(map(str, new_column)))
# # #     new_rows.append(new_column)
# # #
# # # t_new_rows = [list(x) for x in zip(*new_rows)]
# # # result = []
# # # for row in t_new_rows:
# # #     print(sum(row))
# # #     result.append(sum(row))
# # # print(' '.join(map(str, result)))
# #
# # # A = [9,3,9,3,9,7,9]
# # # uniq_elements = set(A)
# # # for elem in uniq_elements:
# # #     count = A.count(elem)
# # #     if count % 2 != 0:
# # #         print(elem)
# # # else:
# # #     raise ValueError
# #
# #
# # # def solution(A):
# # #     res_calc = []
# # #     for (P, a) in enumerate(A):
# # #         if P < 1 or P > (len(A) - 1):
# # #             continue
# # #         head = sum([A[i] for i in range(P)])
# # #         tail = sum([A[i] for i in range(P, len(A))])
# # #         res_calc.append(abs(head - tail))
# # #     else:
# # #         return min(res_calc)
# # # print(solution([3,2,2,5, 100000000000]))
# # #
# # # def solution(X, A):
# # #     if len(set(A)) < X or not X in set(A):
# # #         return - 1
# # #     result = []
# # #     for (i, a) in enumerate(A):
# # #         result.append(a)
# # #         if len(set(result)) == X:
# # #             return i
# #
# # A = 11
# # B = 345
# # K = 17
# # def solution(A, B, K):
# #     # write your code in Python 3.6
# #     if A == B:
# #         return 1 if A % K == 0 else 0
# #
# #     first = A + A % K if A > K else A + K % A
# #     if first > B:
# #         return 0
# #
# #     last = B - B % K
# #
# #     return int((last - first) / K) + 1
# # print(solution(A, B, K))
# # s = [1,2,3]
# # s = 'abcds'
# # s = 'abcdsa'
# # s[]
# # '(((())))'
# def solution(A):
#     leader = 0
#     counter = 0
#     for a in set(A):
#         if counter < A.count(a):
#             print('aaaaaaaaaaaaa')
#             print(counter)
#             print(a)
#             print(A.count(a))
#             leader = a
#     result = 0
#     for i in range(len(A)):
#         head = A[:i+1]
#         tail = A[i+1:]
#         print(head)
#         print(tail)
#         if head.count(leader) > int(len(head) / 2):
#             if tail.count(leader) > int(len(tail) / 2):
#                 result += 1
#     else:
#         return result
# print(solution( [4, 4, 2, 5, 3, 4, 4, 4]))
# min
#

# def solution(A):
#     min_val = 100000
#     for i in range(len(A)):
#         if i + 1 == len(A):
#             break
#         diff = A[i] - sum(A[i + 1:])
#         if min_val > abs(diff):
#             min_val = abs(diff)
#
#     return min_val
# print(solution([1,1,3]))
# '{}'.replace('{}', '')
# def solution(N, M):
#     x = 0
#     while M >= N:
#         M = M - N
#     eatenindex = []
#     i = 0
#     while True:
#         # if i > 100:
#         #     break
#         # i += 1
#         calc = x + M
#
#         x = calc - N if calc > N else calc
#
#         if x in eatenindex:
#             break
#         eatenindex.append(x)
#         print(x, M)
#         print(eatenindex)
#     return len(eatenindex)
def solution(N, M):
    x = 0
    while x != 1:
        x = N
        y = M
        while y != 0:
            (x, y) = (y, x % y)
            print('aaaaaaaaaa')
            print(x,y)
        N = N / x
        M = M / x
        print(N,M)
    return N
print(solution(10, 4))