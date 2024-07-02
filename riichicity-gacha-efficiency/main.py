"""ガチャ券の効率シミュレーターツール.

ガチャ券目当てでデイリー秋刀魚27人大会出場するのどうなんにゃろ。体感としては割と効率いいと思ってるにゃ
参加料10枚で3トップ取ったら勝ち、勝率40%換算で
>>> 0.4*0.4*0.4
0.064

1位なら目的達成で2位ならもう一回遊べるドンという仕組み。ガチャ1回引くのに200枚, 20回参加して1,2位を1回以上取ればプラス。
うーん考えること結構あって単純にシュッとは計算できないにゃ…
(最近ガチャ渋すぎてガチャ券不足が深刻な問題にゃ…)

"""

import math
import typing

# 1回ガチャを引くのに必要なガチャ券の枚数
gacha_ticket_one: typing.Final[int] = 200

# 10回ガチャを引くのに必要なガチャ券の枚数
gacha_ticket_ten: typing.Final[int] = 1800

# 1回大会出場するのに必要なガチャ券の枚数
tournament_fee: typing.Final[int] = 10

# 雀士は5%の確率で獲得できる
atari: typing.Final[float] = 0.05

# 今回ピックアップ対象の雀士は9人


def main() -> None:
    """メイン関数."""
    print(f"1回ガチャを引くのに必要なガチャ券の枚数: {gacha_ticket_one}")
    print(f"10回ガチャを引くのに必要なガチャ券の枚数: {gacha_ticket_ten}")
    print(f"1回大会出場するのに必要なガチャ券の枚数: {tournament_fee}")
    print(f"27人大会で1位になる確率は約{top(0.33): 5f}です。")  # 3人麻雀で3回連続でトップを取る確率
    print(f"27人大会で1位か2位になる確率は約{top_and_2nd(0.33): 5f}です。")  # 3人麻雀で3回連続でトップを取る確率
    print(f"ガチャで当たる確率は約{atari: 5f}です。")
    return None


def top(rate: int = 0.33, last_rate: int = 0.33) -> float:
    """27人大会で1位になる確率.

    0.33^3
    =0.035937
    つまり、3人麻雀で3回連続でトップを取る確率は約3.59%です。
    """
    ret = rate * rate * rate
    return ret


def top_and_2nd(rate: int = 0.33, last_rate: int = 0.66) -> float:
    """27人大会で1位か2位になる確率.

    0.33*0.33*0.66=0.071874
    したがって、3人麻雀で3回連続でトップを取り、最後の回だけ1位か2位で良い場合の確率は約7.19%です。
    """
    ret = rate * rate * last_rate
    return ret


def yonma_top(rate: int = 0.5, last_rate: int = 0.33) -> float:
    """4人麻雀で1位or2位になる確率.

    0.5^4=0.0625
    つまり、4人麻雀で4回連続で1位または2位になる確率は6.25%です。
    """
    ret = rate * rate * rate * rate
    return ret


def yonma_top_or_2nd(rate: int = 0.5, last_rate: int = 0.25) -> float:
    """4人麻雀で1位or2位になる確率.

    0.5^4=0.0625
    つまり、4人麻雀で4回連続で1位または2位になる確率は6.25%です。
    """
    ret = rate * rate * rate * last_rate
    return ret


# 10回ガチャを引いてあたりが出る確率

if __name__ == "__main__":
    main()
