#python3

# misskeyBot.pyを読み込んで動作させる
# cronや外部的要因で無限ループを実行させる。このスクリプト自体は1回で処理しきる
from misskeyBot import misskeyBot
import csv

# DB設計
# sqlite3で作る、
#
#

# Bot設定csv
BOTLIST = './botlist.csv'

# ログ
info_log = '.\log\info.log'
# エラーログ
error_log = '.\log\error.log'

#Bot格納配列
botArray = []

#クラス化と配列送りにする
with open(BOTLIST,'r',encoding="utf_8") as file:
  botreader = csv.reader(file)
  for line in botreader:
    #print(line)
    if line[0].startswith("#"):
      pass
    else:
      #配列に*を付けることによってclassの引数に展開して渡している
      bot = misskeyBot(*line)
      botArray.append(bot)


# misskeyからBOTへRSSのURLを取得する


  # 処理の前段階
    # 1.bot一覧のSQLを呼び出してそもそも存在するか確認、存在していない場合は新規
    # 存在している場合、profileintervalで経過しているかを確認
    # あこれbotのクラスに書く内容だ


# テスト送信（今だけ）
# print(type(botArray[0]))
# print(botArray[0].name)
# botArray[0].sendNote("test")