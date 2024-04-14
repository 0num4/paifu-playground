import os
import json
import random
import requests
import Types.stats
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.baseTypes
import datetime
import time
import pydantic


#
def fetch_domain_name() -> Types.baseTypes.FetchDomainNameResponse:
    url = "https://d3qgi0t347dz44.cloudfront.net/release/notice/domain_name.ncc"
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    # json.dump(response, open("fetch_domain_name.json", "w"))
    response = Types.baseTypes.FetchDomainNameResponse(**response, strict=True)
    return response


def users_check_version(
    headers: dict, channel: str = "default", platform: str = "ios", version: str = "2.1.16.31622"
) -> Types.baseTypes.CheckVersionResponse:
    payload = {
        "channel": channel,
        "platform": platform,
        "version": version,
    }
    checkVersionRes = requests.post("https://alicdn.mahjong-jp.net/users/checkVersion", json=payload, headers=headers)
    checkVersionRes = checkVersionRes.json()
    print(checkVersionRes)
    # json.dump(checkVersionRes, open("users_check_version_latest.json", "w"))
    checkVersionRes = Types.baseTypes.CheckVersionResponse(**checkVersionRes, strict=True)
    return checkVersionRes


# checkVersionで差異があったら呼ばれる
# wget https://d3qgi0t347dz44.cloudfront.net/release/ios/20240329002/version.txt
def get_version():
    # ここの日付は
    getVersionRes = requests.get("https://d3qgi0t347dz44.cloudfront.net/release/ios/20240329002/version.txt")
    if getVersionRes.status_code == 200:
        print(getVersionRes.text)
    else:
        print(f"error! {getVersionRes.status_code} Failed to get version")


# バイナリ差分をダウンロード。使う予定はない
def get_res_bundle_data():
    getResBundleData = requests.get("https://d3qgi0t347dz44.cloudfront.net/release/ios/20240329002/res_bundle_data.dat")
    if getResBundleData.status_code == 200:
        print(getResBundleData.text)
    else:
        print(f"error! {getResBundleData.status_code} Failed to get version")


def login_riichi_city(adjustId: str | None = None) -> Types.stats.EmailLoginResponse:
    # res = fetch_domain_name()
    # print(res.domain_name)
    # リクエストヘッダーを設定
    headers = {
        "Content-Type": "application/json",
        "Cookies": f'{{"channel":"default","deviceid":"{os.environ["deviceid"]}","lang":"en","sid":"{os.environ["sid"]}","version":"2.0.6.31622","platform":"linux"}}',
    }

    payload = {"passwd": os.environ["passwd"], "email": os.environ["email"]}

    if adjustId is not None:
        payload["adjustId"] = adjustId
    response = requests.post("https://alicdn.mahjong-jp.net/users/emailLogin", json=payload, headers=headers)

    emailLoginRes = response.json()
    print(emailLoginRes)
    # json.dump(emailLoginRes, open("emailLoginRes.json", "w"))
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
        "X-Unity-Version": "2020.3.42f1c1",  # TODO: ここが変わっていく
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


# function M:userBrief(userId)
#     local data = {userId = userId}
#     HttpUtil.MjGamePost("users/userBrief", data, RSP.userBriefRsp, data)
# end


def get_user_brief(headers: dict, userId: str) -> Types.stats.UserBriefResponse:
    payload = {"userId": userId}
    userBriefRes = requests.post("https://alicdn.mahjong-jp.net/users/userBrief", json=payload, headers=headers)
    userBriefRes = userBriefRes.json()
    print(userBriefRes)
    userBriefRes = Types.stats.UserBriefResponse(**userBriefRes, strict=True)
    return userBriefRes


def get_user_tasks(headers: dict) -> dict[any]:
    userTasksRes = requests.post("https://alicdn.mahjong-jp.net/activity/userTask", headers=headers)
    userTasksRes = userTasksRes.json()
    print(userTasksRes)
    # userBriefRes = Types.stats.UserBriefResponse(**userBriefRes, strict=True)
    return userTasksRes


# get_user_tasksでtaskを持ってきて個別のawardはget_user_task_awardで獲得できる。
# ログインしてないので動作未確認
def get_user_task_award(headers: dict, taskId: int = 12004, type: int = 1) -> dict[any]:
    payload = {"taskId": taskId, "type": type}
    userTaskAwardRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/userTaskAward", json=payload, headers=headers
    )
    userTaskAwardRes = userTaskAwardRes.json()
    print(userTaskAwardRes)
    return userTaskAwardRes


