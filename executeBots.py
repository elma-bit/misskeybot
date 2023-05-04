#python3

# misskeyBot.pyを読み込んで動作させる
# cronや外部的要因で無限ループを実行させる。このスクリプト自体は1回で処理しきる
from misskeyBot import misskeyBot
import csv

# Bot設定csv
BOTLIST = './botlist.csv'

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

# テスト送信（今だけ）
print(type(botArray[0]))
print(botArray[0].name)
botArray[0].sendNote("test")