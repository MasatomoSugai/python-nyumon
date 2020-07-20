"""
条件分岐、繰り返し、例外処理

インデントは半角空白４つ（慣習的なもの？）
"""

# v = 3
# if v<0:
#     v=0
# v = v*2
# print(v)


# sum = 50 + 38
# limit = 100

# if sum >=limit:
#     result = "合格"
# else:
#     result = "不合格"
#     result += "／" + str(sum-limit)

# print(f"合計点は{sum}でした。")
# print("-" * 20)
# print(f"結果は{result}です。")

"""
３つ以上の選択肢がある場合　if- elif- else
"""
# randamoモジュールのrandint関数を読み込み
# from random import randint
# point = randint(0,100)
# print(f"点数は{point}でした。判定は・・・")
#判定
# if point >= 80:
#     result = "Aクラス"
# elif point >=60:
#     result = "B"
# elif point >=30:
#     result = "C"
# else:
#     result = "不適合"
# print(result)


"""
ifのネスト（ネスティング）
"""

# from random import randint
# size = randint(5, 20)
# weight = randint (20, 40)

# if size >=10:
#     if weight >=25:
#         result = "合格"
#     else:
#         result = "不合格"
# else:
#     result ="不合格"

# text = f"サイズ{size}、重量{weight}:{result}"
# print(text)

# 上記条件式をandでリファクタリングすると
# from random import randint
# size = randint(5,20)
# weight = randint(20,40)

# if (size>=10) and (weight>=25):
#     result = "合格"
# else:
#     result = "不合格"
# text = f"サイズ{size}、重量{weight}:{result}"
# print(text)

from random import randint
a = randint(0,100)
b = randint(0,100)
if a>=40 and b>=40 and (a+b)>=120:
    result = "合格"
else:
    result = "不合格"

text = f"a{a}, b{b}, 合計{a+b}:{result}"
print(text)