# デイリークエスト一括で獲得する
def get_activity_collect_task_award(
    headers: dict, typeList: list[int] = [1, 3]
) -> Types.stats.CollectTaskAwardResponse:
    payload = {"typeList": typeList}
    activityCollectTaskAwardRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/collectTaskAward", json=payload, headers=headers
    )
    activityCollectTaskAwardRes = activityCollectTaskAwardRes.json()
    print(activityCollectTaskAwardRes)
    # json.dump(activityCollectTaskAwardRes, open("get_activity_collect_task_award.json", "w"))
    activityCollectTaskAwardRes = Types.stats.CollectTaskAwardResponse(**activityCollectTaskAwardRes, strict=True)
    return activityCollectTaskAwardRes


# 動作未確認
def get_store_buy_product(
    headers: dict, productID: int = 579, num: int = 1
) -> Types.stats.StoreBuyProductResponse:  # 579は毎日の無料ボーナス
    payload = {"productID": productID, "num": num}
    storeBuyProductRes = requests.post("https://alicdn.mahjong-jp.net/store/buyProduct", json=payload, headers=headers)
    storeBuyProductRes = storeBuyProductRes.json()
    print(storeBuyProductRes)
    storeBuyProductRes = Types.stats.StoreBuyProductResponse(**storeBuyProductRes, strict=True)
    # json.dump(storeBuyProductRes, open("get_store_buy_product.json", "w"))
    return storeBuyProductRes


def get_product_list(
    headers: dict, firstLabel: int = 3, isCheckSkin: bool = True, secondLabel: int = 0
) -> Types.stats.GetProductListResponse:
    payload = {
        "firstLabel": firstLabel,
        "isCheckSkin": isCheckSkin,
        "secondLabel": secondLabel,
    }
    productRes = requests.post("https://alicdn.mahjong-jp.net/store/getProductList", json=payload, headers=headers)
    productRes = productRes.json()
    productRes = Types.stats.GetProductListResponse(**productRes, strict=True)
    print(productRes)
    return productRes


# ガチャ引くリスト？
def store_get_draw(headers: dict) -> Types.stats.StoreGetDrawResponse:
    payload = {}
    storeGetDrawRes = requests.post("https://alicdn.mahjong-jp.net/store/getDraw", json=payload, headers=headers)
    storeGetDrawRes = storeGetDrawRes.json()
    # json.dump(storeGetDrawRes, open("store_get_draw.json", "w"))
    storeGetDrawRes = Types.stats.StoreGetDrawResponse(**storeGetDrawRes, strict=True)
    print(storeGetDrawRes)
    return storeGetDrawRes


# TODO: 検証
def store_user_draw(headers: dict, pool: int = 38, type: int = 1) -> any:
    payload = {"pool": pool, "type": type}
    storeUserDrawRes = requests.post("https://alicdn.mahjong-jp.net/store/userDraw", json=payload, headers=headers)
    storeUserDrawRes = storeUserDrawRes.json()
    print(storeUserDrawRes)
    json.dump(storeUserDrawRes, open("store_user_draw.json", "w"))
    return storeUserDrawRes


# 風林火山イベ
def get_activity_ex_team_daily_award(headers: dict) -> Types.stats.EXTeamDailyAwardResponse:
    payload = {}
    activityEXTeamDailyAwardRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/eXTeamDailyAward", json=payload, headers=headers
    )
    activityEXTeamDailyAwardAwardRes = activityEXTeamDailyAwardRes.json()
    # json.dump(activityEXTeamDailyAwardAwardRes, open("get_activity_ex_team_daily_award.json", "w"))
    print(activityEXTeamDailyAwardAwardRes)
    activityEXTeamDailyAwardRes = Types.stats.EXTeamDailyAwardResponse(**activityEXTeamDailyAwardAwardRes, strict=True)
    return activityEXTeamDailyAwardRes


def activity_ex_team_task(headers: dict) -> Types.stats.EXTeamTaskResponse:
    payload = {}
    activityEXTeamTaskRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/eXTeamTask", json=payload, headers=headers
    )
    activityEXTeamTaskRes = activityEXTeamTaskRes.json()
    # json.dump(activityEXTeamTaskRes, open("activity_ex_team_task.json", "w"))
    print(activityEXTeamTaskRes)
    activityEXTeamTaskRes = Types.stats.EXTeamTaskResponse(**activityEXTeamTaskRes, strict=True)
    return activityEXTeamTaskRes


