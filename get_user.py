# -*- coding: utf-8 -*-
"""
このプログラムの目的
対象: 最近聖上がりした豪3のユーザー一覧を取得する。
"""


import requests
import json
import time
import matplotlib.pyplot as plt

# !pip -q -q -q install japanize-matplotlib

# macだとフォントをインストールする必要がある
# https://datumstudio.jp/blog/matplotlib%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E6%96%87%E5%AD%97%E5%8C%96%E3%81%91%E3%82%92%E8%A7%A3%E6%B6%88%E3%81%99%E3%82%8Bwindows%E7%B7%A8/
# import japanize_matplotlib
from tqdm import tqdm

# @markdown ####以下にプレイヤー名を入力し、左部の再生ボタン(▷)を押してください。
# @markdown ####モード選択で四麻と三麻を切り替えることができます。
# TODO: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
プレイヤー名 = "0\u330D"  # @param {type:"string"}
# TODO: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
モード選択 = "\u4E09\u9EBB"  # @param ['四麻', '三麻']
if モード選択 == "四麻":
    s0 = "https://5-data.amae-koromo.com/api/v2/pl4/"
    mode = "16,15,12,11,9,8"
    Color = {16: "r", 15: "r", 12: "g", 11: "g", 9: "y", 8: "y"}
    pre_level = 10301
elif モード選択 == "三麻":
    s0 = "https://5-data.amae-koromo.com/api/v2/pl3/"
    mode = "26,24,22,25,23,21"
    Color = {26: "r", 25: "r", 24: "g", 23: "g", 22: "y", 21: "y"}
    pre_level = 20301
# @markdown ####同一のプレイヤー名のIDが複数存在しており、別IDに切り替える場合は次の値を1増やしてください。
同名ID切替 = 0  # @param {type:'integer'}
print(f"プレイヤー名：{プレイヤー名}")
pdata = requests.get(f"{s0}search_player/{プレイヤー名}").json()[同名ID切替]
pid = pdata["id"]
start = pdata["latest_timestamp"]
X = []
for i in range(100):
    s1 = f"{s0}player_records/{pid}/{start}999/1262304000000?limit=500&mode={mode}&descending=true&tag="
    games = requests.get(s1).json()
    length = len(games)
    if length == 0:
        break
    print(f"({i}) 読み込み試合数: {length}")
    start = games[-1]["startTime"] - 1
    X += games
    if length < 500:
        break
    time.sleep(0.01)

d = ["士", "傑", "豪", "聖", "天", "魂"]
p = {301: 6, 302: 7, 303: 10, 401: 14, 402: 16, 403: 18, 501: 20, 502: 30, 503: 45}
level_dan = lambda level: f"{d[level // 100 % 100 - 2]}{level % 100}"
level_pt_base = lambda level: 5000 if level // 100 % 100 >= 6 else p[level % 1000] * 100

# @markdown ####・細かい設定
# @markdown #####「左端」と「右端」を指定すると、何戦から何戦までを表示するかを指定できます。
# @markdown #####※右端は適当な大きな数を入れておくと最後まで表示します。
左端 = 0  # @param {type: 'integer'} # default = 0
右端 = 100000  # @param {type: 'integer'} # default = 1000000
# @markdown #####「上端」を指定すると、縦軸のポイント表示の上限を変更できます。
上端 = 10000  # @param {type: 'integer'} # default = 10000

plt.figure(facecolor="w", figsize=(16, 10))
if 左端 == 0:
    plt.text(3, 100, f"傑\n1", fontsize=15)
pre_pt, pt, base = 600, 600, 600
for i, game in enumerate(tqdm(X[::-1])):
    for data in game["players"]:
        if data["accountId"] == pid:
            level = data["level"]
            if pre_level != level:
                if 左端 <= i <= 右端:
                    s = level_dan(level)
                    plt.text(i + 3, 100, f"{s[0]}\n{s[1:]}", fontsize=15)
                    plt.vlines(i, 0, max(level_pt_base(level), level_pt_base(pre_level)) * 2, color="k")
                base = level_pt_base(level)
                pt = pre_pt = base
            pt += data["gradingScore"] * 5 if level // 100 % 100 >= 7 else data["gradingScore"]
            if 左端 <= i <= 右端:
                plt.plot([i, i + 1], [pre_pt, pt], color="k", lw=1.5)
                plt.fill_between([i, i + 1], [pre_pt, pt], color=Color[game["modeId"]], alpha=0.05)
                plt.plot([i, i + 1], [base, base], color="k", lw=1.5)
                plt.plot([i, i + 1], [base * 2, base * 2], color="k", lw=1.5)
            pre_level, pre_pt = level, pt
