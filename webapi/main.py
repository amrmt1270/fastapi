import requests
import json

#APIを変数に格納
url = "https://zipcloud.ibsnet.co.jp/api/search"

#ユーザーからの郵便番号の入力を受け取る
zip = input("郵便番号を入力 =>")

#APIを送るパラメータを準備
#ユーザーが入力した郵便番号をパラメータへ設定
param = {'zipcode' : zip}

#requests.get()関数を利用して
#APIにHTTP GETリクエストを送り、レスポンスがres に格納される
res = requests.get(url, param)

#res.text に格納されているJSON形式のレスポンスデータを
#Python の辞書型データに変換
data = json.loads(res.text)

#変換したデータを出力
print(data)

#見やすくなるための区切り
print('*' * 50)

#レスポンスデータから必要な情報を抽出
if data['results'] is not None:
    #results リストの最初の要素から住所情報を取得
    address_info = data['results'][0]

    #郵便番号
    zipcode = address_info['zipcode']

    #住所を組み立て
    address = f"{address_info['address1']}{address_info['address2']}{address_info['address3']}"

    #整形して表示
    print(f"郵便番号: {zipcode}, 住所 : {address}")
else:
    print('住所情報が見つかりませんでした')