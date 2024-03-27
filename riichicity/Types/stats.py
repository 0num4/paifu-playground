from pydantic import BaseModel
from typing import Any


# 友人戦の詳細のみ。一位率とかはフロントでやってる
class Data(BaseModel):
    addUpYiManCount: int
    beiManCount: int
    chiHuTotalCount: int
    chongCardList: dict[str, int]
    chongFuLouCount: int
    chongLiZhiCount: int
    chongMoTingCount: int
    chongTotalCount: int
    chongTotalScore: int
    existFuLouCount: int
    existLiZhiCount: int
    fangList: dict[str, int]
    firstTimes: int
    flowCount: int
    fourFangCount: int
    fourthTimes: int
    gameCount: int
    heFuLouCount: int
    heLiZhiCount: int
    heMoTingCount: int
    huCardList: dict[str, int]
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


class FavorRole(BaseModel):
    cultivateStatus: int
    feelValue: int
    model: int
    oathValue: int
    roleId: int
    skinId: int


class Collect(BaseModel):
    equipCount: int
    roleCount: int
    skinCount: int
    titleCount: int


class HighLightHu(BaseModel):
    benChangShu: int
    changCi: int
    custom: bool
    fangList: list[int]
    handId: str
    isExistYiMan: bool
    maxHuBashPoints: int
    maxHuCard: int
    maxHuFang: int
    maxHuFuLouList: list
    maxHuHandCards: list[int]
    maxHuPoints: int
    paipuId: str
    quanFeng: int


class UserBriefData(BaseModel):
    certificated: bool
    championNum: int
    collect: Collect
    favorRoleList: list[FavorRole]
    fourPt: int
    fourStage: int
    highLightHu: HighLightHu
    isBlock: bool
    isCanApply: bool
    model: int
    nickname: str
    profileFrameID: int
    roleID: int
    sign: str
    skinID: int
    threePT: int
    threeStage: int
    titleID: int
    userID: int


class UserBriefResponse(BaseModel):
    code: int
    data: UserBriefData
    message: str


class EmailLoginResponseDataUser(BaseModel):
    avatar: str
    email: str
    id: int
    nickname: str
    registerAt: int
    status: int


class EmailLoginResponseData(BaseModel):
    banStartAt: int
    banUntil: int
    cancelContactEmail: str
    cancelEndAt: int
    country: str
    honorRed: bool
    init: bool
    ipCountry: str  # CountryCode
    isCompleteCourse: bool
    isCompleteGive: bool
    isCompleteNew: bool
    isCompleteNewRole: bool
    loginQueue: list[Any]
    serverTime: int
    tokenTypes: list[int]
    user: EmailLoginResponseDataUser
    violationAction: int


class EmailLoginResponse(BaseModel):
    code: int
    data: EmailLoginResponseData
    message: str


class Award(BaseModel):
    category: int
    count: int
    isEquip: bool
    itemId: int


class CollectTaskAwardResponse(BaseModel):
    awards: list[Award]
    boxAwards: list[Any]
    code: int
    message: str


class collectTaskAwardRequest(BaseModel):
    typelist: list[int]


class DiscountBag(BaseModel):
    pass


class ProductList(BaseModel):
    currencyID: int
    currencyNum: int
    discount: int
    discountBag: list[DiscountBag]
    exchangeLeft: int
    iconType: int
    isExchangeLimit: bool
    isLimit: bool
    itemID: int
    labelType: int
    leftTime: int
    num: int
    productID: int
    productPrice: int
    productSKU: str
    secondLabel: int


class GetProductListResponseData(BaseModel):
    firstLabel: int
    isExistSkin: bool
    isFirstBag: bool
    isShowDouble: bool
    leftFreeTimes: int
    leftTime: int
    productList: list[ProductList]
    refreshItemID: int
    refreshItemNum: int
    secondLabel: int
    skinLabels: list[int]
    storeActivity: int
    version: int
    versionNotify: bool


class GetProductListResponse(BaseModel):
    code: int
    data: GetProductListResponseData
    message: str


class GiftContent(BaseModel):
    pass


class StoreBuyProductResponseData(BaseModel):
    createTime: int
    expiredAt: int
    feelValue: int
    giftContent: list[GiftContent]
    isCanEquip: bool
    isEquip: bool
    isExpired: bool
    isLock: bool
    itemID: int
    itemType: int
    label: int
    name: str
    num: int
    recycleNum: int
    source: int


class StoreBuyProductResponse(BaseModel):
    code: int
    data: list[StoreBuyProductResponseData]
    message: str
