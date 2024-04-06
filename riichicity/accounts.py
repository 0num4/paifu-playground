import json
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


# TODO: 検証
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
    usersTokenLoginRes = Types.accountTypes.UsersTokenLoginResponse(**usersTokenLoginRes, strict=True)
    print(usersTokenLoginRes)
    return usersTokenLoginRes


def main():
    # get_res_bundle_data()
    # emailLoginRes = base.login_riichi_city()
    # headers = base.get_headers(emailLoginRes)
    # users_retrieve_account(headers, content="loq")
    users_email_verify({}, "560546", 0)
    print("end")


if __name__ == "__main__":
    main()
