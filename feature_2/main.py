# bin(), oct(), hex()

line_num, target_val = map(lambda x: int(x), input().rstrip().split(' '))
binary_num_str = str(bin(target_val))[2::]
for i in range(line_num):
    x = int(input())
    print(binary_num_str[len(binary_num_str) - x])

import re
x = str(re.search("1.*1", '0b1000001000'))

result = re.sub(r'1','0b1000001000')
print(re.sub(r'1','0b1000001000'))
print(result)
re.findall(r'1.*1', '0b10000010001')