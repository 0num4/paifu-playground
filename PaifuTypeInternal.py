from typing import TypedDict, Optional, Union


class UserInfo(TypedDict):
    user_id: int
    hand_points: int
    luck_score: int
    is_exist_shao_ji: bool
    room_exist_man_guan: bool


class HandInfo(TypedDict):
    hand_cards: list[int]  # 最大14
    dealer_pos: int
    dices: list[int]
    bao_pai_card: int
    ting_list: list[dict]
    quan_feng: int
    chang_ci: int
    ben_chang_num: int
    li_zhi_bang_num: int
    user_info_list: list[UserInfo]
    hand_cards_sha_256: str


class OperationInfo(TypedDict):
    in_card: Optional[int]
    is_zi_mo: bool
    gang_cards: list[int]
    bu_gang_cards: list[int]
    is_gang_incard: bool
    is_can_lizhi: bool
    oper_fixed_time: int
    oper_var_time: int
    in_ting_info: list[dict]
    is_nine_cards: bool
    is_kai_li_zhi: bool
    is_pull_north: bool
    is_first_xun_in: bool


class ActionInfo(TypedDict):
    action: int
    card: int
    move_cards_pos: list[int]
    user_id: int
    hand_cards: Optional[list[int]]
    group_cards: Optional[list[int]]
    is_li_zhi: bool
    li_zhi_operate: int
    li_zhi_type: int


class OutCardInfo(TypedDict):
    out_card: int
    action_list: list[int]
    oper_fixed_time: int
    oper_var_time: int


class WinInfo(TypedDict):
    fang_info: list[dict[str, int]]
    all_fang_num: int
    all_fu: int
    all_point: int
    user_cards: list[int]
    li_bao_card: Optional[list[int]]
    user_id: int
    ting_card_list: Optional[list[int]]
    bash_points: int
    luck_score: int


class UserProfit(TypedDict):
    user_id: int
    point_profit: int
    li_zhi_profit: int
    is_bao_pai: bool
    user_point: int


class GameResult(TypedDict):
    end_type: int
    win_info: list[WinInfo]
    user_profit: list[UserProfit]
    zhong_liu_info: list[dict]
    cheat_info_list: list[dict]


class UserData(TypedDict):
    user_id: int
    point_num: int
    score: int
    coin: int
    rate_value: int
    pt_value: int
    user_pt_value: int
    next_pt_value: int
    last_user_pt: int
    last_next_pt: int
    is_shao_ji: bool
    shao_ji_score: int
    luck_score: int
    StageLevel: int


class GameInfo(TypedDict):
    user_data: list[UserData]
    pai_pu_id: str
    is_exist_room: bool
