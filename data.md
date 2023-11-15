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
