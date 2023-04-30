#python3

# プロフィール欄からfieldsを取得するテスト
import requests
import json

#    obj = {"xxx" : "xxxx", 123 : 123} 
#    json_data = json.dumps(obj).encode("utf-8")

# misskey.ioのURL
URL = "https://misskey.io/api/i"
#tokenはGithub上には置けないのて実行時にカレントディレクトリに配置しておく
file_data = open("token.txt", "r")
TOKEN = file_data.readline()

#tokenを忘れずに渡す
jsonNote = {
  'i' : TOKEN,
}
postdata = json.dumps(jsonNote)

headers = {'content-type': 'application/json'}
response = requests.post(URL, data=postdata,headers=headers)

print(response.status_code)
print(response.content)

#responseの中から

#レスポンスの中身をjsonにする
profile = json.loads(response.content)

print(profile["fields"])
#なんだこれ
print(type(profile["fields"]))

#dict型になるらしい
a = profile["fields"]
print(a[0]["name"])
print(a[0]["value"])

#これで各要素が取れるのでaをloopしたりすれば各値を取れるはず！