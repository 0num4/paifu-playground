from typing import Literal, Annotated
import typing
import pydantic
import datetime

KeyValueType: typing.TypeAlias = typing.Annotated[str, pydantic.StringConstraints(pattern=r"^cn[0-9a-f]{18}$")]
benChangNumType: typing.TypeAlias = typing.Annotated[int, pydantic.Field(strict=True, ge=0, le=4)]


class HandEventRecord(pydantic.BaseModel):
    data: str
    eventPos: int  # eventのindex。0始まり
    eventType: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # EMjReplayEventType, HandInfoなどのtype
    handId: str  # だいたい空。謎。まじでいらん
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
    benChangNum: benChangNumType
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
    keyValue: KeyValueType
    matchStage: int
    matchType: int
    northOperateType: int
    nowTime: datetime.date
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
