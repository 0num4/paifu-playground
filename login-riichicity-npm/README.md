# login-riichicity-npm

To install dependencies:

```bash
bun install
```

To run:

```bash
bun run index.ts
```

This project was created using `bun init` in bun v1.0.0. [Bun](https://bun.sh) is a fast all-in-one JavaScript runtime.

# 一番街ログインスクリプト

ref:
https://github.com/Badtaro/RiichiCityTournamentBot/blob/main/scripts/riichicitybot.js
https://github.com/Badtaro/RiichiCityTournamentBot/blob/main/requests/requests.js#L22

## ログインの流れ

1. domain list(donmain-name.ncc)でドメインを取得する。alicdn.mahjong-jp.net のようなドメインが帰ってくるはず
2. https://${domain}/users/initSession に post を送る。普通に rest api っぽい。
   https://github.com/Badtaro/RiichiCityTournamentBot/blob/main/requests/requests.js#L79C5-L79C5
