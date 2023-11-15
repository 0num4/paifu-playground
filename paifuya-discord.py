# 牌譜屋のデータからランキングを取得する
# discordに投稿する

import discord

import requests

# API endpoint URL
url = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/num_games?mode=26"

uradora_endpoint = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/%E9%87%8C%E5%AE%9D%E7%8E%87_rev?mode=26"
avg_rank_doma = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/avg_rank?mode=24"

# Custom headers
# headers = {
#     "authority": "5-data.amae-koromo.com",
#     "accept": "*/*",
#     "accept-language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5",
#     "origin": "https://ikeda.sapk.ch",
#     "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"macOS"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "cross-site",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
# }

users = ["levena", "timpoにゃ", "電なのです", "0㌍", "高梨ミーシャ", "たくみんvtuber"]
# Making a GET request to the API
response = requests.get(uradora_endpoint)
found_nicknames = []
# Checking if the request was successful
if response.status_code == 200:
    # Printing the response content
    data = response.json()

    for player in data:
        if player.get("nickname") in users:
            found_nicknames.append(player.get("nickname"))
else:
    # エラーが出た場合は終わる
    print("dataの取得に失敗しました")
    exit()

print(data)


# dataの中に該当のnicknameがあるかどうか

data
