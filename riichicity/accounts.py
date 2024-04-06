import json
import uuid
import requests
import Types.stats
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.baseTypes
import Types.accountTypes
import base


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


def users_init_session(deviceId: uuid.UUID | None = None, sid: str | None = None) -> any:

    if deviceId is None:
        uuidv4 = uuid.uuid4()
        deviceId = str(uuidv4).upper()
    print(deviceId)
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


def create(deviceId: str, sid: str, adid: str) -> dict:
    deviceId = "9770F499-D93A-4100-B11E-0A4BB390D9BA"
    # res = users_init_session()
    sid = "co8etieai08cuuf8ja20dd5a8b"  # res["data"]
    adid = "15f2a866c599359054f937f89a43de46"
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
        tokenValue=deviceId + "08b5b1",
    )
    print(res)


def main():
    deviceId = "9770F499-D93A-4100-B11E-0A4BB390D9BA"
    # res = users_init_session()
    sid = "co8etieai08cuuf8ja20dd5a8b"  # res["data"]
    adid = "15f2a866c599359054f937f89a43de46"  # 作り方がわからないので適当に作った。オリジナルは→ # "15f2a866c599359054f937f89a43de47"
    create(deviceId, sid, adid)
    # get_res_bundle_data()
    # emailLoginRes = base.login_riichi_city()
    # headers = base.get_headers(emailLoginRes)
    # users_retrieve_account(headers, content="loq")
    # users_email_verify({}, "560546", 0)
    # print("end")


if __name__ == "__main__":
    main()