# TODO: 検証 壊れてるかも
def activity_receive_ex_team_task(headers: dict, taskID: int = 3, type: int = 4) -> dict[any]:
    payload = {"taskID": taskID, "type": type}
    activityReceiveEXTeamTaskRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/receiveEXTeamTask", json=payload, headers=headers
    )
    activityReceiveEXTeamTaskRes = activityReceiveEXTeamTaskRes.json()
    # json.dump(activityReceiveEXTeamTaskRes, open("activity_receive_ex_team_task.json", "w"))
    print(activityReceiveEXTeamTaskRes)
    activityReceiveEXTeamTaskRes = Types.stats.EXTeamTaskResponse(**activityReceiveEXTeamTaskRes, strict=True)
    return activityReceiveEXTeamTaskRes


# デイリークエストのキャラ見る用
def activity_view_action(
    headers: dict, actionId: Types.consts.EnumDefine.TaskActionServer = 2042
) -> Types.stats.ActivityViewActionResponse:
    payload = {"actionId": actionId}
    activityViewActionRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/viewAction", json=payload, headers=headers
    )
    activityViewActionRes = activityViewActionRes.json()
    print(activityViewActionRes)
    # json.dump(activityViewActionRes, open("activity_view_action.json", "w"))
    activityViewActionRes = Types.stats.ActivityViewActionResponse(**activityViewActionRes, strict=True)
    return activityViewActionRes


def activity_activity_list(
    headers: dict, lang: str = "ja", reqVersion: str = "v1"
) -> Types.stats.ActivityActivityListResponse:
    payload = {"lang": lang, "reqVersion": reqVersion}
    activityActivityListRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/activityList", json=payload, headers=headers
    )
    activityActivityListRes = activityActivityListRes.json()
    print(activityActivityListRes)
    # json.dump(activityActivityListRes, open("activity_activity_list.json", "w"))
    activityActivityListRes = Types.stats.ActivityActivityListResponse(**activityActivityListRes, strict=True)
    return activityActivityListRes


def activity_receive_sign_award(
    headers: dict, activityId: int = 10124, awardType: Types.consts.AwardType = 3
) -> Types.baseTypes.ReceiveSignAwardResponse:
    payload = {"activityId": activityId, "awardType": awardType}
    activityReceiveSignAwardRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/receiveSignAward", json=payload, headers=headers
    )
    activityReceiveSignAwardRes = activityReceiveSignAwardRes.json()
    # json.dump(activityReceiveSignAwardRes, open("activity_receive_sign_award.json", "w"))
    print(activityReceiveSignAwardRes)
    activityReceiveSignAwardRes = Types.baseTypes.ReceiveSignAwardResponse(**activityReceiveSignAwardRes, strict=True)
    return activityReceiveSignAwardRes


def activity_user_sign_progress(headers: dict, activityId: int = 10124) -> Types.baseTypes.UserSignProgressResponse:
    payload = {"activityId": activityId}
    activityUserSignProgressRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/userSignProgress", json=payload, headers=headers
    )
    activityUserSignProgressRes = activityUserSignProgressRes.json()
    json.dump(activityUserSignProgressRes, open("activity_user_sign_progress.json", "w"))
    print(activityUserSignProgressRes)
    activityUserSignProgressRes = Types.baseTypes.UserSignProgressResponse(**activityUserSignProgressRes, strict=True)
    return activityUserSignProgressRes


def lobbys_read_official_match(headers: dict, lang: str = "ja") -> Types.stats.ReadOfficialMatchResponse:
    payload = {"lang": lang}
    lobbysReadOfficialMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/readOfficialMatch", json=payload, headers=headers
    )
    lobbysReadOfficialMatchRes = lobbysReadOfficialMatchRes.json()
    print(lobbysReadOfficialMatchRes)
    # json.dump(lobbysReadOfficialMatchRes, open("lobbys_read_official_match.json", "w"))
    lobbysReadOfficialMatchRes = Types.stats.ReadOfficialMatchResponse(**lobbysReadOfficialMatchRes, strict=True)
    return lobbysReadOfficialMatchRes


# TODO: やる。型をつける
def lobbys_sign_official_match(headers: dict, isCancel: bool = False, officialID: str = "") -> dict[any]:
    payload = {"isCancel": isCancel, "officialID": officialID}
    lobbysSignOfficialMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/signOfficialMatch", json=payload, headers=headers
    )
    lobbysSignOfficialMatchRes = lobbysSignOfficialMatchRes.json()
    print(lobbysSignOfficialMatchRes)
    json.dump(lobbysSignOfficialMatchRes, open("lobbys_sign_official_match.json", "w"))
    # lobbysReadOfficialMatchRes = Types.stats.SignOfficialMatchResponse(**lobbysReadOfficialMatchRes, strict=True)
    return lobbysSignOfficialMatchRes


