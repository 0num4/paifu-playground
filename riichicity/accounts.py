import json
import requests
import Types.stats
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.baseTypes
import Types.accountTypes
import base


# TODO: pingにはheadersが必要ない
def ping_riichi_city(headers: dict) -> Types.accountTypes.PingResponse:
    res = requests.post("https://alicdn.mahjong-jp.net/ping", headers=headers)
    res = res.json()
    json.dump(res, open("ping_riichi_city.json", "w"))
    res = Types.accountTypes.PingResponse(**res, strict=True)
    print(res)
    return res


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


# TODO: 検証
def users_send_email_code(headers: dict, email: str, codeType: int = 0, lang: str = "ja") -> any:
    payload = {"email": email, "codeType": codeType, "lang": lang}
    res = requests.post("https://alicdn.mahjong-jp.net/users/sendEmailCode", json=payload, headers=headers)
    res = res.json()
    json.dump(res, open("users_send_email_code.json", "w"))
    print(res)
    return res


def users_retrieve_account(headers: dict, content: str) -> Types.accountTypes.UsersRetrieveAccountResponse:
    payload = {"content": content}
    usersRetrieveAccountRes = requests.post(
        "https://alicdn.mahjong-jp.net/users/retrieveAccount", json=payload, headers=headers
    )
    usersRetrieveAccountRes = usersRetrieveAccountRes.json()
    json.dump(usersRetrieveAccountRes, open("users_retrieve_account.json", "w"))
    usersRetrieveAccountRes = Types.accountTypes.UsersRetrieveAccountResponse(**usersRetrieveAccountRes, strict=True)
    print(usersRetrieveAccountRes)
    return usersRetrieveAccountRes


def main():
    # get_res_bundle_data()
    emailLoginRes = base.login_riichi_city()
    headers = base.get_headers(emailLoginRes)
    users_retrieve_account(headers, content="loq")

    print("end")


if __name__ == "__main__":
    main()
