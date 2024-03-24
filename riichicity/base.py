import os
import json
import requests
import time

import pydantic
import Types.stats


def login_riichi_city() -> dict:
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

        return emailLoginRes
    else:
        print("Failed to log into Riichi city")
        return None


def get_headers(emailLoginRes: dict) -> dict:
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
    return headers


def get_live_info_from_riichi_city(
    headers: dict, playerCount: int = 3, round: int = 2, stageType: int = 4
) -> list[str]:

    payload = {
        "stageType": stageType,
        "round": round,
        "playerCount": playerCount,
        "gamePlay": 1001,
        "frends": False,
    }
    readOnlineRoomRes = requests.post(
        "https://alicdn.mahjong-jp.net/record/readOnlineRoom", json=payload, headers=headers
    )
    readOnlineRoomResJson = readOnlineRoomRes.json()
    print(readOnlineRoomResJson)
    if readOnlineRoomResJson["code"] == 0:
        print("Successfully read online room")
        readOnlineRoomResJson["data"]
    # format teest
    return readOnlineRoomResJson


# function M:userDetailStats(userID, gameplay, playerCount)
#     local data = {userID = userID, playerCount = playerCount, gameplay = gameplay}
#     HttpUtil.MjGamePost("stats/userDetailStats", data, RSP.userDetailStats, data)
# end
# function M:userDetailStatsV2(userID, gameplay, playerCount)
#     if gameplay == 1001 then
#         local round,stageType,dataType = self:GetCurToggleMsgData()
#         local data = {userID = userID, playerCount = playerCount, gameplay = gameplay,round = round,stageType = stageType,dataType = dataType}
#         HttpUtil.MjGamePost("stats/userDetailStatsV2", data, RSP.userDetailStatsV2, data)
#     else
#         local data = {userID = userID, playerCount = playerCount, gameplay = gameplay}
#         HttpUtil.MjGamePost("stats/userDetailStatsV2", data, RSP.userDetailStatsV2, data)
#     end
# end

# function M:userDetailStatsV2Info(userID, gameplay, playerCount)
#     local round,stageType,dataType = self:GetCurToggleMsgData()
#     local data = {userID = userID, playerCount = playerCount, gameplay = gameplay,round = round,stageType = stageType}
#     HttpUtil.MjGamePost("stats/userDetailStatsV2Info", data, RSP.userDetailStatsV2Info, data)
# end


def get_user_detail_stats(
    headers: dict, userID: str, gameplay: int, playerCount: int
) -> Types.stats.UserDetailStatsV2Response:
    payload = {"userID": userID, "playerCount": playerCount, "gameplay": gameplay}
    userDetailStatsRes = requests.post(
        "https://alicdn.mahjong-jp.net/stats/userDetailStats", json=payload, headers=headers
    )
    userDetailStatsRes = userDetailStatsRes.json()

    print(userDetailStatsRes)
    return userDetailStatsRes


def get_user_detail_stats_v2(
    headers: dict,
    userID: str,
    gameplay: int,
    playerCount: int,
    round: int = 2,
    stageType: int = 4,
    dataType: int = 0,
) -> Types.stats.UserDetailStatsV2Response:
    if gameplay == 1001:
        payload = {
            "userID": userID,
            "playerCount": playerCount,
            "gameplay": gameplay,
            "round": round,
            "stageType": stageType,
            "dataType": dataType,
        }
    else:
        payload = {"userID": userID, "playerCount": playerCount, "gameplay": gameplay}
    userDetailStatsRes = requests.post(
        "https://alicdn.mahjong-jp.net/stats/userDetailStatsV2", json=payload, headers=headers
    )
    userDetailStatsRes = userDetailStatsRes.json()
    userDetailStatsRes = Types.stats.UserDetailStatsV2Response(**userDetailStatsRes, strict=True)
    print(userDetailStatsRes)
    return userDetailStatsRes


playerCountDict = {3: "三麻", 4: "四麻"}

roundDict = {1: "東風", 2: "半荘"}

stageTypeDict = {3: "陽炎", 4: "銀河"}


def save_json(data: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f)
        f.close()


def main():
    emailLoginRes = login_riichi_city()
    headers = get_headers(emailLoginRes)
    res = get_user_detail_stats_v2(headers, "618112137", 1002, 3)
    save_json(res.model_dump_json(), "userDetailStatsv2.json")


if __name__ == "__main__":
    main()
