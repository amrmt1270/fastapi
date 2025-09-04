from typing import Optional

#必須の引数と任意の引数を設定することができるときに用いることが多い

#ユーザー情報を持つプロフィール返却する関数
#引数：文字列型, 文字列型/Optional, 数値型/Optional
#戻り値 : 辞書型 

def get_profile(
        email : str,
        username :Optional[str] = None,
        age : Optional[int] = None,
    ) -> dict:
    profile = {'email' : email}
    if username :
        profile['username'] = username
    if age :
        profile["age"] = age
    return profile

user_profile = get_profile(email = 'amrmt1270@yahoo.co.jp')
print(user_profile)

complete_profile = get_profile(email = 'gentakojima@icloud.com', username = '元太', age = 7)
print(complete_profile)