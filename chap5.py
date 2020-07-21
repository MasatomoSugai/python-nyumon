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

# from random import randint
# a = randint(0,100)
# b = randint(0,100)
# if a>=40 and b>=40 and (a+b)>=120:
#     result = "合格"
# else:
#     result = "不合格"

# text = f"a{a}, b{b}, 合計{a+b}:{result}"
# print(text)


"""
Falseとみなされる値

False
None
数値の0, 0.0, 0j（複素数）
空の値：　"", (), [], {}
"""

# name = ""
# if not name:
#     name = "匿名"
# print(name)

# ２で割った余りが０かFalseになることを利用して奇数か偶数かを振り分ける
# from random import randint
# num = randint(0,100)
# 奇数か偶数かを判定する
# if num%2:
#     result = "奇数"
# else:
#     result = "偶数"
# print(num, result)


"""
条件式の簡略化
"""
# from random import randint
# a = randint(0,10)
# if 4<= a <=7:
#     print(a, "合格！！")
# else:
#     print(a, "不合格。。。")


"""
三項演算子 (bigger = a>b ? a : b)
pythonにはないので、if~elseを使って1行でかく
"""
# if a > b :
#     bigger = a
# else:
#     bigger = b

# これを1行でかくと
# bigger = a if a>b else b

"""
section5-2
while文
"""
# チケットの枚数だけループして、乱数を足し合わせた値を作る
# from random import randint
# tickets = 5
# point = 0
# fmt = "{:>5}" #3桁右づめ
# while tickets >0:
#     v = randint(1,20)
#     print(fmt.format(v))
#     point += v
#     tickets -= 1
# print("-" * 3)
# print(fmt.format(point))

# 無限ループから抜ける
from random import randint
count = 0
while True :
    a = randint(1,13)
    b = randint(1,13)
    c = randint(1,13)
    count += 1
    print(a,b,c)
    if (a+b+c) ==21:
        break
print(f"できたよ！値は{a},{b},{c}だったよ。{count}回もかかっちゃった")





