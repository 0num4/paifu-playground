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

import hogehoge_pb2 で import して.proto で定義した構造体を読み込める

```
import hogehoge_pb2

a= hogehoge_bp2.Hoge()
a.hoge = "hoge"
```

まとめ

- 最初に.protoc を作る
- protoc でそれぞれの言語の定義にコンパイルする(.py や.cpp など)
- それをインポートして使う

go の場合は option go_package = "hogehoge"; でパッケージ名を指定する必要がある

```
syntax = "proto3";

option go_package = "./gen";

package helloworld;
message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

option gopackage の部分は出力したいディレクトリか github.com/hoge みたいな go 特有のパッケージの謎指定方法を書く
