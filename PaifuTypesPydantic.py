from typing import List, Literal
import pydantic


class HandEventRecord(pydantic.BaseModel):
    data: str
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
    handEventRecord: List[HandEventRecord]
    handID: str
    handPos: int
    paiShan: List[int]
    players: List[Player]
    quanFeng: int


class PaifuData(pydantic.BaseModel):
    fangFu: int
    gamePlay: int
    handRecord: List[HandRecord]
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

    class Config:
        extra = "forbid"
        validate_assignment = True
        strict = True
