import datetime
import json
from typing import Annotated, Literal, Optional, TypeAlias, Union

import boto3.dynamodb.types
import pydantic

import PaifuTypesPydantic
import riichicity.Types.commonConsts

UserIdType: TypeAlias = Annotated[int, pydantic.Field(strict=True, ge=100000000, le=999999999)]


class UserInfo(pydantic.BaseModel):
    user_id: int
    hand_points: int
    luck_score: int
    is_exist_shao_ji: bool
    room_exist_man_guan: bool


class HandInfo(pydantic.BaseModel):
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


class OperationInfo(pydantic.BaseModel):
    in_card: Optional[int]
    is_zi_mo: bool  # 上がれる状態の手かどうか
    gang_cards: list[int]  # ほぼ0
    bu_gang_cards: list[int]  # ほぼ0
    is_gang_incard: bool
    is_can_lizhi: bool
    oper_fixed_time: Literal[5]  # ほぼ5秒固定
    oper_var_time: Literal[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]  # 20+5秒だと思うけど12が謎
    in_ting_info: list[dict]  # 鳴くとそれ以降一生データが入るので
    is_nine_cards: bool
    is_kai_li_zhi: bool
    is_pull_north: bool
    is_first_xun_in: bool


class ActionInfo(pydantic.BaseModel):
    action: riichicity.Types.commonConsts.EMjActionType2
    card: int
    move_cards_pos: Optional[
        list[int]
    ]  # だいたい[int, int]。北抜きの場合は手配の左からどこを抜いたか。普通の打牌の場合は[手配の左からどこを捨てたか,ツモ牌をどこにいれるか]
    user_id: int
    hand_cards: Optional[list[int]]
    group_cards: Optional[list[int]]
    is_li_zhi: bool
    li_zhi_operate: int
    li_zhi_type: int


class OutCardInfo(pydantic.BaseModel):
    out_card: int
    action_list: list[int]
    oper_fixed_time: int
    oper_var_time: int


class WinInfo(pydantic.BaseModel):
    fang_info: Optional[list[dict[str, int]]]
    all_fang_num: int
    all_fu: int
    all_point: int
    user_cards: list[int]
    li_bao_card: Optional[list[int]]
    user_id: int
    ting_card_list: Optional[list[int]]
    bash_points: int
    luck_score: int


class UserProfit(pydantic.BaseModel):
    user_id: int
    point_profit: int
    li_zhi_profit: int
    is_bao_pai: bool
    user_point: int


class GameResult(pydantic.BaseModel):
    end_type: int  # 8は友人線で途中終了
    win_info: list[WinInfo]
    user_profit: list[UserProfit]
    zhong_liu_info: list[dict]
    cheat_info_list: list[dict]


class UserData(pydantic.BaseModel):
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


class IsAutoGangInfo(pydantic.BaseModel):
    user_id: int
    is_auto_gang: bool


class TingInfoInternal(pydantic.BaseModel):
    is_zhen_ting: bool
    is_wu_yi: bool
    left_num: int
    ting_card: int
    is_yi_man: bool
    fang_info: dict[str, int]
    ting_type: int


class TingInfo(pydantic.BaseModel):
    ting_info: list[TingInfoInternal]


class CardInfo(pydantic.BaseModel):
    cards: list[int] | None


class GameInfo(pydantic.BaseModel):
    user_data: list[UserData]
    pai_pu_id: str
    is_exist_room: bool


HandEventRecordDataLiteral: TypeAlias = Union[
    HandInfo,  # hand_cards
    OperationInfo,  # in_card
    ActionInfo,  # action
    OutCardInfo,  # out_card
    GameResult,  # end_type
    GameInfo,  # user_data
    UserInfo,
    IsAutoGangInfo,  # user_id & is_auto_gang
    TingInfo,  # ting_info
    CardInfo,
]


class HandEventRecord(pydantic.BaseModel):
    data: HandEventRecordDataLiteral
    eventPos: int
    eventType: riichicity.Types.commonConsts.EMjReplayEventType2
    handId: str
    startTime: int
    userId: UserIdType


class Player(pydantic.BaseModel):
    cardBackID: int
    gameMusicId: int
    headTag: int
    identity: int
    matchMusicId: int
    model: int
    nickname: str
    points: int
    position: int
    profileFrameId: int
    riichiEffectID: int
    riichiMusicId: int
    riichiStickID: int
    roleID: int
    skinID: int
    specialEffectID: int
    tableclothID: int
    titleID: int
    userId: UserIdType


