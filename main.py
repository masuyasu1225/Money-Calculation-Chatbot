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

# # Botがメッセージを読み込んだ際のイベント設定
# @client.event
# async def on_message(message):
#     # Botが出力したメッセージじゃ無い場合（この条件でBotのメッセージを弾く）
#     if not message.author.bot:
#         # 入力されたメッセージが整数の場合
#         if is_int(message.content):
#             global sum_money  # この行でグローバル変数を使用することを明示的に宣言します。
#             sum_money += int(message.content)
#             await message.channel.send(sum_money)  # 'sum' ではなく 'sum_money' を使用します

# #過去のメッセージから数字の合計を算出
# @client.event
# async def on_message(message):
#     if message.content.startswith('!history'):
#         async for old_message in message.channel.history(limit=1000):  # 最新から1000件のメッセージを取得
#             #print(old_message.author, old_message.content)  # メッセージの投稿者と内容を表示
#             if is_int(old_message.content):
#                 global sum_money
#                 sum_money += int(old_message.content)
#                 print(old_message.created_at, "user:", old_message.author, "message:", old_message.content, "sum:", sum_money)
#         print("Total:", sum_money)

# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    # Botが出力したメッセージじゃ無い場合（この条件でBotのメッセージを弾く）
    if not message.author.bot:
        if message.content.startswith('!history'):
            global sum_money  # この行でグローバル変数を使用することを明示的に宣言します。
            sum_money = 0  # コマンドごとに合計値をリセットします
            async for old_message in message.channel.history(limit=100):  # 最新から100件のメッセージを取得
                if old_message.author == message.author and is_int(old_message.content):
                    sum_money += int(old_message.content)
            await message.channel.send(f'{message.author.display_name} Total: {sum_money}')  # 合計をメッセージとして送信

# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv('TOKEN'))
