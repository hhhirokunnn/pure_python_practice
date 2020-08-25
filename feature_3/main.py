# sum() / len()

tree_num, limit = map(lambda x: int(x), input().rstrip().split(' '))
tree_list = list(map(lambda x: int(x), input().rstrip().split(' ')))
target_num = int(input())
target_range_list = list(map(lambda x: x.rstrip().split(' '), [input() for _ in range(target_num)]))

for target_range in target_range_list:
    head = int(target_range[0]) - 1
    tail = int(target_range[1])
    head_tmp = tree_list[:head]
    target_tmp = tree_list[head:tail]
    tail_tmp = tree_list[tail:]
    while sum(target_tmp)/len(target_tmp) < limit:
        target_tmp = [x + 1 for x in target_tmp]
    tree_list = [*head_tmp, *target_tmp, *tail_tmp]
result = list(map(lambda x: str(x), [tree for tree in tree_list]))
print(' '.join(result))
