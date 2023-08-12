# discord.pyをインポート
import discord
from collections import defaultdict

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv

load_dotenv()

# 初期化
client = discord.Client(intents=discord.Intents.all())


# 引数が数値か判定する関数 (整数・浮動小数点数)
def is_number(s):
    try:
        float(s)  # float関数は整数と浮動小数点数の両方を扱うことができます
        return True
    except ValueError:
        return False


# Botが正常に起動した際のイベント設定
@client.event
async def on_ready():
    print("Startup Success!!!")


# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    # Botが出力したメッセージでない場合（この条件でBotのメッセージを弾く）
    if not message.author.bot:
        if message.content.startswith("!Total") or message.content.startswith("!total"):
            user_sums = defaultdict(float)  # defaultdictをfloatに変更
            async for old_message in message.channel.history(
                limit=1000
            ):  # 最新から1000件のメッセージを取得
                if is_number(old_message.content):
                    user_sums[old_message.author.display_name] += float(
                        old_message.content
                    )  # intをfloatに変更

            for user, total in user_sums.items():
                await message.channel.send(
                    f"{user} Total: {total:.2f}"
                )  # 各ユーザーの合計をメッセージとして送信 (小数点以下2桁まで表示)


# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv("TOKEN"))
