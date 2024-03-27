from typing import Literal, Annotated
import typing
import pydantic
import riichicity.Types.commonConsts
import datetime

KeyValueType: typing.TypeAlias = typing.Annotated[str, pydantic.StringConstraints(pattern=r"^cn[0-9a-f]{18}$")]
benChangNumType: typing.TypeAlias = typing.Annotated[int, pydantic.Field(strict=True, ge=0, le=4)]
UserIdType: typing.TypeAlias = Annotated[int, pydantic.Field(strict=True, ge=100000000, le=999999999)]
eventTypeType: typing.TypeAlias = Annotated[int, pydantic.Field(strict=True, ge=1, le=11)]
handCardEncodeType: typing.TypeAlias = Annotated[str, pydantic.Field(strict=True, pattern=r"^[0-9mpsz]*$")]
handCardsSHA256Type: typing.TypeAlias = Annotated[str, pydantic.Field(strict=True, pattern=r"^[a-z\d]{64}$")]


class HandEventRecord(pydantic.BaseModel):
    data: str
    eventPos: int  # eventのindex。0始まり
    eventType: eventTypeType
    handId: str  # だいたい空。謎。まじでいらん
    startTime: int
    userId: UserIdType | Literal[0]  # eventTypeが5のときだけ0がある


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
    handCardEncode: handCardEncodeType  # 256文字にならないことがある
    handCardsSHA256: handCardsSHA256Type
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
