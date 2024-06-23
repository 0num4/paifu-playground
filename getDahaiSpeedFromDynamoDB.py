import decimal
import json

import boto3
from boto3.dynamodb.conditions import Key

import PaifuTypesPydanticWithInternal


def get_hand_event_record_data(table, key_value):
    response = table.query(KeyConditionExpression=Key("id").eq(key_value))

    if response["Items"]:
        item = response["Items"][0]
        hand_records = item.get("handRecord", [])

        for hand_record in hand_records:
            hand_event_records = hand_record.get("handEventRecord", [])

            for event_record in hand_event_records:
                event_data_str: str = event_record.get("data")
                if event_data_str is not None:
                    event_data = json.loads(event_data_str)
                    print(f"Json Event Data: {event_data}")
    else:
        print("No item found with the given key.")


# DynamoDBテーブルの設定
dynamodb = boto3.resource("dynamodb")
table_name = "paifu_playground"
table = dynamodb.Table(table_name)

# 取得したいアイテムのキー値
key_value = "cnsfcgu9nc7ajnvfo1l0"

# 関数の呼び出し
get_hand_event_record_data(table, key_value)
