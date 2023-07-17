#python3

# RSSを読み込んでMisskeyでnoteするBotアカウントクラスを定義する

# クラスがインスタンス作成時に受け取るもの
#   1.名前
#   2.URL（Misskeyのサーバドメイン。今のところ想定はmisskey.io）
#   3.アカウントのトークン文字列
#   4.Misskeyアカウントのプロフィール参照頻度(分)
#   5.RSSサイトへの参照頻度(分)
#   6.ノート投稿頻度(分)
#   7.sqlite3のDBファイルを記載

# クラス内で持っている変数
#   1.url_list(Misskeyから取得したURLのリスト)

# botのDBの仕様について
# 各BOT固有の投稿予定一覧と
# 
# table:Users
#   Usersの想定カラム
#   1.id（primary key）
#   2.username（名前）
#   3.domain（ユーザのドメイン）
#   4.modification_date(RSSの最終更新日付)
#   5.send_date(最後に投稿した更新日付)
#
# table:Sendurl
#   Sendurlの想定カラム
#   1.id（primary key）
#   2.userid(投稿したユーザーのUserテーブル上のprimary key)
#   3.url(RSSから取得しMisskeyに送ったURL)
#   4.send_date(送信日時)
#

# メソッド：
#   初期化
import requests
import json
import sqlite3

class misskeyBot:
  def __init__(self,name,domain,token,profileinterval,rssinterval,noteinterval,dbfile):

    #名前とMisskeyのサーバ名、トークン等を受け取る。
    self.name = name
    self.domein = domain
    self.token = token
    self.profileinterval = profileinterval
    self.rssinterval = rssinterval
    self.noteinterval = noteinterval
    self.dbfile = dbfile

    #各APIのエンドポイントとヘッダー指定はここに記載
    self.endpoint_Crearenote = "/notes/create"
    self.endpoint_GetProfilerss = "/i"
    self.headers = {'content-type': 'application/json'}

    # sqlite3への接続と登録を実施する。
    # 最初に指定のDBファイルが初回起動かを確認する

    self.con = sqlite3.connect(self.dbfile)
    self.cur = self.con.cursor()
    try:
      self.res = self.cur.execute("SELECT * from Users")
      #print(self.res.fetchone())
    except sqlite3.OperationalError:
      #print("テーブル無いよ")
      self.res = self.cur.execute("create table Users(id interger,name text,domain text,modification_date date,send_date date)")
      con.commit()
      
    try:
      self.res = self.cur.execute("SELECT * from Sendurl")
      #print(self.res.fetchone())
    except sqlite3.OperationalError:
      #print("テーブル無いよ")
      self.res = self.cur.execute("create table Sendurl(id interger,userid interger,url text,send_date date)")
      self.con.commit()

    #初回のURLチェックを行う

    #ユーザ登録
    self.res = self.cur.execute(("insert into Users(name,domain) Value(?,?)",(self.name,self.domein))


  def __del__(self):
    #インスタンス破棄の際にはsqlliteのconを閉じる
    self.con.close()

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