# 日時設定されてるグランプリ(週間大会とか)の情報を取得。定期的に取得して時間になったら多分こちらからつなぎに行くっぽい
def lobbys_read_timing_match(headers: dict) -> Types.stats.ReadTimingMatchResponse:
    payload = {}
    lobbysReadTimingMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/readTimingMatch", json=payload, headers=headers
    )
    lobbysReadTimingMatchRes = lobbysReadTimingMatchRes.json()
    # print(lobbysReadTimingMatchRes)
    # json.dump(lobbysReadTimingMatchRes, open("lobbys_read_timing_match.json", "w"))
    lobbysReadTimingMatchRes = Types.stats.ReadTimingMatchResponse(**lobbysReadTimingMatchRes, strict=True)
    return lobbysReadTimingMatchRes


# TODO: 検証
def lobbys_ready_official_next(
    headers: dict, matchID: str = "", matchStage: int = 2, officialID: str = ""
) -> Types.stats.ReadyOfficialNextResponse:
    payload = {"matchID": matchID, "matchStage": matchStage, "officialID": officialID}
    lobbysReadyOfficialNextRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/readyOfficialNext", json=payload, headers=headers
    )
    lobbysReadyOfficialNextRes = lobbysReadyOfficialNextRes.json()
    print(lobbysReadyOfficialNextRes)
    json.dump(lobbysReadyOfficialNextRes, open("lobbys_ready_official_next.json", "w"))
    return lobbysReadyOfficialNextRes


def lobbys_sign_timing_match(
    headers: dict, isCancel: bool = False, signItemID: int = 10002, timingID: str = ""
) -> Types.stats.SignTimingMatchResponse:
    payload = {"isCancel": isCancel, "signItemID": signItemID, "timingID": timingID}
    lobbysSignTimingMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/signTimingMatch", json=payload, headers=headers
    )
    lobbysSignTimingMatchRes = lobbysSignTimingMatchRes.json()
    print(lobbysSignTimingMatchRes)
    # json.dump(lobbysSignTimingMatchRes, open("lobbys_sign_timing_match.json", "w"))
    lobbysSignTimingMatchRes = Types.stats.SignTimingMatchResponse(**lobbysSignTimingMatchRes, strict=True)
    return lobbysSignTimingMatchRes


# TODO: 検証
def get_message_receive_award(headers: dict, mailID: str, userID: str) -> dict:
    payload = {"mailID": mailID, "userID": userID}
    messageReceiveAwardRes = requests.post(
        "https://alicdn.mahjong-jp.net/message/receiveAward", json=payload, headers=headers
    )
    messageReceiveAwardRes = messageReceiveAwardRes.json()
    print(messageReceiveAwardRes)
    return messageReceiveAwardRes


def get_message_user_message(headers: dict, lang: str = "ja", userID: str = "") -> dict:
    payload = {"lang": lang, "userID": userID}
    messageUserMessageRes = requests.post(
        "https://alicdn.mahjong-jp.net/message/userMessage", json=payload, headers=headers
    )
    messageUserMessageRes = messageUserMessageRes.json()
    print(messageUserMessageRes)
    json.dump(messageUserMessageRes, open("get_message_user_message.json", "w"))
    return messageUserMessageRes


def get_gift_code(headers: dict, code: str) -> Types.stats.GetGiftCodeResponse:
    payload = {"code": code}
    giftCodeRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/activateRedeemCode", json=payload, headers=headers
    )
    giftCodeRes = giftCodeRes.json()
    print(giftCodeRes)
    # json.dump(giftCodeRes, open("get_gift_code.json", "w"))
    giftCodeRes = Types.stats.GetGiftCodeResponse(**giftCodeRes, strict=True)
    return giftCodeRes


# stageごとのオンラインの人数が取れる
def lobbys_read_stage_classifies(
    headers: dict,
) -> Types.stats.LobbysReadStageClassifiesResponse:
    lobbysReadStageClassifiesRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/readStageClassifies", headers=headers
    )
    lobbysReadStageClassifiesRes = lobbysReadStageClassifiesRes.json()
    print(lobbysReadStageClassifiesRes)
    # json.dump(lobbysReadStageClassifiesRes, open("lobbys_read_stage_classifies.json", "w"))
    lobbysReadStageClassifiesRes = Types.stats.LobbysReadStageClassifiesResponse(
        **lobbysReadStageClassifiesRes, strict=True
    )
    return lobbysReadStageClassifiesRes


