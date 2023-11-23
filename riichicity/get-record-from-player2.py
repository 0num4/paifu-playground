# こっちが本当に牌譜を取得するやつ
import requests
import json
import dotenv
import os
import time

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
payload = {"isObserve": False, "keyValue": "ccetv969nc7di8ola31g"}

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


# getRoomDataRes = requests.post("https://alicdn.mahjong-jp.net/record/getRoomData", json=payload, headers=headers)
# getRoomDataResJson = getRoomDataRes.json()
# print(getRoomDataResJson)
# with open("gameDataSample.json", "w") as f:
#     json.dump(getRoomDataResJson, f)
#     f.close()

# if getRoomDataResJson["code"] == 156:
#     # 対局終了してて観覧期限も切れている(牌譜データではなく行動リストなので)
#     print("online room end limit")
#     exit(1)
# elif getRoomDataResJson["code"] == 0:
#     getRoomDataResJson["data"][]

headers = {
    "User-Agent": "UnityPlayer/2020.3.42f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "Content-Type": "application/json",
    "Cookies": json.dumps(cookies),
    "Accept": "application/json",
    "X-Unity-Version": "2020.3.42f1c1",
}

# リクエストボディを設定(.envから読み取る)
payload = {
    "friendId": 813942315,
    # "endTime": 0,
    # "gamePlay": 0,  # 普通true or falseでは
    # "limit": 20,
    # "skip": 0,
    # "startTime": 0,
}

startTime = 0
# 100回ループ
for i in range(100):
    payload = {
        "friendID": 813942315,
        # "endTime": endTime,
        # "gamePlay": 0,  # 普通true or falseでは
        # "limit": 0,
        # "skip": 100,
        "startTime": startTime,
    }
    readPaiPuListRes = requests.post(
        "https://alicdn.mahjong-jp.net/record/readPaiPuList", json=payload, headers=headers
    )
    readPaiPuListResJson = readPaiPuListRes.json()
    if len(readPaiPuListResJson["data"]) == 0:
        break
    print(len(readPaiPuListResJson["data"]))
    for item in readPaiPuListResJson["data"]:
        if item["endTime"] > startTime:
            startTime = item["endTime"] + 1
        print(str(item["paiPuId"]) + str(item["paiPuNotId"]))
    time.sleep(0.5)

# リクエストを送信

# readPaiPuListResJson["data"]
