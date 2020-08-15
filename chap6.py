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
# colors = ["green","blue", "red", "green", "yellow","green"]
# print("削除前", colors)
# target = "green"
# while target in colors : #削除する値が含まれている間は繰り返し削除する
#     colors.remove(target)
# print("削除後", colors)

# delを使った削除 リストの位置を指定して削除することが可能
# data = ["a", "b", "c", "d"]
# del data[1]
# print(data)
# del data[0]
# print(data)
# del data  #リストそのものを削除
# print(data)

"""
文字列とリストの相互変換

文字列.split(セパレータ)・・・文字列をセパレータで分割してリストにする
"""
# 空白で区切られた単語をリストにする
# message = "may the force be with you"
# words = message.split()
# print(words)

# # カンマで区切られた単語をリストにする
# fruits = "apple,orange,banana,mango" 
# words = message.split(",")
# print(fruits)
# カンマと空白で区切られた単語をリストにする
# fruits = "apple, orange, banana, mango" 
# words = message.split(", ")
# print(fruits)
# カンマの前後の空白が１個とは限らない場合は事前に取り除いてから分割
# colors = "red,blue,  green, white , black"
# colors = colors.replace(" ", "") #空白を取り除く
# print(colors)
# color_list = colors.split(",")
# print(color_list)

"""
最大分割回数を指定する

"""

# 最愛分割回数を３にしてリストに分割する
# result = "12,13,43,56,778,43,54,55,66"
# result_list = result.split(",", 3)
# print(result_list)
# 先頭から3要素をスライスしてリストを作る
# top3 = result.split(",", 3)[:3]
# print(top3)

"""
リスト要素を連結して文字列を作る
セパレータ.join(リスト)
"""

# members = ["Tom", "jerry", "Spike"]
# name = " and ".join(members) #andの前後にスペースがあった方がいい
# print(name)


"""
section 6-2
リストの連結、スライス、複製、比較

"""

"""
リストを連結する
"""
# + や +=演算子を使うと簡単

# abc = ["a", "b", "c"]
# xyz = ["x", "y", "z"]
# abcxyz = abc + xyz
# print(abcxyz)

# colors = []
# colors += ["red"]
# colors += ["white"]
# print(colors)

# extend()で連結
# data = [1,3,2]
# newdata = [4,5,5]
# data.extend(newdata)
# print(data) #==> [1,3,2,4,5,5]

# append()で追加するとリストを１個の要素として追加
# data = [1,3,2]
# newdata = [4,5,5]
# data.append(newdata)
# print(data) #==>[1,3,2,[4,5,5]]

"""
リストをスライス

リスト[開始位置:終了位置]
"""

colors = ["blue", "red", "green", "yellow", "pink", "black", "white"]
print(colors[:]) #全部
print(colors[3:]) #3から最後まで