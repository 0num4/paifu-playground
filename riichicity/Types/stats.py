import typing
from pydantic import BaseModel, Field
from . import consts
from . import commonConsts


# 友人戦の詳細のみ。一位率とかはフロントでやってる
class UserDetailStatsV2ResponseData(BaseModel):
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
    data: list[UserDetailStatsV2ResponseData]
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


class EmailLoginResponseDataLoginQueue(BaseModel):
    wait_token: str = Field(..., description="待ちトークン")
    wait_cnt: int = Field(..., description="待ち人数")
    wait_rank: int = Field(..., description="待ち順位")
    check_interval: int = Field(..., description="チェック間隔の秒数")


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
    loginQueue: list[EmailLoginResponseDataLoginQueue | None]
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
    boxAwards: list[typing.Any]
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


class StoreBuyProductResponseGiftContent(BaseModel):
    pass


class StoreBuyProductResponseData(BaseModel):
    createTime: int
    expiredAt: int
    feelValue: int
    giftContent: list[StoreBuyProductResponseGiftContent]
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
    data: typing.Optional[list[StoreBuyProductResponseData]]
    message: str


class Award(BaseModel):
    itemID: int
    itemModule: int
    itemType: int
    num: int


class RankAwardList(BaseModel):
    awardList: list[Award]
    maxRank: int
    minRank: int


class PenaltyInfo(BaseModel):
    num: int
    pointsCount: int


class ReadOfficialMatchResponseDataRule(BaseModel):
    CardType: int
    ChangBang: int
    FangFu: int
    IsAutoLi: bool
    IsChangBang: bool
    IsChiDuan: bool
    IsChiTi: bool
    IsFirstNotRand: bool
    IsGeMu: bool
    IsJinChiTi: bool
    IsKaiLiZhi: bool
    IsLastHeEnd: bool
    IsLastTingEnd: bool
    IsNotCompound: bool
    IsNotEffect: bool
    IsNotGrabNorth: bool
    IsNotHandFondle: bool
    IsNotKeepDealer: bool
    IsNotShowHand: bool
    IsOpenFace: bool
    IsOpenVoice: bool
    IsShaoJi: bool
    IsTimeLimit: bool
    LimitTime: int
    NorthOperateType: int
    ShaoJiPoint: int
    ThreeZiMoType: int
    TimeLimitType: int
    fristReqPoints: int
    initialPoints: int
    isAddUpYakuman: bool
    isBoxStick: bool
    isConvenientTips: bool
    isCutOff: bool
    isEightContinuous: bool
    isFourGang: bool
    isFourGangPass: bool
    isFourRiichi: bool
    isFourRiichiPass: bool
    isFourWinds: bool
    isFourWindsPass: bool
    isGangDora: bool
    isGangLiDora: bool
    isGangOpen: bool
    isGangPay: bool
    isKnock: bool
    isLiDora: bool
    isLuck: bool
    isMinusRiichi: bool
    isMultipleYakuman: bool
    isNanXiRu: bool
    isNineCards: bool
    isNineCardsPass: bool
    isOpenRiichi: bool
    isPayYakuman: bool
    isQiangGang: bool
    isQieShang: bool
    isRenHe: bool
    isSameOrder: bool
    isTailContinue: bool
    isThreeHe: bool
    isThreeHePass: bool
    isTingPrompt: bool
    isTopReward: bool
    isYiFa: bool
    lianFeng: int
    luckRate: int
    minimumPoints: int
    numRedCard: int
    operFixedTime: int
    operVarTime: int
    orderPoints: list[int]
    orderPtValue: list[typing.Any]
    penaltyInfo: list[PenaltyInfo]
    playerCount: int
    round: int


class ReadOfficialMatchResponseData(BaseModel):
    isSign: bool
    matchJoinNum: int
    matchStage: int
    name: str
    officialID: str
    qualifiedNum: int
    rankAwardList: list[RankAwardList]
    rule: ReadOfficialMatchResponseDataRule
    signItemID: int
    signItemNum: int
    signNum: int
    totalJoinNum: int


class UserInfo(BaseModel):
    timingStart: int


class ReadOfficialMatchResponse(BaseModel):
    code: int
    data: list[ReadOfficialMatchResponseData]
    message: str
    userInfo: UserInfo


