"""
chapter 6

リスト

複数の値を１個の値として扱えるようにまとめる機能
他で言う、配列
"""

# a = 10
# b = 20 
# c = 30
# abc = [a,b,c]      #リストの値が決まる
# print(abc)
# b = 5             #bの値を変更する
# print(abc)        #リスト内のbは変わらない

# リストの要素は型が混在してもOK
# mixture = [10,"test", "dog", True]

# リスト内で改行も可能
# data = [
#     3,55,6,  #コメント
#     44,66,7
# ]
# print(data)

# リストの繰り返し
# nums = [0 ]*10
# print(nums)

# data = [1,2,3]
# print(data*3)

# thelist = list(range(-10, 10))
# print(thelist)

# # 偶数のリスト
# evenlist = list(range(0, 10, 2))
# print(evenlist)

# # 奇数のリスト
# oddlist = list(range(1,30, 2))
# print(oddlist)

# # 5の倍数のリスト
# list_x5 = list(range(0, 50, 5))
# print(list_x5)


# 文字列をリストに分ける
# list_happy = list("happy")
# print(list_happy)

# 空のリストを作る
# newlist = list()

# リストに入っている値を変更する
# colors = ["blue", "red", "green", "yellow"]
# print(colors[2])
# colors[2] = "black" #これで置き換えられる
# print(colors[2])

# 多重リスト（多次元リスト）
# list = [[[  ],[  ]    ], [   ], [    ] ]

"""
インデックスエラーIndexErrorを回避する
"""
# リストの長さをlen()で調べてインデックスエラーにならないようにする

# pos = int(input("取り出す位置："))
# colors = ["blue", "red", "green", "yellow"]
# length = len(colors)
# if -length <= pos < length :
#     item = colors[pos]
#     print(item)
# else :
#     print("エラーになりました。")

# 上記コードを例外処理に組み込む（書き換え）
# pos = int(input("取り出す位置："))
# colors = ["blue", "red", "green", "yellow"]
# # 例外処理に組み込む
# try :
#     item = colors[pos]
#     print(item)
# except IndexError :
#     print("インデックスエラーですよ！！")
# except Exception as error :
#     print(error)

"""
リストに要素を追加挿入する

リストの末尾に要素を追加・・・append()
要素を挿入・・・　insert(挿入位置, 値)
"""

# data = [] #空のリストを作っておく
# data.append(10)
# data.append(20)
# print(data)
# data.insert(0,500) #500を挿入
# print(data)

"""
リストの要素を削除する

pop()・・・リストの末尾の要素を削除し、削除した値を返す関数。pop(抜き取る位置)　空のリストにやるとIndexErrorとなる。
LIFO(last In First Out) append()で値を追加→pop()で取り出し

remove()・・・削除したい特定の値がわかっている時に使用。削除したい値が複数ある場合には最初に見つけた値が削除される。
　　　　　　　　削除したい値がリストに含まれていないとエラーになるので、in演算子でチェックする
"""

# fruits = ["apple", "orange", "banana", "peach"]
# print(fruits)
# dessert = fruits.pop(0)
# print(dessert)
# print(fruits)

# リストがからの場合に対処する
# fruits = ["apple", "orange", "banana", "peach"]
# fruits = []

# if fruits : #リストが空の時はFalseとなる
#     dessert = fruits.pop()
#     print("デザートは" + dessert)
# print(fruits)

# 例外処理に組み込んだ場合
# fruits = ["apple", "orange", "banana", "peach"]
# fruits = []
# try : 
#     dessert = fruits.pop(1)
#     print("デザートは" + dessert)
#     print(fruits)
# except :
#     print("エラーになりました")

# リストに削除したい値が含まれていたならば削除する
# colors = ["blue", "red", "green", "yellow"]
# print("削除前", colors)
# target = "black"
# # 削除する値が含まれているならば削除する
# if target in colors :
#     colors.remove(target)
# print("削除後",colors)

# 削除したい値をリストから全て削除するパターン
colors = ["green","blue", "red", "green", "yellow","green"]
print("削除前", colors)
target = "green"
while target in colors : #削除する値が含まれている間は繰り返し削除する
    colors.remove(target)
print("削除後", colors)