plt.title(f"雀魂段位戦ポイント推移[{モード選択}]({プレイヤー名})", fontsize=30)
plt.xlabel("試合数", fontsize=20)
plt.ylabel("ポイント", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks([i * 1000 for i in range(11)], fontsize=20)
plt.xlim([左端, min(右端, i + 1)])
plt.ylim([0, 上端 + 100])
plt.show()

import numpy as np
from collections import Counter
import datetime

# @markdown #段位戦履歴表示
# @markdown ####ポイントグラフ作成後にフォーム左部の再生ボタン(▷)を押すと、各段位区間の日付、順位内訳、対戦数、平均順位、最高pt、最低pt、卓の内訳の一覧を表示させることができます。
# @markdown ####開発中のためバグ等はご容赦ください。
maid_to_ma = {
    16: "4王南",
    12: "4玉南",
    9: "4金南",
    15: "4王東",
    11: "4玉東",
    8: "4金東",
    26: "3王南",
    24: "3玉南",
    22: "3金南",
    25: "3王東",
    23: "3玉東",
    21: "3金東",
}


def get_rank(player_list, target_account_id):
    sorted_list = sorted(player_list, key=lambda x: x["score"], reverse=True)
    sorted_ids = [player["accountId"] for player in sorted_list]
    return sorted_ids.index(target_account_id) + 1


if モード選択 == "四麻":
    pre_level = 10203
elif モード選択 == "三麻":
    pre_level = 20203

hist = []
pre_pt, pt, base = 600, 600, 600
for i, game in enumerate(X[::-1]):
    for data in game["players"]:
        if data["accountId"] == pid:
            level = data["level"]
            if pre_level != level:
                hist.append([])
                base = level_pt_base(level)
                pt = pre_pt = base
            pt += data["gradingScore"] * 5 if level // 100 % 100 >= 7 else data["gradingScore"]
            rank = get_rank(game["players"], pid)
            dt1 = datetime.datetime.fromtimestamp(game["startTime"])
            dt2 = datetime.datetime.fromtimestamp(game["endTime"])
            ma = game["modeId"]
            gdata = (i, dt1, dt2, maid_to_ma[ma], level_dan(pre_level), level_dan(level), rank, pre_pt, pt)
            hist[-1].append(gdata)
            pre_level, pre_pt = level, pt

# Find maximum length of each element
max_period_length = max_n_length = max_pt_length = max_rank_length = max_ro_length = max_counter_mas_length = 0
for g in hist:
    a = np.array(g)
    period = (a[:, 2][-1].date() - a[:, 1][0].date()).days + 1
    max_period_length = max(max_period_length, len(str(period)))
    n = len(a)
    max_n_length = max(max_n_length, len(str(n)))
    pts = np.concatenate([a[:, 7], [a[:, 8][-1]]])
    max_pt = max(pts)
    min_pt = min(pts)
    max_pt_length = max(max_pt_length, len(str(max_pt)), len(str(min_pt)))
    ranks = a[:, 6]
    avg_rank = np.mean(ranks)
    max_rank_length = max(max_rank_length, len(str(avg_rank)))
    counter_ranks = Counter(ranks)
    ro = [counter_ranks[i] for i in (1, 2, 3, 4)]
    max_ro_length = max(max_ro_length, *map(len, map(str, ro)))
    counter_mas = Counter(a[:, 3])
    max_counter_mas_length = max(max_counter_mas_length, *map(len, map(str, counter_mas.values())))

print(f"雀魂段位戦履歴[{モード選択}]({プレイヤー名})")
for g in hist:
    a = np.array(g)
    n = len(a)
    counter_mas = Counter(a[:, 3])
    ranks = a[:, 6]
    counter_ranks = Counter(ranks)
    ro = [counter_ranks[i] for i in (1, 2, 3, 4)]
    pts = np.concatenate([a[:, 7], [a[:, 8][-1]]])
    s0 = "戦, ".join(f"{k}{v:{max_counter_mas_length}}" for k, v in counter_mas.items()) + "戦"
    period = (a[:, 2][-1].date() - a[:, 1][0].date()).days + 1
    s = f'{a[:, 1][0].strftime("%Y/%m/%d")}-{a[:, 2][-1].strftime("%Y/%m/%d")} '
    s += f"({period:{max_period_length}}日)【{a[:, 4][-1]}】"
    s += f"({ro[0]:{max_ro_length}} +{ro[1]:{max_ro_length}} "
    s += f"+{ro[2]:{max_ro_length}} +{ro[3]:{max_ro_length}})="
    s += f"{n:{max_n_length}}戦, "
    s += f"平均順位 {np.mean(ranks):.3f}, "
    s += f"最高pt {pts.max():{max_pt_length}}, "
    s += f"最低pt {pts.min():{max_pt_length}} | {s0}"
    print(s)
