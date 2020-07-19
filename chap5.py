"""
条件分岐、繰り返し、例外処理

インデントは半角空白４つ（慣習的なもの？）
"""

# v = 3
# if v<0:
#     v=0
# v = v*2
# print(v)


sum = 50 + 38
limit = 100

if sum >=limit:
    result = "合格"
else:
    result = "不合格"
    result += "／" + str(sum-limit)

print(f"合計点は{sum}でした。")
print("-" * 20)
print(f"結果は{result}です。")