def backpack_recycle_gift(
    headers: dict, isAll: bool = False, itemID: int = 11003, num: int = 1
) -> Types.stats.BackpackRecycleGiftResponse:
    payload = {
        "isAll": isAll,
        "items": [
            {
                "itemID": itemID,
                "num": num,
            }
        ],
    }
    backpackRecycleGiftRes = requests.post(
        "https://alicdn.mahjong-jp.net/backpack/recycleGift", json=payload, headers=headers
    )
    backpackRecycleGiftRes = backpackRecycleGiftRes.json()
    print(backpackRecycleGiftRes)
    # json.dump(backpackRecycleGiftRes, open("backpack_recycle_gift.json", "w"))
    backpackRecycleGiftRes = Types.stats.BackpackRecycleGiftResponse(**backpackRecycleGiftRes, strict=True)
    return backpackRecycleGiftRes


def backpack_user_item_list(headers: dict, isUserEquip: bool = False) -> Types.stats.BackpackUserItemListResponse:
    payload = {
        "isUserEquip": isUserEquip,
    }
    backpackUserItemListRes = requests.post(
        "https://alicdn.mahjong-jp.net/backpack/userItemList", json=payload, headers=headers
    )
    backpackUserItemListRes = backpackUserItemListRes.json()
    print(backpackUserItemListRes)
    # json.dump(backpackUserItemListRes, open("backpack_user_item_list.json", "w"))
    backpackUserItemListRes = Types.stats.BackpackUserItemListResponse(**backpackUserItemListRes, strict=True)
    return backpackUserItemListRes


# ランキングの情報を取得。デフォルト値は4麻
def activity_read_ranks(
    headers: dict, index: int = 0, kind: int = 1, limit: int = 100, scope: int = 1, skip: int = 0
) -> Types.stats.ActivityReadRanksResponse:
    payload = {"index": index, "kind": kind, "limit": limit, "scope": scope, "skip": skip}
    # payload_4ma = {
    #     "index": 0,
    #     "kind": 1,
    #     "limit": 100,
    #     "scope": 1,
    #     "skip": 0,
    # }
    # payload_3ma = {
    #     "index": 0,
    #     "kind": 3,
    #     "limit": 100,
    #     "scope": 1,
    #     "skip": 0,
    # }
    activityReadRanksRes = requests.post(
        "https://alicdn.mahjong-jp.net/activity/readRanks", json=payload, headers=headers
    )
    activityReadRanksRes = activityReadRanksRes.json()
    # json.dump(activityReadRanksRes, open("activity_read_ranks_3ma.json", "w"))
    print(activityReadRanksRes)
    activityReadRanksRes = Types.stats.ActivityReadRanksResponse(**activityReadRanksRes, strict=True)
    return activityReadRanksRes


# その他/activity/achiveUserInfoなどがプロフ欄から飛べるやつ

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


# 未検証。段位開始時に使う。classifyIDはreadStageClassifiesから取れる
def lobbys_start_stage(headers: dict, classifyID: str) -> dict:
    payload = {"classifyID": classifyID}
    lobbysStartStageRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/startStage", json=payload, headers=headers
    )
    lobbysStartStageRes = lobbysStartStageRes.json()
    print(lobbysStartStageRes)
    return lobbysStartStageRes


# 未検証。段位開始時に使う？
def lobbys_cancel_stage(headers: dict, matchID: str) -> dict:
    payload = {"matchID": matchID}
    lobbysCancelStageRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/cancelStage", json=payload, headers=headers
    )
    lobbysCancelStageRes = lobbysCancelStageRes.json()
    print(lobbysCancelStageRes)
    return lobbysCancelStageRes


# 友人戦のpublic roomを取得、その他更新ボタンもこれ。クイック参加はjoinPublicRoom
def lobbys_read_public_room(headers: dict, playerCount: int, round: int) -> Types.stats.lobbysReadPublicRoomResponse:
    payload = {"playerCount": playerCount, "round": round}
    lobbysReadPublicRoomRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/readPublicRoom", json=payload, headers=headers
    )
    lobbysReadPublicRoomRes = lobbysReadPublicRoomRes.json()
    print(lobbysReadPublicRoomRes)
    # json.dump(lobbysReadPublicRoomRes, open("lobbys_read_public_room.json", "w"))
    lobbysReadPublicRoomRes = Types.stats.lobbysReadPublicRoomResponse(**lobbysReadPublicRoomRes, strict=True)
    return lobbysReadPublicRoomRes


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
    if isinstance(data, pydantic.BaseModel):
        data = data.model_dump_json()
    with open(filename, "w") as f:
        json.dump(data, f)
        f.close()


