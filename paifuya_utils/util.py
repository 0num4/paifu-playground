
import enum


class dan(enum.IntEnum):
    士 = 6
    傑 = 7
    豪 = 8
    聖 = 9
    天 = 10
    魂 = 11

d = ["士", "傑", "豪", "聖", "天", "魂"]
p = {301: 6, 302: 7, 303: 10, 401: 14, 402: 16, 403: 18, 501: 20, 502: 30, 503: 45}
level_dan = lambda level: f"{d[level // 100 % 100 - 2]}{level % 100}"
level_pt_base = lambda level: 5000 if level // 100 % 100 >= 6 else p[level % 1000] * 100


# @markdown ####・細かい設定
def parse_dan(level: int):
    """それぞれのlevelの段位に対応する昇段ptを返す
    levelはint型で、100の位が段位、1の位が段位内のレベルを表す
    Args:
        level (int): レベル。牌譜屋から帰ってくる値
    Returns:
        int: 昇段pt
    """
    return f"{d[level // 100 % 100 - 2]}{level % 100}"


def parse_pt_base(level: int) -> int:
    """それぞれのlevelの段位に対応する昇段ptを返す
    levelはint型で、100の位が段位、1の位が段位内のレベルを表す
    Args:
        level (int): レベル。牌譜屋から帰ってくる値
    Returns:
        int: 昇段pt
    """
    return 5000 if level // 100 % 100 >= 6 else p[level % 1000] * 100


if __name__ == "__main__":
    # print(parse_dan(301))
    # print(parse_dan(302))
    # print(parse_dan(303))
    # print(parse_dan(401))
    # print(parse_dan(402))
    # print(parse_dan(403))
    print(parse_dan(501))
    # print(parse_dan(502))
    # print(parse_dan(503))
    # print(parse_pt_base(301))
    # print(parse_pt_base(302))
    # print(parse_pt_base(303))
    # print(parse_pt_base(401))
    # print(parse_pt_base(402))