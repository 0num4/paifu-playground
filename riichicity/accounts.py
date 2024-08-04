import hashlib
import json
import random
import uuid

import boto3
import requests
import Types.accountTypes
import Types.baseTypes
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.stats

# def insert_dynamo_user():
#     dynamodb = boto3.resource("dynamodb")
#     table = dynamodb.Table("users")
#     table.put_item(
#         Item={
#             "email":


# pingにはheadersが必要ない
def ping_riichi_city(headers: dict) -> Types.accountTypes.PingResponse:
    res = requests.post("https://alicdn.mahjong-jp.net/ping", headers=headers)
    res = res.json()
    json.dump(res, open("ping_riichi_city.json", "w"))
    res = Types.accountTypes.PingResponse(**res, strict=True)
    print(res)
    return res


# adjustIdをもらうため？
def users_get_last_login(headers: dict, adid: str) -> Types.accountTypes.UserGetLastLoginResponse:
    payload = {"adid": adid}  # emailloginから返ってくる
    userGetLastLoginRes = requests.post(
        "https://alicdn.mahjong-jp.net/users/getLastLogin", json=payload, headers=headers
    )
    userGetLastLoginRes = userGetLastLoginRes.json()
    json.dump(userGetLastLoginRes, open("users_get_last_login.json", "w"))
    userGetLastLoginRes = Types.accountTypes.UserGetLastLoginResponse(**userGetLastLoginRes, strict=True)
    print(userGetLastLoginRes)
    return userGetLastLoginRes


# ####### 新規登録系 ########


# TODO: 検証
def users_send_email_code(headers: dict, email: str, codeType: int = 0, lang: str = "ja") -> any:
    payload = {"email": email, "codeType": codeType, "lang": lang}
    res = requests.post("https://alicdn.mahjong-jp.net/users/sendEmailCode", json=payload, headers=headers)
    res = res.json()
    json.dump(res, open("users_send_email_code.json", "w"))
    print(res)
    return res


def users_email_verify(headers: dict, code: str, codeType: int = 0) -> any:
    payload = {"code": code, "codeType": codeType}
    # cookieが必須で、cookieでemail判別してそう
    res = requests.post("https://alicdn.mahjong-jp.net/users/emailVerify", json=payload)
    res = res.json()
    json.dump(res, open("users_email_verify.json", "w"))
    print(res)
    return res


# ####### 新規登録系 ########

# ログインはemailLoginが既に定義した


# パスワード紛失
def users_retrieve_account(headers: dict, content: str) -> Types.accountTypes.UsersRetrieveAccountResponse:
    payload = {"content": content}
    # ログインしてなくてもOK
    usersRetrieveAccountRes = requests.post("https://alicdn.mahjong-jp.net/users/retrieveAccount", json=payload)
    usersRetrieveAccountRes = usersRetrieveAccountRes.json()
    # json.dump(usersRetrieveAccountRes, open("users_retrieve_account_root_s_a_gmail.json", "w"))
    usersRetrieveAccountRes = Types.accountTypes.UsersRetrieveAccountResponse(**usersRetrieveAccountRes, strict=True)
    print(usersRetrieveAccountRes)
    return usersRetrieveAccountRes


# guestログインの流れ
# 1. initSession
# 2. users/tokenLogin


# response EmailLoginResponse
def users_token_login(
    headers: dict,
    adjustId: str,
    logCreate: bool = True,
    orinToken: str = "",
    tokenType: int = 1,
    tokenValue: str = "",  # uuidv4
) -> Types.stats.EmailLoginResponse:
    payload = {
        "adjustId": adjustId,
        "logCreate": logCreate,
        "orinToken": orinToken,
        "tokenType": tokenType,
        "tokenValue": tokenValue,
    }
    usersTokenLoginRes = requests.post("https://alicdn.mahjong-jp.net/users/tokenLogin", json=payload, headers=headers)
    usersTokenLoginRes = usersTokenLoginRes.json()
    # json.dump(usersTokenLoginRes, open("users_token_login.json", "w"))
    usersTokenLoginRes = Types.stats.EmailLoginResponse(**usersTokenLoginRes, strict=True)
    print(usersTokenLoginRes)
    return usersTokenLoginRes


# deviceIDさえ持っておけばsidは降ってくる
def users_init_session(
    deviceId: uuid.UUID | None = None, sid: str | None = None
) -> Types.accountTypes.UsersInitSessionResponse:

    if deviceId is None:
        uuidv4 = uuid.uuid4()
        deviceId = str(uuidv4).upper()
        print(f"users_init_session deviceId: {deviceId}")
    cookie = {
        "platform": "ios",
        "channel": "default",
        "lang": "ja",
        "version": "2.1.1.40364",
        "deviceid": deviceId,
    }
    if sid is not None:
        cookie["sid"] = sid
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "x-unity-version": "2021.3.42f1c1",
        "cookies": json.dumps(cookie),
        "user-agent": "ProductName/44 CFNetwork/1490.0.4 Darwin/23.2.0",
        "accept-language": "ja",
    }
    usersInitSessionRes = requests.post("https://alicdn.mahjong-jp.net/users/initSession", headers=headers)
    usersInitSessionRes = usersInitSessionRes.json()
    # json.dump(usersInitSessionRes, open("users_init_session.json", "w"))
    usersInitSessionRes = Types.accountTypes.UsersInitSessionResponse(**usersInitSessionRes, strict=True)
    print(usersInitSessionRes)
    return usersInitSessionRes


