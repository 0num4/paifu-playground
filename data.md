    s1 = f"{s0}player_records/{pid}/{start}999/1262304000000?limit=500&mode={mode}&descending=true&tag="
    games = requests.get(s1).json()

```
{'accountId': 69645757, 'nickname': '超絶肉球', 'level': 20403, 'score': 76900, 'gradingScore': 217}
```

この level は豪は 204,聖は 205。03 や 01 は段位。

4 人麻雀のデータを取得する場合
"https://5-data.amae-koromo.com/api/v2/pl4/"

3 人麻雀のデータを取得する場合
"https://5-data.amae-koromo.com/api/v2/pl3/"

### https://5-data.amae-koromo.com/api/v2/pl3/player_records/73425222/1700007119999/1262304000000?limit=153&mode=22&descending=true&tag=53 について

最初の 1700007119999 の部分は starttime+999。starttime は現在の unixtime などで良い。もしくは search_player の latest_timestamp で取れる(paifuya-stats.py)

```
タイムスタンプ＝1262304000
↓
日時（Tokyo）＝2010/01/01 09:00:00
```

逆に player_stats api は最後の日付(126304000)から最新の日付っぽい
