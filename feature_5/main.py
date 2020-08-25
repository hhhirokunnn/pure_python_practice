
def calc(target_int):
    result = [1, 2, 3]
    if target_int < 4:
        return result
    else:
        for i in range(4, target_int + 1):
            flg = True
            for ii in range(2, i):
                if i % ii == 0:
                    flg = False
            if flg:
                result.append(i)
    print(result)

name_list = ['aa', 'bb', 'ccc']
for name in name_list:
    print('Hello, {} san !'.format(name))

def calc_even_odd(number):
    result = '偶数' if number % 2 == 0 else '奇数'
    print('The number is {}'.format(result))

def add_array(a_1, a_2):
    if len(a_1) != len(a_2):
        print('error')
    else:
        result = [a_1[x] + a_2[x] for x in range(len(a_1))]
        print(result)

import re
def encode():
    # output '{0 or 1}{length},...,{0 or 1}{length}'
    with open('input.txt', 'r') as f:
        txt = f.read()
    splitted = filter(lambda x: x, re.split('(1+)|(0+)',txt))
    formatted = ['{}{}'.format(x[0],len(x)) for x in splitted]
    result = ','.join(formatted)
    with open('result.txt', 'w') as r:
        r.write(result)

def decode():
    with open('result.txt', 'r') as r:
        r_txt = r.read()
    raw_array = r_txt.split(',')
    result_array = [x[0] * int(x[1:]) for x in raw_array]
    result = ''.join(result_array)
    with open('input.txt', 'r') as f:
        txt = f.read()

    for (i,x) in enumerate(txt):
        if x != result[i]:
            print('{}: {}'.format(i,x))


test = '00000000000101111111'
splitted = filter(lambda x: x, re.split('(1+)|(0+)',test))
formatted = ['{}{}'.format(x[0],len(x)) for x in splitted]
','.join(formatted)