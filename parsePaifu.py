import PaifuTypesPydantic
import PaifuTypesPydanticWithInternal
import PaifuTypeInternalPydantic
import PaifuType
import json
import os
from typing import Any, Literal, Mapping, Type, TypedDict, get_type_hints, Union, Never
import pydantic
from pydantic import ValidationError
import boto3

dynamodb = boto3.resource("dynamodb")
hand_event_playground_table = dynamodb.Table("paifu_hands_event_playground2")


paifu = "cnrkj069nc7ajnvadk30.json"
json_file = open(paifu, "r")
json_data = json.load(json_file)

# paifu = PaifuTypesPydantic.Paifu.model_validate_json(json.dumps(json_data), strict=True)
# print(paifu)


paifuAdapter = pydantic.TypeAdapter(PaifuTypesPydantic.Paifu)
a = paifuAdapter.validate_python(json_data, strict=True)


def analyze_hand_record(hand_event_records: list[PaifuTypesPydanticWithInternal.HandEventRecord], hand_id: str, paifu_id: str, room_id: str):
    print(f"hand_id: {hand_id}")
    print(f"paifu_id: {paifu_id}")
    print(f"room_id: {room_id}")
    count = 0
    for hand_event_record in hand_event_records:
        print(f"hand_record type: {type(hand_event_record.data)}") #hand_record type: <class 'str'>
        hand_event_record_data_json = json.loads(hand_event_record.data)
        print(f"hand_event_record_data_json: {hand_event_record_data_json}")
        if hand_event_record_data_json == {}:
            print("hand_event_record_data_json is null")
            continue
        paifuInternalAdapter = pydantic.TypeAdapter(Union[
                    PaifuTypeInternalPydantic.HandInfo,  # hand_cards
                    PaifuTypeInternalPydantic.OperationInfo,  # in_card
                    PaifuTypeInternalPydantic.ActionInfo,  # action
                    PaifuTypeInternalPydantic.OutCardInfo,  # out_card
                    PaifuTypeInternalPydantic.GameResult,  # end_type
                    PaifuTypeInternalPydantic.GameInfo,  # user_data
                    PaifuTypeInternalPydantic.IsAutoGangInfo,  # user_id & is_auto_gang
                    PaifuTypeInternalPydantic.TingInfo,  # ting_info
                    #dict[Never, Never], # 他の型にもかかってしまうので関数で省く
        ])
        b = paifuInternalAdapter.validate_python(hand_event_record_data_json, strict=True)
        # print(b)
        metadata = {
            "hand_id": hand_id,
            "paifu_id": paifu_id,
            "room_id": room_id,
            "count_id": str(count)
        }
        res = hand_event_playground_table.put_item(
            Item={**b.model_dump(), **metadata}
        )
        if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("put_item success")
        else:
            print("put_item failed")
        print(f"count: {count}")
        count += 1
        # print(f"hand_event_record_data_json: {hand_event_record_data_json['hand_cards']}") # 当然keyerrorが起こることがある
        # print(f"hand_record: {hand_event_record.data}")


keyvalue = a.data.keyValue
room_id = a.data.roomId
for hand_record in a.data.handRecord:
    analyze_hand_record(hand_record.handEventRecord, hand_record.handID, keyvalue, room_id)