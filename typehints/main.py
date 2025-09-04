def greet(name:str) -> str :
    return f"Hello, {name}"

#整数型の「型ヒント」
#引数：整数型, 戻り値：文字列型
def add(num1:int, num2:int) -> str:
    #変数に「型ヒント」
    result :str = '足し算結果 ->'
    return result + str(num1 + num2)

#文字列型の「型ヒント」
def greet(name : str) -> str :
    return f"おはよう！{name}"

#浮動小数型「型ヒント」
#引数：浮動小数点型、戻り値：浮動小数点型
def divide(divide : float, divisor :float) -> float :
    return divide /divisor

#リスト型の「型ヒント」
#引数：リスト「文字列型」, 戻り値なし
def process_items(items : list[str]) -> None :
    for item in items :
        print(item)

#辞書の「型ヒント」
#引数：リスト「文字列型」、戻り値：辞書「文字列型、整数型」
def count_character(word_list : list[str]) -> dict[str, int]:
    ans : dict[str, int] = {}
    for word in word_list :
        ans[word] = len(word)
    return ans

result_add = add(10, 20)
print(result_add)

greeting = greet('Taro')
print(greeting)

result_divided = divide(10.0, 2.0)
print('割り算の結果 ->', result_divided)

process_items(['リンゴ', 'ゴリラ', 'ラッパ'])

character_counts = count_character(['apple', 'amazon', 'google'])
print('文字列に対する文字数は ->', character_counts)