def signMatch_dev(headers: dict):
    lobbysReadTimingMatchRes = lobbys_read_timing_match(headers)
    if lobbysReadTimingMatchRes.code == 0:
        for item in lobbysReadTimingMatchRes.data:
            print(item)
            if item.isSign is False:
                print(f"参加してない: {item.officialID}")
                print(f"参加料: {item.signItemList[0].num}, ItemID: {item.signItemList[0].itemID}")
                print(f"日時: {datetime.datetime.fromtimestamp(item.startTime)}")
                if item.signItemList[0].itemID == 10002:
                    res = lobbys_sign_timing_match(headers, isCancel=False, signItemID=10002, timingID=item.officialID)
                    print(res)
                    print(f"参加しました: {item.officialID}")
                    sleep_time = random.uniform(3, 5)
                    time.sleep(sleep_time)
    # res = lobbys_sign_official_match(headers)
    # save_json(res, "lobbys_sign_official_match.json")


# /release/notice/domain_name.ncc
# /users/checkVersion
# /ping
# /users/initSession
# /users/emailLogin
# /backpack/userEquip
# /users/getRoleInfo
# /mixed_content/redDot
# /users/userBaseData
# /activity/specialBag
# /activity/userTask
# /activity/activityList
# /store/GetDraw
# /store/storeRed
# users/userSetting
# /activity/userSignProgress
# /activity/receiveSignAward
# /activity/activityList


def print_item_list(items: list[Types.stats.BackpackUserItemListResponseUserItem]):
    for item in items:
        itemName = Types.consts.ItemName.search_by_value(item.itemID)
        itemTypeName = Types.consts.EnumDefine.ItemType(item.itemType).name
        print(
            f"ItemType: {item.itemType}, ItemTypeName: {itemTypeName}, ItemID: {item.itemID}, ItemName: {itemName}, num: {item.num}"
        )


def daily_recycle_gift(headers: dict) -> bool:
    res = backpack_user_item_list(headers)
    gift_items: list[Types.stats.BackpackUserItemListResponseUserItem] = [
        item for item in res.data if item.itemType == 11
    ]
    print_item_list(gift_items)
    recycled = False
    for item in gift_items:
        itemName = Types.consts.ItemName.search_by_value(item.itemID)
        # itemTypeName = Types.consts.EnumDefine.ItemType(item.itemType).name
        # print(
        #     f"ItemType: {item.itemType}, ItemTypeName: {itemTypeName}, ItemID: {item.itemID}, ItemName: {itemName}, num: {item.num}"
        # )
        if item.num > 1:
            res = backpack_recycle_gift(headers, isAll=False, itemID=item.itemID, num=1)
            if res.code == 0:
                print(f"Successfully recycled {itemName}")
                recycled = True
                break  # 1回で終わり
            else:
                print(f"Failed to recycle {itemName}")
    print(f"recycled: {recycled}")
    return recycled


def lobbys_get_friend_match_rule(headers: dict) -> any:
    # 友人戦のルール一覧を取得
    # TODO: 実装
    pass


def lobbys_create_friend_match(
    headers: dict, rule: Types.stats.FrendMatchRule
) -> Types.stats.lobbysCreateFriendMatchResponse:
    payload = {
        "rule": rule.model_dump(),
    }
    lobbysCreateFriendMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/createFriendMatch", json=payload, headers=headers
    )
    lobbysCreateFriendMatchRes = lobbysCreateFriendMatchRes.json()
    print(lobbysCreateFriendMatchRes)
    # json.dump(lobbysCreateFriendMatchRes, open("lobbys_create_friend_match.json", "w"))
    lobbysCreateFriendMatchRes = Types.stats.lobbysCreateFriendMatchResponse(**lobbysCreateFriendMatchRes, strict=True)
    return lobbysCreateFriendMatchRes


def lobbys_enter_friend_match(headers: dict, roomNum: str) -> Types.stats.EnterFriendMatchResponse:
    payload = {"roomNum": roomNum}
    lobbysEnterFriendMatchRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/enterFriendMatch", json=payload, headers=headers
    )
    lobbysEnterFriendMatchRes = lobbysEnterFriendMatchRes.json()
    print(lobbysEnterFriendMatchRes)
    # json.dump(lobbysEnterFriendMatchRes, open("lobbys_enter_friend_match.json", "w"))
    lobbysEnterFriendMatchRes = Types.stats.EnterFriendMatchResponse(**lobbysEnterFriendMatchRes, strict=True)
    return lobbysEnterFriendMatchRes


