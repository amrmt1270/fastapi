from typing import Optional

#Userクラス
#ユーザーのIDと名前を属性として持つ

class User :
    def __init__(self, id:int, name : str):
        self.id = id
        self.name = name

user_list = [
    User(id = 1, name ='内藤'),
    User(id = 2, name = '辻'),
    User(id = 3, name = '鷹木')
]

def get_user(user_id : int) -> Optional[User]:
    for user in user_list :
        if user.id == user_id :
            return user
    return None

