# 4 buildings, each of which has 3 floors, each of which consists of 10 rooms
# given four integers b, f, r and v
# which represent that v persons entered to room r of fth floor at building b.
# If v is negative, it means that −v persons left.


order_number = int(1)
info = ['1 1 3 8', '1 1 3 -8', '3 2 2 7',
        '4 3 8 1']
move_infos = [list(map(int, i.split(' '))) for i in info]
for building_index in range(1, 5):
    for floor_index in range(1, 4):
        rooms_member = [0] * 10
        for (i, move_info) in enumerate(move_infos):
            if move_info[0] == building_index and move_info[1] == floor_index:
                calc = rooms_member[move_info[2] - 1] + move_info[3]
                rooms_member[move_info[2] - 1] = calc if calc > -1 else 0
                # move_infos.pop(i)
        print(''.join(map(lambda x: ' ' + str(x), rooms_member)))
    if building_index < 4:
        print('#' * 20)
        enumerate