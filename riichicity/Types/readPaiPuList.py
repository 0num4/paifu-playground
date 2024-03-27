from pydantic import BaseModel


class ReadPaiPuListType1DataPlayer(BaseModel):
    identity: int
    isExistYiMan: bool
    nickname: str
    points: int
    rank: int
    roleID: int
    serial: int
    skinID: int
    userId: int


class ReadPaiPuListType1Data(BaseModel):
    endTime: int
    gamePlay: int
    isClear: bool
    isCollect: bool
    isMiddlePause: bool
    matchStage: int
    matchType: int
    paiPuId: str
    paiPuNotId: str
    period: int
    playerCount: int
    players: list[ReadPaiPuListType1DataPlayer]
    remark: str
    roomID: str
    round: int
    signItemID: int
    stageNum: int
    stageType: int


class ReadPaiPuListType1(BaseModel):
    code: int
    data: list[ReadPaiPuListType1Data]
    message: str
