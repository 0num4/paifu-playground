import requests
import json
import dotenv
import os

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
payload = {
    "stageType": 4,
    "round": 2,
    "playerCount": 4,
    "gamePlay": 1001,
    "frends": False,
}
readOnlineRoomRes = requests.post("https://alicdn.mahjong-jp.net/record/readOnlineRoom", json=payload, headers=headers)