class HandRecord(pydantic.BaseModel):
    benChangNum: int  # 0始まり。8連荘までなので普通は0-7
    changCi: Literal[1, 2, 3, 4]  # 3人麻雀の場合は1, 2, 3
    handCardEncode: PaifuTypesPydantic.handCardEncodeType  # その局の牌山
    handCardsSHA256: PaifuTypesPydantic.handCardsSHA256Type
    handEventRecord: list[HandEventRecord]
    handID: str
    handPos: int
    paiShan: list[int]
    players: list[Player]
    quanFeng: int


class PaifuData(pydantic.BaseModel):
    fangFu: riichicity.Types.commonConsts.EMFanFuType2
    gamePlay: int
    handRecord: list[HandRecord]
    initPoints: int
    isCollect: bool
    isGangPay: bool
    isGeMu: bool
    isKaiLiZhi: bool
    isLuck: bool
    isNotEffect: bool
    isNotShowHand: bool
    isObserve: bool
    isShaoJi: bool
    isWithUser: bool
    keyValue: Annotated[str, pydantic.Field(pattern=r"^[0-9a-z]{20}$")]
    matchStage: int
    matchType: int
    northOperateType: int
    nowTime: datetime.date
    period: int
    playerCount: Literal[2, 3, 4]
    remark: str
    roomId: str
    round: Literal[1, 2]
    stageNum: int
    stageType: int


class Paifu(pydantic.BaseModel):
    code: int
    data: PaifuData
    message: str  # ok


# deserializer = boto3.dynamodb.types.TypeDeserializer()


def deserialize_number(number: str) -> int:
    return int(number)


# setattr(deserializer, "N", deserialize_number)
setattr(boto3.dynamodb.types.TypeDeserializer, "_deserialize_n", lambda _, number: deserialize_number(number))


# def assignDictToHandEventRecordDataLiteral(handEventRecord: dict) -> HandEventRecordDataLiteral:
def parse_hand_record(hand_record: PaifuTypesPydantic.HandRecord) -> list[any]:
    HandRecordAdapter = pydantic.TypeAdapter(PaifuTypesPydantic.HandRecord)
    hand_record = HandRecordAdapter.validate_python(hand_record)
    # hand_info_list = []
    # operation_info_list = []
    # action_info_list = []
    # out_card_info_list = []
    # game_result_list = []
    # game_info_list = []
    # user_info_list = []
    # is_auto_gang_info_list = []
    # ting_info_list = []

    for hand_event_record in hand_record.handEventRecord:
        # print(f"hand_event_record.eventType {hand_event_record.eventType}")
        # continue
        # if hand_event_record.userId == 813942315:
        #     event_data_str: str = hand_event_record.data
        #     event_data = json.loads(event_data_str)
        #     print(event_data)
        # else:
        #     continue
        # continue
        # print(hand_event_record)
        event_data_str: str = hand_event_record.data
        event_data = json.loads(event_data_str)
        print(event_data)
        ada = pydantic.TypeAdapter(HandEventRecordDataLiteral)
        s = ada.validate_python(event_data)
        if isinstance(s, ActionInfo):
            # print("OperationInfo")
            # print(s.user_id)
            # print(s.hand_cards)
            # print(s.group_cards)
            continue
            # elif isinstance(s, PaifuTypesPydanticWithInternal.HandInfo):
            #     print("HandInfo")
            # continue
        continue
        if isinstance(s, HandInfo):
            print("HandInfo")
            # print(s)
            # playerid,hand_cardsだけでい
        elif isinstance(s, OperationInfo):
            print("OperationInfo")
        elif isinstance(s, ActionInfo):
            print("ActionInfo")
        elif isinstance(s, OutCardInfo):
            print("OutCardInfo")
        elif isinstance(s, GameResult):
            print("GameResult")
        elif isinstance(s, GameInfo):
            print("GameInfo")
        elif isinstance(s, UserInfo):
            print("UserInfo")
        elif isinstance(s, IsAutoGangInfo):
            print("IsAutoGangInfo")
        elif isinstance(s, TingInfo):
            print("TingInfo")
        elif isinstance(s, CardInfo):
            print("CardInfo")
