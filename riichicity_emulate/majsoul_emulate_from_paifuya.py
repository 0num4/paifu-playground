# paifuya-stats.py
import requests
import streamlit as st
import datetime
import sys
import pydantic

import paifuya_utils.util

endpoints = [
    "https://5-data.amae-koromo.com/api/v2/pl3/player_records/73425222/1700007119999/1262304000000?limit=153&mode=22&descending=true&tag=53",
    "https://5-data.amae-koromo.com/api/v2/pl3/global_histogram",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_stats/73425222/1262304000000/1700007119999?mode=26.24.22.25.23.21&tag=472224",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_extended_stats/73425222/1262304000000/1700007119999?mode=22&tag=472224",
    "https://5-data.amae-koromo.com/api/v2/pl3/player_stats/73425222/1262304000000/1700007119999?mode=22&tag=472224",
]

print(sys.path)


class PlayerLevel(pydantic.BaseModel):
    id: int
    score: int
    delta: int


class PlayerData(pydantic.BaseModel):
    id: int
    nickname: str
    level: PlayerLevel
    latest_timestamp: datetime.datetime


def getplayerIds(name, game_mode=3) -> list[PlayerData] | None:
    if game_mode == 3:
        s0 = "https://5-data.amae-koromo.com/api/v2/pl3/"
    elif game_mode == 4:
        s0 = "https://5-data.amae-koromo.com/api/v2/pl4/"
    res = requests.get(f"{s0}search_player/{name}").json()
    if len(res) == 0:
        return None
    print(res)
    playerdatas = pydantic.TypeAdapter(list[PlayerData])
    pdatas = playerdatas.validate_python(res)
    for pdata in pdatas:
        print(pdata.latest_timestamp)
        print(pdata.nickname)
        print(paifuya_utils.util.parse_dan(pdata.level.id))
    print(pdatas)
    # date = pdata
    # date = datetime.datetime.fromtimestamp(date)
    
    # print(date.strftime("%Y-%m-%d %H:%M:%S"))
    # return pdata["id"]


st.title("majsoul sanma sampling")
num_games = st.selectbox("Number of games", [100, 500, 1000, 2000, 3000], index=1)
player_name = st.text_input("Player name", "みちよん")
player_id = getplayerIds(player_name)
num_dan = st.selectbox(
    "坂を選んでください",
    ("豪1", "豪2", "豪3"))

st.write(num_dan)
st.write("Player ID: ", player_id)

if __name__ == "__main__":
    getplayerIds("みちよん")
