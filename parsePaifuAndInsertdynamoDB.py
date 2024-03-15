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
        "id": paifu.data.keyValue,
        "period": paifu.data.period,
        "roomId": paifu.data.roomId,
        "nowTime": paifu.data.nowTime,
    }
)
print(response)
