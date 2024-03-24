import boto3
import json
import os
import requests
import dotenv
import time
import random
import datetime
import pytz
import PaifuTypesPydantic
import pydantic
from decimal import Decimal

dotenv.load_dotenv()


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # または str(obj) によって文字列に変換
    raise TypeError


def get_item_size(table_name: str, key: str) -> int:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key={"id": key})
        if response.get("Item") is None:
            print("error!!おそらくレコードがありません")
            return None
        item = response["Item"]
        item_size = len(json.dumps(item, default=decimal_default))
        return item_size
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None


def get_table_size(table_name: str):
    # DynamoDBリソースの作成
    dynamodb = boto3.client("dynamodb")
    response = dynamodb.describe_table(TableName=table_name)
    table_size_bytes = response["Table"]["TableSizeBytes"]
    # サイズをキロバイト（KB）およびメガバイト（MB）に変換
    table_size_kb = table_size_bytes / 1024
    table_size_mb = table_size_kb / 1024

    return table_size_bytes, table_size_kb, table_size_mb


table_name = "paifu_playground"  # DynamoDBテーブル名
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)


paifu = "gameDataSample.json"
json_file = open(paifu, "r")
json_data = json.load(json_file)

paifu = PaifuTypesPydantic.Paifu.model_validate_json(json.dumps(json_data), strict=True)
print(paifu.data.keyValue)

item_size = get_item_size(table_name, paifu.data.keyValue)
table_size_bytes, table_size_kb, table_size_mb = get_table_size(table_name)


if item_size is not None:
    print(f"テーブルのサイズ: {table_size_mb:.2f} MB")
    print(f"レコードのサイズ: {item_size / 1024:.2f} kb")

response = table.delete_item(Key={"id": paifu.data.keyValue})
if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    if response.get("Attributes") is not None:
        print("アイテムを削除しました。")
    else:
        print("アイテムの削除に失敗しました。")
else:
    print("delete_itemのレスポンスが200以外です。")


# exit(0)

# 必要最低限のデータだけいれる
response = table.put_item(
    Item={
        # "code": paifu.code, errorのデータは別で入れる
        # "message": paifu.message,
        "id": paifu.data.keyValue,
        "period": paifu.data.period,
        "roomId": paifu.data.roomId,
        # "nowTime": paifu.data.nowTime,
        # "remark": paifu.data.remark, # 謎の値(ほぼ常に空白)。おそらくブックマークのコメント
        # "fangFu": paifu.data.fangFu, # 友人戦の翻数縛り
        "gamePlay": paifu.data.gamePlay,  # 1003とか
        # "initPoints": paifu.data.initPoints, # 初期点数 段位なら35000固定
        # "isCollect": paifu.data.isCollect, # ブックマーク済みかどうか。マジでいらん。
        # "isGangPay": paifu.data.isGangPay, # パオの設定(槍カンか？)、段位ではfalse、友人線でも設定できなくね？
        # "isGeMu": paifu.data.isGeMu, #　割れ目友人線
        # "isKaiLiZhi": paifu.data.isKaiLiZhi, # オープンリーチ
        # "isLuck": paifu.data.isLuck, # 祝儀。段位ではfalse
        # "isNotEffect": paifu.data.isNotEffect, # 効果音とかいれるかのオプション。友人戦のみっぽい
        # "isNotShowHand": paifu.data.isNotShowHand, # これも友人戦のみっぽい
        "isObserve": paifu.data.isObserve,
        # "isShaoJi": paifu.data.isShaoJi, # 焼き鳥、段位ではfalse
        # "isWithUser": paifu.data.isWithUser, # 匿名化どうか(ここの値にかかわらず牌譜にはニックネームが入ってる)
        # "matchStage": paifu.data.matchStage, # 大会のみ
        # "matchType": paifu.data.matchType, # 大会のみ
        # "northOperateType": paifu.data.northOperateType,  # EGameNorthTypeか？とりあえず段位は北抜きルール
        # "playerCount": paifu.data.playerCount,　# もう秋刀魚四麻で分けて固定なので
        # "round": paifu.data.round, # もう銀半とかで分けて固定なので
        # "stageNum": paifu.data.stageNum, # 段位なら0
        # "stageType": paifu.data.stageType,  # もう銀半とかで分けて固定なので
        "handRecord": [
            {
                "benChangNum": record.benChangNum,
                "changCi": record.changCi,
                "handCardEncode": record.handCardEncode,
                "handCardsSHA256": record.handCardsSHA256,
                "handID": record.handID,
                "handPos": record.handPos,
                "paiShan": record.paiShan,
                "quanFeng": record.quanFeng,
                "handEventRecord": [
                    {
                        "data": event.data,
                        "eventPos": event.eventPos,
                        "eventType": event.eventType,
                        "handId": event.handId,
                        "startTime": event.startTime,
                        "userId": event.userId,
                    }
                    for event in record.handEventRecord
                ],
                "players": [
                    {
                        "cardBackID": player.cardBackID,
                        "gameMusicId": player.gameMusicId,
                        "headTag": player.headTag,
                        "identity": player.identity,
                        "matchMusicId": player.matchMusicId,
                        "model": player.model,
                        "nickname": player.nickname,
                        "points": player.points,
                        "position": player.position,
                        "profileFrameId": player.profileFrameId,
                        "riichiEffectID": player.riichiEffectID,
                        "riichiMusicId": player.riichiMusicId,
                        "riichiStickID": player.riichiStickID,
                        "roleID": player.roleID,
                        "skinID": player.skinID,
                        "specialEffectID": player.specialEffectID,
                        "tableclothID": player.tableclothID,
                        "titleID": player.titleID,
                        "userId": player.userId,
                    }
                    for player in record.players
                ],
            }
            for record in paifu.data.handRecord
        ],
    }
)
print(response)


item_size = get_item_size(table_name, paifu.data.keyValue)
table_size_bytes, table_size_kb, table_size_mb = get_table_size(table_name)


if item_size is not None:
    print(f"テーブルのサイズ: {table_size_mb:.2f} MB")
    print(f"レコードのサイズ: {item_size / 1024:.2f} kb")
