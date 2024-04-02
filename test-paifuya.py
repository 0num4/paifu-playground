import requests


def check_nickname_in_api(nickname):
    url = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/%E9%87%8C%E5%AE%9D%E7%8E%87_rev?mode=26"
    headers = {
        "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Referer": "",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"macOS"',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for player in data:
            if player.get("nickname") == nickname:
                return True
        return False
    else:
        print("APIからの応答がありません。")
        return False


# ここでニックネームをチェック
nickname_to_check = "ぺいぺいちゃん"
exists = check_nickname_in_api(nickname_to_check)
if exists:
    print(f"ニックネーム '{nickname_to_check}' はAPIデータに存在します。")
else:
    print(f"ニックネーム '{nickname_to_check}' はAPIデータに存在しません。")
