#python3

# RSSを読み込んでMisskeyでnoteするBotアカウントクラスを定義する

# クラスが受け取るもの
#   1.名前
#   2.URL（Misskeyのサーバドメイン。今のところ想定はmisskey.io）
#   3.アカウントのトークン文字列
#   4.Misskeyアカウントのプロフィール参照頻度(分)
#   5.RSSサイトへの参照頻度(分)
#   6.ノート投稿頻度(分)

# メソッド：
#   初期化
import requests
import json

class misskeyBot:
  def __init__(self,name,domain,token,profileinterval,rssinterval,noteinterval):

    #名前とMisskeyのサーバ名、トークン等を受け取る。
    self.name = name
    self.domein = domain
    self.token = token
    self.profileinterval = profileinterval
    self.rssinterval = rssinterval
    self.noteinterval = noteinterval

    #各APIのエンドポイントとヘッダー指定はここに記載
    self.endpoint_Crearenote = "/notes/create"
    self.endpoint_GetProfilerss = "/i"
    self.headers = {'content-type': 'application/json'}

  def sendNote(self,text):
    #   ノート送信

    # postするURL作成
    URL = "https://" + self.domein + "/api/" + self.endpoint_Crearenote
    # postするjson作成
    # vusibility関連は最終的に消す
    jsonNote = {
      "visibility" : 'specified',
      "visibleUserIds" : [self.name],
      'i' : self.token,
      'text' : text
    }
    postdata = json.dumps(jsonNote)
    response = requests.post(URL, data=postdata,headers=self.headers)

    print(response.status_code)
    print(response.content)

  def setRSSlinks():
    #ユーザのプロフィールを参照しURLを取得
    #Misskeyのプロフィール取得可能か確認
    pass

  def checkIntervalprofile():
  # スパム行為にならないよう、プロフィールの参照頻度を指定した時間でコントロールする
  # アカウント存在確認DBに自分の名前で問い合わせて最終確認頻度をコントロールする
    pass

  #   アカウントの存在確認
  def checkMisskeyAccount():
  # Misskeyへ接続できないのであればFalseを返す
    pass
