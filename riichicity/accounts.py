import json
import random
import uuid
import requests
import Types.stats
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.baseTypes
import Types.accountTypes
import hashlib


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


# TODO: エラーが出た
# response EmailLoginResponse
def users_token_login(
    headers: dict,
    adjustId: str,
    logCreate: bool = True,
    orinToken: str = "",
    tokenType: int = 1,
    tokenValue: str = "",  # uuidv4
) -> any:
    payload = {
        "adjustId": adjustId,
        "logCreate": logCreate,
        "orinToken": orinToken,
        "tokenType": tokenType,
        "tokenValue": tokenValue,
    }
    usersTokenLoginRes = requests.post("https://alicdn.mahjong-jp.net/users/tokenLogin", json=payload, headers=headers)
    usersTokenLoginRes = usersTokenLoginRes.json()
    json.dump(usersTokenLoginRes, open("users_token_login.json", "w"))
    # usersTokenLoginRes = Types.accountTypes.UsersTokenLoginResponse(**usersTokenLoginRes, strict=True)
    print(usersTokenLoginRes)
    return usersTokenLoginRes


def create_cookie() -> dict:
    # fetchDomainNameRes = base.fetch_domain_name()
    # checkVersionRes = base.users_check_version()
    return {}


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


def GetEncryptDeviceID(str):
    len_str = len(str)
    if len_str % 2 != 0:
        len_str += 1

    new_str = ""
    for i in range(0, len_str, 2):
        new_str += str[i]

    md5 = hashlib.md5(new_str.encode("utf-8")).hexdigest()
    return str + md5[:6]


def dummyadid():
    # 1文字目を'1'に設定し、残り31文字をランダムな16進数で生成
    random_hex = "".join(random.choices("0123456789abcdef", k=31))
    adid = "1" + random_hex
    return adid


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
    res = users_token_login(
        headers,
        adjustId=adid,
        logCreate=True,
        orinToken=deviceId,
        tokenType=1,
        tokenValue=GetEncryptDeviceID(deviceId),
    )
    print(res)


def main():
    create_user()
    # create()
    # get_res_bundle_data()
    # emailLoginRes = base.login_riichi_city()


if __name__ == "__main__":
    main()