class ReadyOfficialNextResponse(BaseModel):
    code: int
    data: bool
    message: str


class ReadTimingMatchRankAward(BaseModel):
    itemID: int
    itemModule: int
    itemType: int
    num: int


class ReadTimingMatchRankAwardList(BaseModel):
    awardList: list[ReadTimingMatchRankAward]
    maxRank: int
    minRank: int


class ReadTimingMatchSignItemList(BaseModel):
    itemID: int
    itemModule: int
    itemType: int
    num: int


class ReadTimingMatchResponseData(BaseModel):
    isSign: bool
    label: int
    matchJoinNum: int
    matchStage: int
    officialID: str
    period: int
    playerCount: int
    qualifiedNum: int
    rankAwardList: list[ReadTimingMatchRankAwardList]
    signItemList: list[ReadTimingMatchSignItemList]
    signNum: int
    signTimes: int
    signUpEndTime: int
    signUpStartTime: int
    startTime: int


class ReadTimingMatchResponse(BaseModel):
    code: int
    data: list[ReadTimingMatchResponseData]
    message: str


class SignOfficialMatchResponseData(BaseModel):
    signNum: int
    totalJoinNum: int


class SignOfficialMatchResponse(BaseModel):
    code: int
    data: SignOfficialMatchResponseData
    message: str


class SignTimingMatchResponseData(BaseModel):
    signCount: int
    signTimes: int


class SignTimingMatchResponse(BaseModel):
    code: int
    data: SignTimingMatchResponseData
    message: str


class MessageReceiveAward(BaseModel):
    category: int
    count: int
    expireTime: int
    itemId: int


class MessageReceiveAwardResponse(BaseModel):
    awards: list[MessageReceiveAward]
    code: int
    message: str


class LobbysReadStageClassifiesResponseData(BaseModel):
    highRank: int
    id: str
    isLock: bool
    lowCoins: int
    lowRank: int
    lowRate: dict[str, int] = {}
    onlinePlayers: int
    playerCount: int
    round: int
    stageType: int


class LobbysReadStageClassifiesResponseUserInfoStage(BaseModel):
    isRedDot: bool
    rValue: int
    stageLevel: int
    stageNextPt: int
    stagePt: int
    timingStart: int


class LobbysReadStageClassifiesResponseUserInfo(BaseModel):
    player_3: LobbysReadStageClassifiesResponseUserInfoStage = Field(None, alias="3")
    player_4: LobbysReadStageClassifiesResponseUserInfoStage = Field(None, alias="4")


class LobbysReadStageClassifiesResponse(BaseModel):
    code: int
    data: list[LobbysReadStageClassifiesResponseData]
    message: str
    userInfo: LobbysReadStageClassifiesResponseUserInfo


class EXTeamDailyAwardResponseDataAward(BaseModel):
    category: int
    count: int
    isEquip: bool
    itemId: int


class EXTeamDailyAwardResponseDataAwardPageUser(BaseModel):
    exp: int
    level: int
    levelExp: int
    title: int
    userId: int


class EXTeamDailyAwardResponseDataAwardPage(BaseModel):
    dailyAwardRed: bool
    giftRed: bool
    guessRed: bool
    matchRed: bool
    storeRed: bool
    taskRed: bool
    user: EXTeamDailyAwardResponseDataAwardPageUser


class EXTeamDailyAwardResponseData(BaseModel):
    awards: list[EXTeamDailyAwardResponseDataAward]
    page: EXTeamDailyAwardResponseDataAwardPage


class EXTeamDailyAwardResponse(BaseModel):
    code: int
    data: EXTeamDailyAwardResponseData
    message: str


class EXTeamTaskResponseDataTaskAward(BaseModel):
    category: int
    count: int
    isEquip: bool
    itemId: int


class EXTeamTaskResponseDataTask(BaseModel):
    action: int
    award: list[EXTeamTaskResponseDataTaskAward]
    awardTimes: int
    id: int
    status: int
    times: int


class EXTeamTaskResponseData(BaseModel):
    monthly: list[EXTeamTaskResponseDataTask]
    week: list[EXTeamTaskResponseDataTask]


class EXTeamTaskResponse(BaseModel):
    code: int
    data: EXTeamTaskResponseData
    message: str


