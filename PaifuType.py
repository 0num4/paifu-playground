from typing import TypedDict, Literal


class HandEventRecord(TypedDict):
    data: str
    eventPos: int
    eventType: int
    handId: str
    startTime: int
    userId: int


class Player(TypedDict):
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


class HandRecord(TypedDict):
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


class PaifuData(TypedDict):
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


class Paifu(TypedDict):
    code: int
    data: PaifuData
    message: str  # ok
