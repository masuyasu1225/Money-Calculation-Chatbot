# discord.pyをインポート
import discord

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv
load_dotenv()

# 初期化
client = discord.Client(intents=discord.Intents.all())

# 合計金額を保持するための変数を0で初期化
sum_money = 0

#引数が整数か判定する関数
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Botが正常に起動した際のイベント設定
@client.event
async def on_ready():
    print('Startup Success!!!')

# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    # Botが出力したメッセージじゃ無い場合（この条件でBotのメッセージを弾く）
    if not message.author.bot:
        # 入力されたメッセージが整数の場合
        if is_int(message.content):
            global sum_money  # この行でグローバル変数を使用することを明示的に宣言します。
            sum_money += int(message.content)
            await message.channel.send(sum_money)  # 'sum' ではなく 'sum_money' を使用します

# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv('TOKEN'))
