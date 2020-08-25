# bin(), oct(), hex()
ord_num = ord('a') -1

target_str = input().replace(" ", '')
target_num_list = [ord(target_str[i]) - ord_num for i in range(len(target_str))]
while(len(target_num_list) != 1):
    temp = []
    for (i, target_num) in enumerate(target_num_list):
        if(i == len(target_num_list) - 1):
            target_num_list = temp
        else:
            res = int(target_num) + target_num_list[i + 1]
            temp.append(res if res < 101 else res - 101)

print(target_num_list[0])

import string
string_list = [x for x in string.ascii_lowercase]
enumerate(string_list)
