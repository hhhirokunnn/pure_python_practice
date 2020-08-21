line_num = int(input())
target_str = input()
target_list = [input() for _ in range(line_num)]
results = list(filter(lambda x: target_str in x, target_list))

if not results:
    print('None')
else:
    for result in results:
        print(result)
