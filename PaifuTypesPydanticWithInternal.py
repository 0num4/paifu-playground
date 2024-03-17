from typing import Literal, Union
import pydantic
import PaifuTypeInternalPydantic


class HandEventRecord(pydantic.BaseModel):
    data: Union[
        PaifuTypeInternalPydantic.HandInfo,  # hand_cards
        PaifuTypeInternalPydantic.OperationInfo,  # in_card
        PaifuTypeInternalPydantic.ActionInfo,  # action
        PaifuTypeInternalPydantic.OutCardInfo,  # out_card
        PaifuTypeInternalPydantic.GameResult,  # end_type
        PaifuTypeInternalPydantic.GameInfo,  # user_data
        PaifuTypeInternalPydantic.IsAutoGangInfo,  # user_id & is_auto_gang
        ]
    eventPos: int
    eventType: int
    handId: str
    startTime: int
    userId: int


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
    userId: int


class HandRecord(pydantic.BaseModel):
    benChangNum: int
    changCi: int
    handCardEncode: str
    handCardsSHA256: str
    handEventRecord: list[HandEventRecord]
    handID: str
    handPos: int
    paiShan: list[int]
    players: list[Player]
    quanFeng: int


class PaifuData(pydantic.BaseModel):
    fangFu: int
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
    keyValue: str
    matchStage: int
    matchType: int
    northOperateType: int
    nowTime: int
    period: int
    playerCount: Literal[2, 3, 4]
    remark: str
    roomId: str
    round: int
    stageNum: int
    stageType: int


class Paifu(pydantic.BaseModel):
    code: int
    data: PaifuData
    message: str  # ok