class ActivityReadRanksResponseDataItem(BaseModel):
    alphaValue: int
    level: int
    model: int
    nickname: str
    profileFrameID: int
    rank: int
    roleID: int
    skinID: int
    titleID: int
    userID: int
    value: int


class ActivityReadRanksResponseData(BaseModel):
    items: list[ActivityReadRanksResponseDataItem]
    kind: int
    scopeValue: int
    selfItem: ActivityReadRanksResponseDataItem
    totalCount: int


class ActivityReadRanksResponse(BaseModel):
    code: int
    data: ActivityReadRanksResponseData
    message: str


class ActivityActivityListResponseDataActivitySignActivityListPersistentAwardListAward(BaseModel):
    category: int
    count: int
    isEquip: bool
    itemId: int


class ActivityActivityListResponseDataActivitySignActivityListPersistentAwardList(BaseModel):
    awardList: list[ActivityActivityListResponseDataActivitySignActivityListPersistentAwardListAward]
    days: int
    stage: int


class ActivityActivityListResponseDataActivitySignActivityListSignResult(BaseModel):
    isVip: bool
    persistentDay: int
    persistentStatusList: list[int]
    repairLeft: int
    signDay: int
    signStatusList: list[int]
    vipStatus: int


class ActivityActivityListResponseDataActivitySignActivityList(BaseModel):
    persistentAwardList: list[ActivityActivityListResponseDataActivitySignActivityListPersistentAwardList]
    persistentAwardType: int
    signAwardList: list[ActivityActivityListResponseDataActivitySignActivityListPersistentAwardListAward]
    signResult: ActivityActivityListResponseDataActivitySignActivityListSignResult
    vipAwardList: list[ActivityActivityListResponseDataActivitySignActivityListPersistentAwardListAward]


class ActivityActivityListResponseDataActivity(BaseModel):
    activityId: int
    activityType: (
        consts.ActivityType | int
    )  # 基本的にはActivityTypeなんだがactivity/activityListは全部返すので新しいのが来るときもあるので
    award: list[ActivityActivityListResponseDataActivitySignActivityListPersistentAwardListAward]
    currentTime: int
    describe: str
    endTime: int
    inviteActivity: list
    isNew: bool
    pop: bool
    popUpLocation: int
    popUpType: int
    priority: int
    receiveEndTime: int
    receiveStartTime: int
    redPoint: bool
    returnActivity: list
    sBtlActivity: list
    signActivityList: list[ActivityActivityListResponseDataActivitySignActivityList]
    startTime: int
    title: str


class ActivityActivityListResponseData(BaseModel):
    list: list[ActivityActivityListResponseDataActivity]


class ActivityActivityListResponse(BaseModel):
    code: int
    data: ActivityActivityListResponseData
    message: str


class BackpackUserItemListResponseUserItemGiftContent(BaseModel):
    pass


class BackpackUserItemListResponseUserItem(BaseModel):
    createTime: int
    expiredAt: int
    feelValue: int
    giftContent: list[BackpackUserItemListResponseUserItemGiftContent]
    isCanEquip: bool
    isEquip: bool
    isExpired: bool
    isLock: bool
    itemID: consts.EnumDefine.ItemID | int
    itemType: consts.EnumDefine.ItemType
    label: int
    name: str
    num: int
    recycleNum: int
    source: int


class BackpackUserItemListResponse(BaseModel):
    code: int
    data: list[BackpackUserItemListResponseUserItem]
    message: str


class ActivityViewActionResponse(BaseModel):
    code: int
    message: str


class BackpackRecycleGiftResponse(BaseModel):
    code: int
    data: bool
    message: str


class GetGiftCodeResponseAward(BaseModel):
    category: int
    count: int
    isEquip: bool
    itemId: int


class GetGiftCodeResponse(BaseModel):
    awards: list[GetGiftCodeResponseAward]
    code: int
    message: str


