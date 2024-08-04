import json
import os

import dotenv
import requests

dotenv.load_dotenv()

# リクエストヘッダーを設定
headers = {
    "Content-Type": "application/json",
    "Cookies": f'{{"channel":"default","deviceid":"{os.environ["deviceid"]}","lang":"en","sid":"{os.environ["sid"]}","version":"2.0.6.31622","platform":"linux"}}',
}

# リクエストボディを設定(.envから読み取る)
payload = {"passwd": os.environ["passwd"], "email": os.environ["email"]}

# リクエストを送信
response = requests.post("https://alicdn.mahjong-jp.net/users/emailLogin", json=payload, headers=headers)

# レスポンスを表示
print(response.text)
emailLoginRes = response.json()
if emailLoginRes["code"] == 0:
    print("Logged into Riichi city as " + emailLoginRes["data"]["user"]["nickname"])

    # return emailLoginRes
else:
    print("Failed to log into Riichi city")
    # return None

deviceid = os.environ["deviceid"]
SID = os.environ["sid"]
UID = emailLoginRes["data"]["user"]["id"]
version = "2.0.6.31622"
cookies = {
    "channel": "default",
    "lang": "en",
    "deviceid": deviceid,
    "sid": SID,
    "uid": UID,
    "region": "cn",
    "platform": "pc",
    "version": version,
}
headers = {
    "User-Agent": "UnityPlayer/2020.3.42f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "Content-Type": "application/json",
    "Cookies": json.dumps(cookies),
    "Accept": "application/json",
    "X-Unity-Version": "2020.3.42f1c1",
}
# payload = {"isObserve": True, "keyValue": "clec9ou9nc758r6i5gdg"}
# paifu id is tmp paifu id
# payload = {"isObserve": True, "keyValue": "cnpp08m9nc7ajnusdol0"}
# payload = {"isObserve": False, "keyValue": "cnrkj069nc7ajnvadk30"}
# payload = {"isObserve": False, "keyValue": "cnrlatu9nc7ajnvagcq0"}
# payload = {"isObserve": False, "keyValue": "cnvbk1uai0897qsgduc0"}
# payload = {"isObserve": False, "keyValue": "cnvefreai0897qshaii0"}  # 割れ目
# payload = {"isObserve": False, "keyValue": "cnveknuai0897qshc4m0"}  # 焼き鳥
# payload = {"isObserve": False, "keyValue": "cnves7mai0897qshei9g"}  # 祝儀
# payload = {"isObserve": False, "keyValue": "cnvf06eai0897qshfp10"}  # 三麻
# payload = {"isObserve": False, "keyValue": "cnvnmj6ai0897qsis3gg"}  # collectTest
payload = {"isObserve": False, "keyValue": "co22hduai0897qt1uocg"}  # collectTest

# readOnlineRoomRes = requests.post("https://alicdn.mahjong-jp.net/record/readOnlineRoom", json=payload, headers=headers)
# readOnlineRoomResJson = readOnlineRoomRes.json()
# print(readOnlineRoomResJson)
# if readOnlineRoomResJson["code"] == 0:
#     print("Successfully read online room")
#     readOnlineRoomResJson["data"]
# # format teest

# for item in readOnlineRoomResJson["data"]:
#     players = item["players"]
#     nicknames = [player["nickname"] for player in players]
#     print(f"対局中のプレイヤー: {', '.join(nicknames)}")


getRoomDataRes = requests.post("https://alicdn.mahjong-jp.net/record/getRoomData", json=payload, headers=headers)
getRoomDataResJson = getRoomDataRes.json()
print(getRoomDataResJson)
with open("4ma_gin_han_sample.json", "w") as f:
    json.dump(getRoomDataResJson, f)
    f.close()

# if getRoomDataResJson["code"] == 156:
#     # 対局終了してて観覧期限も切れている(牌譜データではなく行動リストなので)
#     print("online room end limit")
#     exit(1)
# elif getRoomDataResJson["code"] == 0:
#     getRoomDataResJson["data"][]
