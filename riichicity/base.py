import os
import json
import requests
import time

import pydantic
import Types.stats
import Types.commonConsts
import Types.importantConsts


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
    round: list[int] = [1, 2],
    stageType: list[int] = [1, 2, 3, 4],
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
    # userDetailStatsRes = Types.stats.UserDetailStatsV2Response(**userDetailStatsRes, strict=True)
    print(userDetailStatsRes)
    return userDetailStatsRes


# TODO: 動かない
def get_user_detail_stats_v2_info(
    headers: dict,
    userID: str,
    gameplay: int,
    playerCount: int,
    round: int = 2,
    stageType: int = 4,
) -> dict:
    payload = {
        "userID": userID,
        "playerCount": playerCount,
        "gameplay": gameplay,
        "round": round,
        "stageType": stageType,
    }
    userDetailStatsV2InfoRes = requests.post(
        "https://alicdn.mahjong-jp.net/stats/userDetailStatsV2Info", json=payload, headers=headers
    )
    userDetailStatsV2InfoRes = userDetailStatsV2InfoRes.json()
    print(userDetailStatsV2InfoRes)
    return userDetailStatsV2InfoRes


# function M:userBaseData(userID, gameplay, playerCount)
#     local data = {userID = userID, gameplay = gameplay, playerCount = playerCount}
#     HttpUtil.MjGamePost("users/userBaseData", data, RSP.userBaseData, data)
# end


def get_user_base_data(headers: dict, userID: str, gameplay: int, playerCount: int) -> Types.stats.UserBaseDataResponse:
    payload = {"userID": userID, "gameplay": gameplay, "playerCount": playerCount}
    userBaseDataRes = requests.post("https://alicdn.mahjong-jp.net/users/userBaseData", json=payload, headers=headers)
    userBaseDataRes = userBaseDataRes.json()
    print(userBaseDataRes)
    userBaseDataRes = Types.stats.UserBaseDataResponse(**userBaseDataRes, strict=True)
    return userBaseDataRes


# -- 牌谱对局数据
# function M:getPaipuUserGames(paipuId)
#     local data = {paipuId = paipuId}
#     HttpUtil.MjGamePost("stats/getPaipuUserGames", data, RSP.getPaipuUserGamesRsp, data)
# end


# 動かない、ログインしたユーザーの牌譜しか取れない
def get_paipu_user_games(headers: dict, paipuId: str) -> dict:
    payload = {"paipuId": paipuId}
    getPaipuUserGamesRes = requests.post(
        "https://alicdn.mahjong-jp.net/stats/getPaipuUserGames", json=payload, headers=headers
    )
    getPaipuUserGamesRes = getPaipuUserGamesRes.json()
    print(getPaipuUserGamesRes)
    return getPaipuUserGamesRes


# --[[
#     不限制都为0
#     classifyID:比赛为房间id（字符串）,其他不用传
#     matchID:大奖赛 匹配ID  其他玩法可不传
# ]]--这里有时间可以改下，太多参数了
# function M:readPaiPuList(startTime, enTime, gamePlay, classifyID, skip, limit, isSelf,matchID,stageType,matchType)
#     local data = {startTime = startTime, endTime = enTime, gamePlay = gamePlay, classifyID = classifyID, skip = skip, limit = limit, isSelf = isSelf,matchID=matchID,stageType = stageType,matchType = matchType}
#     HttpUtil.MjGamePost("record/readPaiPuList", data, RSP.readPaiPuList, data)
# end


def read_pai_pu_list(
    headers: dict,
    startTime: int,
    enTime: int,
    gamePlay: int,
    classifyID: str,
    skip: int,
    limit: int,
    isSelf: bool,
    matchID: str,
    stageType: int,
    matchType: int,
) -> dict:
    payload = {
        "startTime": startTime,
        "endTime": enTime,
        "gamePlay": gamePlay,
        "classifyID": classifyID,
        "skip": skip,
        "limit": limit,
        "isSelf": isSelf,
        "matchID": matchID,
        "stageType": stageType,
        "matchType": matchType,
    }
    readPaiPuListRes = requests.post(
        "https://alicdn.mahjong-jp.net/record/readPaiPuList", json=payload, headers=headers
    )
    readPaiPuListRes = readPaiPuListRes.json()
    print(readPaiPuListRes)
    return readPaiPuListRes


# function M:collectPaiPu(paiPuId, isCancel, remark)
#     local data = {paiPuId = paiPuId, isCancel = isCancel, remark = remark}
#     HttpUtil.MjGamePost("record/collectPaiPu", data, RSP.collectPaiPu, data, true)
# end


# ブックマーク。isCancelがtrueだとブックマーク解除。当然ですがisCollectの値はユーザー単位で見え方が違う(別のユーザーの別のブックマークは違うので)
def collect_pai_pu(headers: dict, paiPuId: str, isCancel: bool, remark: str) -> Types.stats.CollectPaiPuResponse:
    payload = {"paiPuId": paiPuId, "isCancel": isCancel, "remark": remark}
    collectPaiPuRes = requests.post("https://alicdn.mahjong-jp.net/record/collectPaiPu", json=payload, headers=headers)
    collectPaiPuRes = collectPaiPuRes.json()
    print(collectPaiPuRes)
    collectPaiPuRes = Types.stats.CollectPaiPuResponse(**collectPaiPuRes, strict=True)
    return collectPaiPuRes


# function M:getRoomData(isObserve, keyValue,handID)
#     local data = {isObserve = isObserve, keyValue = keyValue,handID = handID}
#     HttpUtil.MjGamePost("record/getRoomData", data, RSP.getRoomData, data, true)
# end

# function M:getGameData(roomId, eventStartPos)
#     local data = {roomId = roomId, eventStartPos = eventStartPos}
#     HttpUtil.MjGamePost("record/getGameData", data, RSP.getGameData, data, true)
# end


# いつもの牌譜データ取得のやつ！！
def get_room_data(headers: dict, isObserve: bool, keyValue: str, handID: str) -> dict:
    payload = {"isObserve": isObserve, "keyValue": keyValue, "handID": handID}
    getRoomDataRes = requests.post("https://alicdn.mahjong-jp.net/record/getRoomData", json=payload, headers=headers)
    getRoomDataRes = getRoomDataRes.json()
    print(getRoomDataRes)
    return getRoomDataRes


# 動いたけど、[]になってる
def get_game_data(headers: dict, roomId: str, eventStartPos: int) -> dict:
    payload = {"roomId": roomId, "eventStartPos": eventStartPos}
    getGameDataRes = requests.post("https://alicdn.mahjong-jp.net/record/getGameData", json=payload, headers=headers)
    getGameDataRes = getGameDataRes.json()
    print(getGameDataRes)
    return getGameDataRes


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
    res = get_user_detail_stats_v2(
        headers, userID="617696847", gameplay=1001, playerCount=3, round=[1, 2], stageType=[1, 2, 3, 4], dataType=0
    )
    print(res)
    save_json(res, "get_user_detail_stats_v2_rank.json")


if __name__ == "__main__":
    main()