def lobbys_friend_player_action(
    headers: dict, action: int = 8, matchId: str = ""  # 1: ゲーム開始, 8: CPU追加
) -> Types.stats.lobbysFriendPlayerActionResponse:
    payload = {"action": action, "matchId": matchId}
    lobbysFriendPlayerActionRes = requests.post(
        "https://alicdn.mahjong-jp.net/lobbys/friendPlayerAction", json=payload, headers=headers
    )
    lobbysFriendPlayerActionRes = lobbysFriendPlayerActionRes.json()
    print(lobbysFriendPlayerActionRes)
    # json.dump(lobbysFriendPlayerActionRes, open("lobbys_friend_player_action.json", "w"))
    lobbysFriendPlayerActionRes = Types.stats.lobbysFriendPlayerActionResponse(
        **lobbysFriendPlayerActionRes, strict=True
    )
    return lobbysFriendPlayerActionRes


def daily_friend_match(headers: dict) -> bool:
    # is_success = False
    rule = Types.stats.FrendMatchRule(
        FangFu=5,
        IsAdvancedOptions=False,
        IsChiDuan=False,
        IsConvenientTips=False,
        IsGeMu=False,
        IsKaiLiZhi=False,
        IsLuck=False,
        IsMinusRiichi=False,
        IsMoreoptions=False,
        IsNanXiRu=False,
        IsNotEffect=False,
        IsNotShowHand=False,
        IsOpenVoice=False,
        IsRandSeat=True,
        IsShaoJi=False,
        RoomType=0,
        ThreeZiMoType=0,
        changBang="400",
        fristReqPoints="40000",
        initialPoints="35000",
        isKnock=True,
        isTopReward=True,
        minimumPoints="40000",
        numRedCard=4,
        operFixedTime=3,
        operVarTime=5,
        orderPoints=[10, 0, -10],
        playerCount=3,
        round=3,  # 1: 東風, 2: 半荘 3: 一局
    )
    res = lobbys_create_friend_match(headers, rule=rule)
    if res.code == 0:
        print("Successfully created friend match")
        time.sleep(0.5)
        # dataは6桁の数字
        lobbysEnterFriendMatchRes = lobbys_enter_friend_match(headers, roomNum=res.data)
        if lobbysEnterFriendMatchRes.code == 0:
            print("Successfully entered friend match")
            time.sleep(0.5)
            addCpuAction = lobbys_friend_player_action(headers, action=8, matchId=lobbysEnterFriendMatchRes.data.Id)
            if addCpuAction.code == 0:
                print("Successfully added CPU")
            else:
                print("Failed to add CPU")
                return False
            time.sleep(0.5)
            addCpuAction2 = lobbys_friend_player_action(headers, action=8, matchId=lobbysEnterFriendMatchRes.data.Id)
            if addCpuAction2.code == 0:
                print("Successfully added CPU2")
            else:
                print("Failed to add CPU2")
                return False
            time.sleep(1)
            gameStartAction = lobbys_friend_player_action(headers, action=1, matchId=lobbysEnterFriendMatchRes.data.Id)
            if gameStartAction.code == 0:
                print("Successfully started game")
                return True
            else:
                print("Failed to start game")
                return False
        else:
            print("Failed to enter friend match")
            return False
    else:
        print("Failed to create friend match")
        return False


