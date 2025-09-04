#パイプ演算子においては|はまたはを表す

def greet(name: str|None) -> None :
    if name is None :
        print('こんにちは、ゲストさん！')
    else :
        print(f"こんにちは！ {name} さん！")

greet()