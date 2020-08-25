# ※ 表の作成には等幅のフォントを用います。すなわちこの表で使われる文字の文字幅はすべて等しくなります。
#
# ・表の 1 行目を見出し行、2 行目を区切り行、 3 行目以降をデータ行とよびます。
# ・表の各見出し・データを格納する部分は "| xxx |" のように縦棒 2 つの間に見出し・データが入り、見出し・データの前にちょうど 1 つ、後ろに 1 つ以上半角スペースが入る形にします。
# ・各列の幅はその列の中で最も長さの大きい見出し・データが上記の形で収まる最小の幅 (見出し・データの前後にちょうど 1 つずつ半角スペースが入れられる幅) にします。
# ・区切り行は縦棒を除きハイフンで埋めます。

# データの取得
# 各列ごとにリストを作成する
# 各列のリストの最大値に合わせて半角スペースを入れる
# 各リストごとに行をフォーマット通りに出力する

def data_fetch():
    list_num = int(input())
    table_items = input().rstrip().split(' ')
    item_num = int(input())
    items = input().rstrip().split(' ')

    return