def GetEncryptDeviceID(str) -> str:
    len_str = len(str)
    if len_str % 2 != 0:
        len_str += 1

    new_str = ""
    for i in range(0, len_str, 2):
        new_str += str[i]

    md5 = hashlib.md5(new_str.encode("utf-8")).hexdigest()
    return str + md5[:6]


def dummyadid() -> str:
    # 1文字目を'1'に設定し、残り31文字をランダムな16進数で生成
    random_hex = "".join(random.choices("0123456789abcdef", k=31))
    adid = "1" + random_hex
    return adid


# 流れ
# 1. store_create_payment_order

# logsuccessfulpurchase(steam)
# 2. store_complete_payment_order
# 3. get_product_list(いらないけどui的に)


def store_create_payment_order(
    headers: dict,
    amount: int = 0.99,
    area: str = "jp",
    channel: str = "steam",
    email: str = "a@a.com",
    itemNum: int = 80,
    item_id: int = 10001,
    item_name: str = "一番券",
    lang: str = "ja",
    payer: str = "steam",
    productSKU: str = "com.riichicity.happywoods_1000108",
    site_type: int = 3,
    token_id: str = "76561199017366274",  # ここの値は何回かリクエストを送ってみても変わらない
    version: str = "2.1.3.41302",
) -> any:
    payload = {
        "amount": amount,
        "area": area,
        "channel": channel,
        "email": email,
        "itemNum": itemNum,
        "item_id": item_id,
        "item_name": item_name,
        "lang": lang,
        "payer": payer,
        "productSKU": productSKU,
        "site_type": site_type,
        "token_id": token_id,
        "version": version,
    }
    res = ""  # requests.post("https://alicdn.mahjong-jp.net/store/createPaymentOrder", json=payload, headers=headers)
    res = res.json()
    json.dump(res, open("store_create_payment_order.json", "w"))
    print(res)
    return res


def store_complete_payment_order(headers: dict, orderID: str) -> any:
    payload = {"orderID": orderID}
    res = ""  # requests.post("https://alicdn.mahjong-jp.net/store/completePaymentOrder", json=payload, headers=headers)
    res = res.json()
    json.dump(res, open("store_complete_payment_order.json", "w"))
    print(res)
    return res


def create_user() -> dict:
    uuidv4 = uuid.uuid4()
    deviceId = str(uuidv4).upper()
    print(f"deviceId: {deviceId}")
    usersInitSessionRes = users_init_session(
        deviceId=deviceId,
    )
    if usersInitSessionRes.code != 0:
        print("initSession failed")
        return {}
    sid = usersInitSessionRes.data
    print(f"sid: {sid}")
    adid = dummyadid()  # "15f2a866c599359064f937f89a43de46"
    print(f"adid: {adid}")
    cookie = {
        "platform": "ios",
        "channel": "default",
        "lang": "ja",
        "version": "2.1.1.40364",
        "deviceid": deviceId,
        "sid": sid,
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "x-unity-version": "2021.3.42f1c1",
        "cookies": json.dumps(cookie),
        "user-agent": "ProductName/44 CFNetwork/1490.0.4 Darwin/23.2.0",
        "accept-language": "ja",
    }
    print(headers)
    userTokenLoginRes = users_token_login(
        headers,
        adjustId=adid,
        logCreate=True,
        orinToken=deviceId,
        tokenType=1,
        tokenValue=GetEncryptDeviceID(deviceId),
    )
    if userTokenLoginRes.code != 0:
        print("tokenLogin failed")
        return {}

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("create-account")
    response = table.put_item(
        Item={
            "id": str(userTokenLoginRes.data.user.id),  # uid
            "device_id": deviceId,
            "sid": sid,
            "adid": adid,
            "nickname": userTokenLoginRes.data.user.nickname,
            "res": userTokenLoginRes.model_dump(),
            "cookie": cookie,
            "headers": headers,
        }
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
        return {"statusCode": 500, "body": "Failed to create account."}
    print("Account created.")

    print(userTokenLoginRes)


# AWS_PROFILE=ankokuyakusyo python riichicity/accounts.py
def main():
    create_user()
    # create()
    # get_res_bundle_data()
    # emailLoginRes = base.login_riichi_city()


if __name__ == "__main__":
    main()
