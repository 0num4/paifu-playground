import requests

endpoints = [
    "https://5-data.amae-koromo.com/api/v2/pl3/player_records/73425222/1700007119999/1262304000000?limit=153&mode=22&descending=true&tag=53",
    "https://5-data.amae-koromo.com/api/v2/pl3/global_histogram",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_stats/73425222/1262304000000/1700007119999?mode=26.24.22.25.23.21&tag=472224",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_extended_stats/73425222/1262304000000/1700007119999?mode=22&tag=472224",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_stats/73425222/1262304000000/1700007119999?mode=22&tag=472224",
]


def getplayerId(name, game_mode=3):
    if game_mode == 3:
        s0 = "https://5-data.amae-koromo.com/api/v2/pl3/"
    elif game_mode == 4:
        s0 = "https://5-data.amae-koromo.com/api/v2/pl4/"
    pdata = requests.get(f"{s0}search_player/{name}").json()[0]
    return pdata["id"]


print(getplayerId("ぺいぺいちゃん"))