def get_daily(headers: dict):
    # 毎日ログイン
    activityList = activity_activity_list(headers)
    list = [activity for activity in activityList.data.list if activity.activityType == 0]
    if len(list) == 1:
        activityId = list[0].activityId
    else:
        print("Failed to get daily activity")
        activityId = 10125
    userSignProgress = activity_user_sign_progress(headers, activityId)
    if userSignProgress.code == 0:
        print(
            f"Successfully got user sign progress. persistentDay: {userSignProgress.data.persistentDay}, persistentStatusList: {userSignProgress.data.persistentStatusList}, signDay: {userSignProgress.data.signDay}, signStatusList: {userSignProgress.data.signStatusList}"
        )
        receiveSignAward = activity_receive_sign_award(headers, activityId, 3)
        if receiveSignAward.code == 0:
            print("Successfully received sign award")
            for item in receiveSignAward.awards:
                try:
                    itemName = Types.consts.EnumDefine.ItemID(item.itemId).name
                    print(f"ItemID: {item.itemId}, ItemName: {itemName} num: {item.num}")
                except (ValueError, KeyError):
                    print(f"ItemID: {item.itemId}, unRegisterdItemName, num: {item.num}")
        else:
            print("Failed to receive sign award")
    else:
        print("Failed to get user sign progress")
    # 雀士一覧を見る
    res = activity_view_action(headers, actionId=Types.consts.EnumDefine.TaskActionServer["ViewCharsList"].value)
    if res.code == 0:
        print("Successfully 雀士一覧を見る action")
    else:
        print("Failed to 雀士一覧を見る action")
    # キャラの育成を見る
    res = activity_view_action(headers, actionId=Types.consts.EnumDefine.TaskActionServer["ViewShopRoleFeed"].value)
    if res.code == 0:
        print("Successfully キャラクター餌やりを見る action")
    else:
        print("Failed to キャラクター餌やりを見る action")
    # ギフトの回収
    if daily_recycle_gift(headers):
        print("Successfully collected gift")
    else:
        print("Failed to collect gift")
    # ストアの毎日無料アイテムを取得
    res = get_product_list(headers)
    if res.code == 0:
        print("Successfully got product list")
        res2 = get_store_buy_product(headers, productID=579, num=1)
        if res2.code == 0:
            print("Successfully get daily free item")
        else:
            print("Failed to get daily free item")
    # if daily_friend_match(headers):
    #     print("Successfully daily friend match")
    # else:
    #     print("Failed daily friend match")
    # # 2回対局する必要がある
    # if daily_friend_match(headers):
    #     print("Successfully daily friend match")
    # else:
    #     print("Failed daily friend match")
    # 上記で完了した報酬の取得
    daily_res = get_activity_collect_task_award(headers, typeList=[1, 3])
    if daily_res.code == 0:
        print("Successfully got daily task")
    else:
        print("Failed to get daily task")
    weekly_res = get_activity_collect_task_award(headers, typeList=[4, 5])
    if weekly_res.code == 0:
        print("Successfully got weekly task")
    else:
        print("Failed to get weekly task")


def readAllPaiPu(headers: dict) -> list[Types.readPaiPuList.ReadPaiPuListType1 | None]:
    all_pai_pu = []
    end_time = int(datetime.datetime.now().timestamp())
    while True:
        payload = {
            "friendID": 813942315,
            "endTime": end_time,
        }
        readPaiPuListRes = requests.post(
            "https://alicdn.mahjong-jp.net/record/readPaiPuList", json=payload, headers=headers
        )
        readPaiPuListRes = readPaiPuListRes.json()
        if len(readPaiPuListRes["data"]) == 0:
            break
        elif readPaiPuListRes["code"] != 0:
            print("Failed to get pai pu list")
            break
        elif not readPaiPuListRes["data"]:
            break
        earliest_date = min(data["endTime"] for data in readPaiPuListRes["data"])
        latest_date = max(data["endTime"] for data in readPaiPuListRes["data"])
        print(f"readPaiPuListRes count {len(readPaiPuListRes['data'])}")
        print(f"earliest_date: {datetime.datetime.fromtimestamp(earliest_date)} {earliest_date}")
        print(f"latest_date: {datetime.datetime.fromtimestamp(latest_date)} {latest_date}")
        readPaiPuListRes = Types.readPaiPuList.ReadPaiPuListType1(**readPaiPuListRes, strict=True)
        all_pai_pu.append(readPaiPuListRes)
        end_time = earliest_date - 1
        time.sleep(random.uniform(3, 5))

    return all_pai_pu


def main():
    # get_res_bundle_data()
    emailLoginRes = login_riichi_city()
    headers = get_headers(emailLoginRes)
    store_get_draw(headers)
    # res = get_live_info_from_riichi_city(headers)
    # print(res)
    # lobbys_read_public_room(headers, playerCount=3, round=0)
    # get_daily(headers)

    # res = get_gift_code(headers, code="MQYFJCM")

    # users_check_version(headers, channel="default", platform="ios", version="2.1.1")
    # res = activity_user_sign_progress(headers, activityId=10124)
    # res = activity_receive_sign_award(headers, activityId=10124, awardType=3)
    # # res = get_gift_code(headers, code="happybirthday03210")
    # res = get_activity_ex_team_daily_award(headers)
    # if res.code == 0:
    #     print("Successfully got activity ex team daily award")
    # res = activity_receive_ex_team_task(headers)
    # signMatch_dev(headers)
    # backpack_recycle_gift(headers)
    # activity_ex_team_task(headers)
    # activity_read_ranks(headers)
    # res = lobbys_read_stage_classifies(headers)
    # save_json(res, "get_activity_ex_team_daily_award.json")

    print("end")


if __name__ == "__main__":
    main()
