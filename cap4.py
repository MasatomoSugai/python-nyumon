# 関数

# print(abs(-3.5)) #絶対値
# print(min(5,6,-9,3,1,-4)) #min最小値、max最大値

#xの値を５〜⑩の値にする
# x = 5.1
# x = max(5, min(10, x))
# print(x)

# print(pow(2,3)) #2の３乗
# print(pow(2,3,5)) #2の３乗を４で割ったあまりを求める


# 文字列に使う関数
# chr(整数) 整数が示すUnicodeを文字列で返す
# ord(1文字) 文字に対するUnicodeを調べる

# print(ord("a"))
# print(chr(97))

# 入出力に使う関数
# input(文字列)　キーボードからの入力を受け取る
# open() テキストファイルを開く

# value = input("何か入れてください。：")
# print(value)


# モジュール
#モジュール名.関数()

# import math
# a = math.ceil(15.2) #切り上げ
# print(a)
# b = math.floor(15.3) #切り捨て
# print(b)

# print(math.pi) #円周率π 定数として定義してある
# print(math.degrees(math.pi/4))  #ラジアンを度に換算

# tan()を使って距離と角度から気の高さを求める
# import math
# kyori = 20
# kakudo = math.radians(32) #ラジアンに換算
# print(kakudo)
# takasa = kyori * math.tan(kakudo) #高さを計算
# print(takasa)
# takasa = math.floor(takasa * 100)/100 #小数点以下第2位で切り捨て
# print(str(takasa) + "m")


# 関数を指定して読み込む
# from モジュール名　import 関数名 as 別名
# この時、モジュールを指定せずに関数名だけで利用できる

# from random import randint as dice
# print(randint(1, 6)) #as~~と名前を付けたのでこれはエラーになる
# print(dice(1,6))

# 0.0~1.0の浮動小数点の乱数が欲しい場合
# from random import random
# print(random())

"""
オブジェクト・・・・データ（属性）とメソッド(関数)を持ったもの
オブジェクトが知っているメソッドの中から実行したいメソッドを命令する。
オブジェクトが知らないメソッドを命令されてもエラーになる（数値に文字列に使うメソッドを命令してもダメ）
「オブジェクト.メソッド()」・・・オブジェクトのメソッドを実行


"""

# s = "hello Python."
# print(type(s))#str型であると確認
# print(s.upper()) #半角英字を大文字に変換するメソッド
# print("good morning.".upper())

"""
文字列のメソッド
"""

# upper()  全て大文字に変換
# lower()  全て小文字に変換
# swapcase()  大文字と小文字を入れ替える
# capitalize()  1文字目だけを大文字に変換。2文字目以降は小文字にする
# title()  各単語の1文字目を大文字に、2文字目以降を小文字にする。it'sのようなアポストロフィがあるのは正規表現が必要

# s = "apple pie"
# print(s.count())#エラーになる
# print(s.count("p")) #文字列が含まれる個数を返す
# print(len(s)) #空白を含めた文字数を返す
# count(文字列,開始位置,終了位置)
# print(s.count("p",0,4))

# find(文字列,開始位置,終了位置)　文字が見つかった最初の位置を返す。見つからなかったときは-1を返す
# s = "apple pie"
# print(s.find("e"))
# print(s.find("x"))
# print(s.find("a",2))
# print(s.find("i",0,7))
# print(s.find("i",2,8))
# rfind()最後に見つかった位置を返す。後ろから検索して最初に見つかった位置
# print(s.rfind("e"))
"""
見つからなかったとき
find(),rfind() ==> -1
index(), rindex() ==> ValueError　を返す
"""

# 文字列を置換する replace(検索文字列,置換文字列,個数)
# s = "eeeee"
# print(s.replace("e", "x"))
# print(s.replace("e", "x",3)) #個数をマイナスにすると全部変わる？
# print(s.replace("e", "子供",2)) #==> 子供子供eee 置換前後で文字数が違ってもOK

"""
前後の余分な文字を取り除く
"""
# t = "  hello  world.,\n"
# print(t.strip()) #前後の空白を削除
# print(t.rstrip()) #末尾の空白を削除
# print (t.rstrip("ld.,\n")) #指定した文字を削除

"""
文字列に値を埋め込む
"""
# name = "高橋"
# age = 34
# point = 100.56
# s = "{}選手、年齢{}、得点{}でした！！！！"
# text = s.format(name, age, point) #変数でいれるパターン
# text = s.format("須貝", 28, 1000) #直接いれるパターン　数値を文字列に変換しなくても入る
# python3.6~　こちらが最新の書き方
# text = f"{name}選手、年齢{age}、得点{point/2}でした！"

#引数の順番を指定することもできる
# s = "得点{2}、{0}、{1}才   " #s.format(0, 1, 2)に対応している
# text = s.format(name, age, point)
# print(text)

# 埋め込む引数をキーワード引数で指定する
# s = "{name}選手、年齢{age}、得点{point}でした。"
# text = s.format(name="高橋", age=23, point=100)
# print(text)

"""
値の書式指定 {値:書式} 3桁位取り
"""

#３桁くらいとり
# tokyo = 1234000000 #==>1,234,000,000
# kyoto = 455530 #==> 455,530
# print(f"東京{tokyo:,}、京都{kyoto:,} ")

#format()を使うパターン
# s = "東京{:,}、京都{:,}"
# print(s.format(tokyo, kyoto))

# 値の型＝文字列s、整数d、浮動小数てんf

# length = 123.45
# thickness = 5.67
# text = f"長さ{length:.1f}cm、厚み{thickness:.0f}mm  "  #:.1f=小数点以下第一位まで。:.0f=小数点以下を表示しない。
# print(text)

#format()を使うパターン
# length = 1101.4445
# thickness = 4.67
# s = "長さ{:.1f}cm、厚み{:.0f}mm "
# s = "長さ{:,.1f}cm、厚み{:.0f}mm " #３桁の位取りも一緒にやりたいパターン{ :,.1f}=,が入る。
# print(s.format(length, thickness))

"""
値の位置揃え　左詰<、中央揃え^、右づめ>
"""
#10文字フィールドで右づめで表示
num1 = 123.4
num2 = 56.32
num3 = 111112.122
# print(f"{num1:>10.1f}") #右揃え
# print(f"{num2:>10.1f}")
# print(f"{num3:>10.1f}")
# print(f"{num1:<10.1f}") #左揃え
# print(f"{num2:<10.1f}")
# print(f"{num3:<10.1f}")
# print(f"{num1:^10.1f}")　#中央揃え
# print(f"{num2:^10.1f}")
# print(f"{num3:^10.1f}")




