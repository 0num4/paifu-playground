import datetime
import json
import os
import random
import time

import boto3
import dotenv
import pydantic
import pytz
import requests

import PaifuTypesPydantic

dotenv.load_dotenv()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("paifu_playground")


paifu = "gameDataSample.json"
json_file = open(paifu, "r")
json_data = json.load(json_file)

paifu = PaifuTypesPydantic.Paifu.model_validate_json(json.dumps(json_data), strict=True)
paifu.code

response = table.put_item(
    Item={
        "code": paifu.code,
        "message": paifu.message,
        "id": paifu.data.keyValue,
        "period": paifu.data.period,
        "roomId": paifu.data.roomId,
        "nowTime": paifu.data.nowTime,
        "remark": paifu.data.remark,
        "fangFu": paifu.data.fangFu,
        "gamePlay": paifu.data.gamePlay,
        "initPoints": paifu.data.initPoints,
        "isCollect": paifu.data.isCollect,
        "isGangPay": paifu.data.isGangPay,
        "isGeMu": paifu.data.isGeMu,
        "isKaiLiZhi": paifu.data.isKaiLiZhi,
        "isLuck": paifu.data.isLuck,
        "isNotEffect": paifu.data.isNotEffect,
        "isNotShowHand": paifu.data.isNotShowHand,
        "isObserve": paifu.data.isObserve,
        "isShaoJi": paifu.data.isShaoJi,
        "isWithUser": paifu.data.isWithUser,
        "matchStage": paifu.data.matchStage,
        "matchType": paifu.data.matchType,
        "northOperateType": paifu.data.northOperateType,
        "playerCount": paifu.data.playerCount,
        "round": paifu.data.round,
        "stageNum": paifu.data.stageNum,
        "stageType": paifu.data.stageType,
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
