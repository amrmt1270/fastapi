from typing import Annotated

#引数で渡された整数値が指定された範囲内にあるかチェックする関
#引数：数値型(Annotated)
#戻り値:None

def process_value(
        value : Annotated[int, '範囲 : 0 <= value <= 100']
) -> None :
    if 0 <= value <= 100 :
        print(f"受け取った値は範囲内です: {value}")
    else :
        raise ValueError(f"範囲外の値です。受け取った値: {value}")
    

process_value(50)

try :
    process_value(150)
except ValueError as e :
    print(e)