# discord.pyをインポート
import discord

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv
load_dotenv()

# 初期化
client = discord.Client(intents=discord.Intents.all())

# Botが正常に起動した際のイベント設定
@client.event
async def on_ready():
    print('Startup Success!!!')

# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    # Botが出力したメッセージじゃ無い場合（この条件でBotのメッセージを弾く）
    if not message.author.bot:
        # 入力されたメッセージが数字の場合
        if message.content.isdecimal():
            await message.channel.send('数字だね')

    # 上記と同様に2個目の設定
    if message.content == 'さようなら':
        await message.channel.send('またあいましょう')

# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv('TOKEN'))