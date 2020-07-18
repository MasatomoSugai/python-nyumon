# kosu = 12*5; all = kosu +20
# ;で命令文を区切ることができる
# print(all)

# \で改行できる
# ans = 1+2+3+\
# 4+5+6\
# +7+8+9+10*1000
# print(ans)

"""
複数業のコメントは
こんな感じでOK
"""

# a = 100
# b = 200
# c = 300
# abc = a+b+c
# print(a,b,c)
# print(a,b,c, sep="、", end = "/以上です") #sepで区切り文字の指定、endで行末文字の指定

# 浮動小数点
# 0の省略
# a = .99
# b = 10.
# print(a,b)
# 指数の表記 eは大文字でもOK e:Exponet
# a= 1.23e+7 #1.23 x 10の7乗
# b= 9.6e-4
# c= 1.23E+4
# print(a,b,c)

# 浮動小数の計算
# 浮動小数点と整数の計算結果は浮動小数点
# a = 10.3 + 0.5
# b = 120 *0.1
# print(a,b)
# 整数通しの割り算は割り切れても浮動小数点になる
# a= 124 / 4
# print(a)
# 小数点以下を丸めるにはround(数値, 桁)
# a = round(23.456, 1)
# b = round(23.456, 2)
# print(a,b)

# a = 0b0101 #２進数
# b = 0o011 #８進数
# c = 0xFF #１６進数
# d = bin(a + 0b010)#２進数でどう計算されているのかわかる
# print(a,b,c,d)

# 複素数 「実部 + 虚部」 虚部にはiまたはj pythonではjを使う
# a = 1j * 1j
# print(a)

# シングルクォート、タブルクォート
# print('私は"人工知能"です')
# print("私は'人工知能'です")

# エスケープシーケンス \n改行　\t水平タブ \rキャリッジリターン \" \' \\
# print("選んだ色は\n緑と\n黄色でした")

# 複数行の文字列
# poem = """ほととぎす
# なきつるかたをながむれば
# ただ有明の月ぞ残れる"""
# print(poem)

# 文字列演算子
# print("abc"*3) #==>abcabcabc

# 数値＋文字列
# tannka = 1000
# kosu = 3
# price = str(tannka * kosu)+ "円"
# print(price)

# 文字の繰り返しで棒グラフがわりにする
# symbol = "★"
# print("東京", symbol*10)
# print("新潟", symbol*6)

# 文字列からの取り出し
# id = "abcdefghijk"
# print(id[-3])
# print(id[:]) #全部
# print(id[2:5]) #3文字目から6文字目まで（6文字目は含まない）
# print(id[:4])#4文字目まで
# print(id[2:3+4]) #3文字目から8文字目まで
# # 飛び飛びで抜き出す
# print(id[::2]) #1文字おきに取り出す
# print(id[3::2]) #4文字目から1文字飛ばしで取り出す
# print(id[::-2]) #後ろから1文字飛ばし
# print(id[::-1]) #文字列を逆順にする


# 比較演算子
# a = 3; b =4; c=5
# print(a == b)
# print(a != b)
# print(a > b)
# print(a <=3)
# print(2 < c <10)

# 論理演算子
# print(True and False) #論理積 aかつbの両方がTrueの時True。一方でもFalseならFalse
# print(True or False) #論理和　aまたはbのどちらか一方でもTrueならTrue。両方FalseならFalse
# print(not True) #否定

# a = 50
# kekka = (a >=10) or (a <90)
# kekka = (a >=10) + (a <90) #True = 1, False = 0として扱われる

# print(kekka)
# print(1 and 1)
# print(1 or 0)
# print(1 or 1)
# #True, False,0,1以外の値が論理式で使われたときは、orで左項、andで右項
# print(2 or 3)
# print(2 and 3)

# ビット演算子
#論理積& AND 両ビット共に1の時１
# 論理和| OR どちらかのビットが１ならば１
# 排他的論理和^ XOR 比較したビット値が異なる時１
# ビット反転:- NOT ビットの１、０を反転させます

# 右しふと>>ビットを右にずらすので値は1/2 左シフト<<ビットを左にずらすので値は２倍
# a = 0b001011
# print(a) #==> 11
# print(a << 1) #==> 22
# print(bin(a << 1))
# print(a >> 1) #==>5

# ビットマスク　必要な部分を１にした値とANDすることで、数値から必要なビットを抜き出す
# a = 0b100110
# print(bin(a & 0b111)) #ビットマスクでしも３桁を取り出す
# print(bin((a>>1) & 0b11)) #先にみぎへ１桁シフトしてから取り出す

#型を変換する type()で調べることが可能
# 数字を文字列に変換して足す
# len = 10*12.3
# print(type(len))
# print("長さは" + str(len) + "cmです。")

# 理論値を文字列に変換
# print("5<10は" + str(5<10) + "です")

# print(int("240")*3) #文字列を整数に変換
# print(float("11.4") + 10) #浮動小数点を型変換
# print(int(12.88)) #浮動小数を整数かすると小数点以下切り捨て

# print(bin(10)) #２進数に変換
# print(oct(10)) #8進数に変換
# print(hex(10)) #16進数に変換

# 複合代入演算子
"""
a += b  a=a+b
a -= b  a=a-b
a *= b  a=a*b
a /= b  a=a/b
a //= b  a=a//b
a %= b  a=a%b
a **= b  a=a**b
"""