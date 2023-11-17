# protoc-study

なんだか急に protocol buffer の練習がしたくなってきたにゃ

helloworld.proto・・・手動で書いたファイル

protocol buffer の最新は 3
protoc は protocol buffer のコンパイラ

最初にバージョンの宣言をする
message hoge で構造体というかデータの宣言をする

```
paifu-playground/protoc-study on  main [!?] via 🐹 v1.20.3 on ☁️  r.oonuma@matsuri-tech.com
❯ protoc helloworld.proto --go_out=./
helloworld.proto:3:1: Expected ";".

```

```
protoc --python_out=./ helloworld.proto
```
