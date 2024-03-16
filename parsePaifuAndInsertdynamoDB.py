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
        "id": paifu["data"]["keyValue"],
        "period": paifu["data"]["period"],
        "roomId": paifu["data"]["roomId"],
        "nowTime": paifu["data"]["nowTime"],
        "remark": paifu["data"]["remark"],
        "fangFu": paifu["data"]["fangFu"],
        "gamePlay": paifu["data"]["gamePlay"],
        "handRecord": paifu["data"]["handRecord"],
        "initPoints": paifu["data"]["initPoints"],
        "isCollect": paifu["data"]["isCollect"],
        "isGangPay": paifu["data"]["isGangPay"],
        "isGeMu": paifu["data"]["isGeMu"],
        "isKaiLiZhi": paifu["data"]["isKaiLiZhi"],
        "isLuck": paifu["data"]["isLuck"],
        "isNotEffect": paifu["data"]["isNotEffect"],
        "isNotShowHand": paifu["data"]["isNotShowHand"],
        "isObserve": paifu["data"]["isObserve"],
        "isShaoJi": paifu["data"]["isShaoJi"],
        "isWithUser": paifu["data"]["isWithUser"],
        "matchStage": paifu["data"]["matchStage"],
        "matchType": paifu["data"]["matchType"],
        "northOperateType": paifu["data"]["northOperateType"],
        "playerCount": paifu["data"]["playerCount"],
        "round": paifu["data"]["round"],
        "stageNum": paifu["data"]["stageNum"],
        "stageType": paifu["data"]["stageType"],
        "code": paifu["code"],
        "message": paifu["message"],
    }
)
print(response)
