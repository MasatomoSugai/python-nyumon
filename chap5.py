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
# from random import randint
# count = 0
# while True :
#     a = randint(1,13)
#     b = randint(1,13)
#     c = randint(1,13)
#     count += 1
#     print(a,b,c)
#     if (a+b+c) ==21:
#         break
# print(f"できたよ！値は{a},{b},{c}だったよ。{count}回もかかっちゃった")

# 3階間違えるか、qと入力されるまで出題を繰り返す
# f

"""
continue
"""
# 重複しない値が１０個入ったリストを作る
# from random import randint
# numbers = []
# while len(numbers)<10:
#     n = randint(0,100)
#     print("{}が出ました！".format(n))
#     if n in numbers :
#         continue  #すでに含まれている値は追加せずに処理をスキップして次の値にいく
#     numbers.append(n)
#     print(numbers)

# print("最終的にこれっす",numbers)

"""
while ~ else
"""
# from random import randint
# numbers = []
# while len(numbers)<10:
#     n = randint(-10,90)
#     if n<0:
#         print(f"{n}が出たので中断されました")
#         break
#     if n in numbers :
#         continue
#     numbers.append(n)
# else:
#     print(numbers)


"""
section5-3
for文　処理を繰り返す
"""

"""
n回繰り返すfor文.０から始まってn回繰り返す。最後の値はn-1
for i in range(n):
"""

# for i in range(10):
#     print(i)

#range(10)は,iが繰り返しを数えるカウンタのように見えますが、0~9のシーケンスから値を１つずつ取り出してiに代入しています。
#range(開始値,終了値,ステップ)
# for i in range(5,10):
#     print(i)

# forのネスティング
# for i in range(3):
#     print("i =", i)
#     for j in range(7,9):
#         print(" ", "j =",j)

# 4行３列の点の座標
# 垂直方向３、水平方向２の感覚で並ぶ4行３列の点の座標を求める
# for i in range(4):
#     print()  #各行の改行
#     for j in range(3):
#         x = j*2
#         y = i*3
#         print(f"({x}, {y})", end="") #end=""で改行なし？
# print()  #最後の改行

# 繰り返しを中断んして終了するbreak
# numlist = [3, 4.4, 6,"x",1,7]
# sum = 0
# for num in numlist:   #変数numとして、オブジェクトnumlistから値を取り出す
#     if not isinstance(num, (int, float)): #isinstanceで数値(int, float)の判定
#         print(num, "数値ではありません。")
#         break
#     sum += num
#     print(num, "/", sum)

# ネスティングのbreak
# for i in range(4):
#     for j in range(4):
#         if i<j:
#             print("." * j)
#             break
#         print(f"i={i}, j={j}")

#continueでスキップ
# numlist = [3, 4.4, 6,"x",1,7]
# sum = 0
# for num in numlist:   #変数numとして、オブジェクトnumlistから値を取り出す
#     if not isinstance(num, (int, float)): #isinstanceで数値(int, float)の判定
#         print(num, "数値ではありません。")
#         continue
#     sum += num
#     print(num, "/", sum)

# ネスティングの中でcontinueを使う
# for i in range(4):
#     for j in range(4):
#         if i<j:
#             print("con " * j)
#             continue
#         print(f"i={i}, j={j}")

"""
繰り返した後で実行するfor in ~ else
"""
# numlist = [3, 4.4, 6,99,1,7]
# sum = 0
# for num in numlist:   #変数numとして、オブジェクトnumlistから値を取り出す
#     if not isinstance(num, (int, float)): #isinstanceで数値(int, float)の判定
#         print(num, "数値ではない値が含まれていました。")
#         break
#     sum += num
# else:  #breakされなかったときに実行される
#     print(num, "/", sum)


"""
section5-4
try文　例外処理
"""
"""
try:
  例外が発生する可能性がある処理
except:
  例外を受けて実行する処理
finally:
  try文を抜ける前に実行する処理
"""

# while True :
#     num = input("何個ですか？(qで終了)")
#     if num == "q":
#         print("終了しました。")
#         break
#     try:
#         price = 12 * int(num) #numのままだと文字列なので、int()で整数に変換
#         print("金額：",price)
#     except :
#         print("エラーです。正しい数値を入れてください。")


# num = input("整数を入れてね")
# try:
#     value =120 / int(num)
#     print(value)
# except:
#     print("エラーになりました。")
# finally:
#     print("計算終わり。") #エラーが発生してもしなくても最後に実行される

"""
関数内で値をreturnする場合、そのtry文にfinallyブロックがあるなら、
finallyブロックで値をreturnする必要がある
"""

"""
NameError:初期化されていない変数を使った
ZeroDivisionError:ゼロの割り算を行った
ValueError:方を変換できなかった
IndexError:空のリストから値を取り出そうとした
FileNotFoundError:指定したファイルが見つからなかった

"""

# sum = 7600
# while True:
#     num = input("何人ですか？（qで終了）")
#     if num == "q":
#         print("終了しました。")
#         break
#     try:
#         price = round(sum / int(num))
#         if price <0:
#             continue
#         print("一人当たりの金額", price)
#     except ValueError:
#         print("数値を入れてください。")
#     except ZeroDivisionError:
#         print("0以外の数値を入力してください。")

"""
try:
  例外が発生する可能性がある処理
except 例外１:
  例外１に対応する例外処理
except 例外２：
  例外２に対応する例外処理
else:
  例外が発生しなかったときに実行する処理
finally:
  try文を抜ける前に必ず実行する処理
  
"""