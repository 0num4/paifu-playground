import os
import json
import requests
import Types.stats
import Types.commonConsts
import Types.consts
import Types.readPaiPuList
import Types.baseTypes
import datetime
import time
import pydantic
import Types.accountTypes


#
def fetch_domain_name() -> Types.baseTypes.FetchDomainNameResponse:
    url = "https://d3qgi0t347dz44.cloudfront.net/release/notice/domain_name.ncc"
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    json.dump(response, open("fetch_domain_name.json", "w"))
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


def login_riichi_city() -> Types.stats.EmailLoginResponse:
    # res = fetch_domain_name()
    # print(res.domain_name)
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
        "X-Unity-Version": "2020.3.42f1c1",
    }
    return headers


# TODO: pingにはheadersが必要ない
def ping_riichi_city(headers: dict) -> Types.accountTypes.PingResponse:
    res = requests.post("https://alicdn.mahjong-jp.net/ping", headers=headers)
    res = res.json()
    json.dump(res, open("ping_riichi_city.json", "w"))
    res = Types.accountTypes.PingResponse(**res, strict=True)
    print(res)
    return res


def users_get_last_login(headers: dict, adid: str) -> Types.accountTypes.UserGetLastLoginResponse:
    payload = {"adid": adid}
    userGetLastLoginRes = requests.post(
        "https://alicdn.mahjong-jp.net/users/getLastLogin", json=payload, headers=headers
    )
    userGetLastLoginRes = userGetLastLoginRes.json()
    json.dump(userGetLastLoginRes, open("users_get_last_login.json", "w"))
    userGetLastLoginRes = Types.accountTypes.UserGetLastLoginResponse(**userGetLastLoginRes, strict=True)
    print(userGetLastLoginRes)
    return userGetLastLoginRes


def main():
    # get_res_bundle_data()
    emailLoginRes = login_riichi_city()
    headers = get_headers(emailLoginRes)
    users_get_last_login(headers, "1")

    print("end")


if __name__ == "__main__":
    main()
