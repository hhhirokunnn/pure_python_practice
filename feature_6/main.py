
raw_rows = [['S', '1'], ['H', '2']]
# cards = []
# tmp_num = []
# tmp_mark = ''
# for [mark, number] in raw_rows:
#     if mark != tmp_mark and len(tmp_mark) > 0:
#         non_numbers = set(range(1, 14)) - set(tmp_num)
#         cards.append([tmp_mark, list(non_numbers)])
#         tmp_num = []
#     tmp_num.append(int(number))
#     tmp_mark = mark
# else:
#     non_numbers = set(range(1, 14)) - set(tmp_num)
#     cards.append([mark, list(non_numbers)])
# for card in cards:
#     for number in card[1]:
#         print(card[0] + ' ', str(number))

cards = {'S': [], 'H': [], 'C': [], 'D': []}
tmp_num = []
tmp_mark = ''
for [mark, number] in raw_rows:
    cards[mark].append(int(number))

all_numbers = set(range(1, 14))
for mark in cards:
    non_numbers = list(all_numbers - set(cards[mark]))
    non_numbers.sort()
    for number in non_numbers:
        print(mark, number)