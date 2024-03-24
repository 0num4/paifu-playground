from typing import Dict
from pydantic import BaseModel


# 友人戦の詳細のみ。一位率とかはフロントでやってる
class Data(BaseModel):
    addUpYiManCount: int
    beiManCount: int
    chiHuTotalCount: int
    chongCardList: Dict[str, int]
    chongFuLouCount: int
    chongLiZhiCount: int
    chongMoTingCount: int
    chongTotalCount: int
    chongTotalScore: int
    existFuLouCount: int
    existLiZhiCount: int
    fangList: Dict[str, int]
    firstTimes: int
    flowCount: int
    fourFangCount: int
    fourthTimes: int
    gameCount: int
    heFuLouCount: int
    heLiZhiCount: int
    heMoTingCount: int
    huCardList: Dict[str, int]
    huRoundTotal: int
    huTotalCount: int
    huTotalScore: int
    huangFuLouCount: int
    huangLiZhiCount: int
    huangMoTingCount: int
    keepLoseCount: int
    keepWinCount: int
    liZhiChiCount: int
    liZhiSuccessCount: int
    liZhiZiMoCount: int
    manGuanCount: int
    maxChongPoints: int
    maxDealerCount: int
    mingChiCount: int
    mingZiMoCount: int
    minusCount: int
    moTingHuCount: int
    oneFangCount: int
    qingChiCount: int
    qingZiMoCount: int
    round: int
    secondTimes: int
    thirdTimes: int
    threeBeiManCount: int
    threeFangCount: int
    tiaoManCount: int
    totalEndTimes: int
    twoFangCount: int
    yiFaTotalCount: int
    yiManCount: int
    ziMoCount: int


class UserDetailStatsV2Response(BaseModel):
    code: int
    data: list[Data]
    message: str


class CollectPaiPuResponse(BaseModel):
    code: int
    data: bool
    message: str


class GetGameDataResponse(BaseModel):
    code: int
    data: dict
    message: str


class UserBaseDataResponseData(BaseModel):
    headTag: int
    honorOpen: bool
    isBlock: bool
    isCanApply: bool
    isNewerCertificated: bool
    lastRankList: list[int]
    lastScoreList: list[int]
    maxHuAddUpYiMan: bool
    maxHuBashPoints: int
    maxHuCard: int
    maxHuFang: int
    maxHuFuLouList: list
    maxHuHandCards: list[int]
    maxHuPoints: int
    medal: bool
    model: int
    nickname: str
    paiFengDiDian: int
    paiFengFang: int
    paiFengFuLou: int
    paiFengGaoDian: int
    paiFengGong: int
    paiFengLiZhi: int
    paiFengMenQing: int
    paiFengMoTing: int
    profileFrameID: int
    rValue: int
    roleID: int
    skinID: int
    stageLevel: int
    stageNextPt: int
    stagePt: int
    titleID: int


class UserBaseDataResponse(BaseModel):
    code: int
    data: UserBaseDataResponseData
    message: str
