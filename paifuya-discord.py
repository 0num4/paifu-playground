# 牌譜屋のデータからランキングを取得する
# discordに投稿する

import discord

import requests

# API endpoint URL
url = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/num_games?mode=26"

uradora_endpoint = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/%E9%87%8C%E5%AE%9D%E7%8E%87_rev?mode=26"
avg_rank_doma = "https://5-data.amae-koromo.com/api/v2/pl3/career_ranking/avg_rank?mode=24"

users = ["levena", "timpoにゃ", "電なのです", "0㌍", "高梨ミーシャ", "たくみんvtuber", "ぺいぺいちゃん"]


def check_nicknames_in_endpoints(nicknames, endpoints):
    found_nicknames = {}
    for endpoint in endpoints:
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            for player in data:
                player_nickname = player.get("nickname")
                if player_nickname in nicknames:
                    if player_nickname not in found_nicknames:
                        found_nicknames[player_nickname] = []
                    found_nicknames[player_nickname].append(endpoint)

    return found_nicknames


print(check_nicknames_in_endpoints(users, [url, uradora_endpoint, avg_rank_doma]))