class FrendMatchRule(BaseModel):
    FangFu: commonConsts.EMFanFuType2 = Field(...)
    IsAdvancedOptions: bool = Field(...)
    IsChiDuan: bool = Field(...)
    IsConvenientTips: bool = Field(...)
    IsGeMu: bool = Field(...)
    IsKaiLiZhi: bool = Field(...)
    IsLuck: bool = Field(...)
    IsMinusRiichi: bool = Field(...)
    IsMoreoptions: bool = Field(...)
    IsNanXiRu: bool = Field(...)
    IsNotEffect: bool = Field(...)
    IsNotShowHand: bool = Field(...)
    IsOpenVoice: bool = Field(...)
    IsRandSeat: bool = Field(...)
    IsShaoJi: bool = Field(...)
    RoomType: int = Field(...)
    ThreeZiMoType: int = Field(...)
    changBang: str = Field(...)
    fristReqPoints: int = Field(...)
    initialPoints: int = Field(...)
    isKnock: bool = Field(...)
    isTopReward: bool = Field(...)
    minimumPoints: int = Field(...)
    numRedCard: int = Field(...)
    operFixedTime: int = Field(...)
    operVarTime: int = Field(...)
    orderPoints: list[int] = Field(...)
    playerCount: int = Field(...)
    round: int = Field(...)


class lobbysCreateFriendMatchResponse(BaseModel):
    code: int
    data: str  # TODO: 6桁の数字の文字列
    message: str


class EnterFriendMatchResponseDataPlayerStageLevel(BaseModel):
    level_3: int = Field(..., alias="3")
    level_4: int = Field(..., alias="4")


class EnterFriendMatchResponseDataPlayer(BaseModel):
    identity: int
    isOwner: bool
    location: int
    model: int
    nickName: str
    roleId: int
    sequence: int
    skinId: int
    stageLevel: EnterFriendMatchResponseDataPlayerStageLevel
    status: int
    titleID: int
    userID: int


class EnterFriendMatchResponseDataRule(BaseModel):
    CardType: int
    FangFu: int
    IsAdvancedOptions: bool
    IsAutoLi: bool
    IsChiDuan: bool
    IsConvenientTips: bool
    IsGeMu: bool
    IsKaiLiZhi: bool
    IsLuck: bool
    IsMinusRiichi: bool
    IsMoreoptions: bool
    IsNanXiRu: bool
    IsNotEffect: bool
    IsNotShowHand: bool
    IsOpenVoice: bool
    IsRandSeat: bool
    IsShaoJi: bool
    RoomType: int
    ShaoJiPoint: int
    ThreeZiMoType: int
    UpdateTime: int
    changBang: int
    fristReqPoints: int
    initialPoints: int
    isKnock: bool
    isTopReward: bool
    minimumPoints: int
    numRedCard: int
    operFixedTime: int
    operVarTime: int
    orderPoints: list[int]
    playerCount: int
    round: int


class EnterFriendMatchResponseData(BaseModel):
    Id: str
    createAt: int
    players: list[EnterFriendMatchResponseDataPlayer]
    roomNum: str
    rule: EnterFriendMatchResponseDataRule


class EnterFriendMatchResponse(BaseModel):
    code: int
    data: EnterFriendMatchResponseData
    message: str


class lobbysFriendPlayerActionResponse(BaseModel):
    code: int
    message: str


class lobbysReadPublicRoomResponseUser(BaseModel):
    avatar: str
    email: str
    id: int
    nickname: str
    registerAt: int
    status: int


class lobbysReadPublicRoomResponseLoginResponse(BaseModel):
    banStartAt: int
    banUntil: int
    cancelContactEmail: str
    cancelEndAt: int
    country: str
    honorRed: bool
    init: bool
    ipCountry: str
    isCompleteCourse: bool
    isCompleteGive: bool
    isCompleteNew: bool
    isCompleteNewRole: bool
    loginQueue: list[typing.Any]
    serverTime: int
    tokenTypes: list[int]
    user: lobbysReadPublicRoomResponseUser
    violationAction: int


class lobbysReadPublicRoomResponseRoomListResponseRoom(BaseModel):
    Id: str
    IsGeMu: bool
    isLuck: bool
    isShaoJi: bool
    ownerId: int
    ownerName: str
    playerCount: int
    roomNum: str
    roomPlayerCount: int
    round: int
    updateTime: int


class lobbysReadPublicRoomResponseRoomListResponse(BaseModel):
    list: list[lobbysReadPublicRoomResponseRoomListResponseRoom]


class lobbysReadPublicRoomResponse(BaseModel):
    code: int
    data: lobbysReadPublicRoomResponseLoginResponse | lobbysReadPublicRoomResponseRoomListResponse
    message: str
