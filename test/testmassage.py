#python3exi

# 自分のアカウントでBotに呟かせてみよう
# 
# import requests
#
#response = requests.post('http://www.example.com', data={'foo': 'bar'})
#print(response.status_code)    # HTTPのステータスコード取得
#print(response.text)    # レスポンスのHTMLを文字列で取得
# 
# 
#{
#  visibility: '',
#  visibleUserIds: [],
#  text: 'test',
#  cw: '',
#  localOnly: false,
#  noExtractMentions: false,
#  noExtractHashtags: false,
#  noExtractEmojis: false,
#  fileIds: [],
#  mediaIds: [],
#  replyId: '',
#  renoteId: '',
#  channelId: '',
#  poll: {},
#}

# memo、投稿パラメータの中で配列系のfileid,mediaidsは空配列で入れるとエラーになる
# 最低限のパラメーターで送ればよし
import requests
import json

#    obj = {"xxx" : "xxxx", 123 : 123} 
#    json_data = json.dumps(obj).encode("utf-8")

# misskey.ioのURL
URL = "https://misskey.io/api/notes/create"
#tokenはGithub上には置けないのて実行時にカレントディレクトリに配置しておく
file_data = open("token.txt", "r")
TOKEN = file_data.readline()

#テスト実行なので他の人に見せないようvisibilityを設定する
jsonNote = {
  "visibility" : 'specified',
  "visibleUserIds" : ["ElmaDS"],
  'i' : TOKEN,
  'text' : 'Hallo Misskey api'
}
headers = {'content-type': 'application/json'}
postdata = json.dumps(jsonNote)
response = requests.post(URL, data=postdata,headers=headers)

print(response.status_code)
print(response.content)
