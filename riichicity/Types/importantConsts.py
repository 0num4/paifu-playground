# 定义番型
EMjFangType = {
    "fangTypeLiZhi": 0,  # 立直
    "fangTypeMenQingZiMO": 1,  # 门清自摸
    "fangTypeYiFa": 2,  # 一发
    "fangTypeLingShangKaihua": 3,  # 岭上开花
    "fangTypeHaiDiLaoYue": 4,  # 海底捞月
    "fangTypeHeDiLaoYu": 5,  # 河底捞鱼
    "fangTypeQiangGang": 6,  # 抢杠
    "fangTypeYiPaiZhong": 7,  # 役牌 中
    "fangTypeYiPaiFa": 8,  # 役牌 发
    "fangTypeYiPaiBai": 9,  # 役牌 白
    "fangTypeYiPaiQuan": 10,  # 役牌 圈风牌
    "fangTypeYiPaiMen": 11,  # 役牌 场风牌
    "fangTypeYiBeiKou": 12,  # 一杯口
    "fangTypePingHe": 13,  # 平和
    "fangTypeDuanYaoJiu": 14,  # 断幺九
    "fangTypeShuangLiZhi": 15,  # 双立直
    "fangTypeDuiDuiHe": 16,  # 对对和
    "fangTypeQiDuiZi": 17,  # 七对子
    "fangTypeSanAnKe": 18,  # 三暗刻
    "fangTypeSanGangZi": 19,  # 三杠子
    "fangTypeHuiYaoJiu": 20,  # 混幺九，混老头
    "fangTypeHuiQuanDaiYaoJiu": 21,  # 混全带幺九
    "fangTypeYiQiTongGuan": 22,  # 一气通贯
    "fangTypeSanSeTongShui": 23,  # 三色同顺
    "fangTypeXiaoSanYuan": 24,  # 小三元
    "fangTypeSanSeTongKe": 25,  # 三色同刻
    "fangTypeChunQuanDaiYaoJiu": 26,  # 纯全带幺九
    "fangTypeHuiYiSe": 27,  # 混一色
    "fangTypeErBeiKou": 28,  # 二杯口
    "fangTypeQingYiSe": 29,  # 清一色
    "fangTypeLiuJuManGuan": 30,  # 流局满贯
    "fangTypeTianHe": 31,  # 天和
    "fangTypeDiHe": 32,  # 地和
    "fangTypeRenHe": 33,  # 人和
    "fangTypeGuoShiWuShuang": 34,  # 国士无双
    "fangTypeGuoShiWuShuang13": 35,  # 国士无双13面
    "fangTypeJiuLianBaoDeng": 36,  # 九莲宝灯
    "fangTypeChunaJiuLianBaoDeng": 37,  # 纯正九莲宝灯
    "fangTypeSiAnKe": 38,  # 四暗刻
    "fangTypeSiAnKeDan": 39,  # 四暗刻单骑
    "fangTypeSiGangZi": 40,  # 四杠子
    "fangTypeQingLaoTou": 41,  # 清老头
    "fangTypeZiYiSe": 42,  # 字一色
    "fangTypeDaSiXi": 43,  # 大四喜
    "fangTypeXiaoSiXi": 44,  # 小四喜
    "fangTypeDaSanYuan": 45,  # 大三元
    "fangTypeLvYiSe": 46,  # 绿一色
    "fangTypeChunLvYiSe": 47,  # 純緑一色
    "fangTypeBaLianZhuang": 48,  # 八連荘
    "fangTypeQiBaoPai": 49,  # 赤宝牌
    "fangTypeBaoPai": 50,  # 宝牌
    "fangTypeLiBaoPai": 51,  # 里宝牌
    "fangTypeKaiLiZhi": 52,  # 開立直
    "fangTypeKaiShuangLiZhi": 53,  # 開双立直
    "fangTypeKaiYiMan": 54,  # 開立直役満
    "fangTypePullNorth": 55,  # 北抜き宝牌
    "fangTypeYiPaiBei": 56,  # 役牌 北
}

# ゲーム終了
EMjGameEndType = {
    "ChiHu": 0,  # 和了で終了
    "ZiMo": 1,  # 自摸で終了
    "SiFengLianDa": 2,  # 四風連打
    "SiGangSanLe": 3,  # 四槓散了
    "SiJiaLiZhi": 4,  # 四家立直
    "SanJiaHuLe": 5,  # 三家和了
    "JiuZhongJiuPai": 6,  # 九種九牌
    "HuanPai": 7,  # 荒牌
    "VoteTermination": 8,  # 投票終了
    "Cheat": 9,  # チート和
    "HuangCheat": 10,  # 荒牌聴牌
    "ForcedEnd": 11,  # 強制終了(タイムアウトなど)
    "SanMaStart": 1000,
    "SanFengLianDa": 1002,  # 三家連打、クライアント側で変換しやすいように
    "SanJiaLiZhi": 1004,  # 三家立直
}

EMjSettingType = {
    "ShowHands": 1,  # 手牌を表示する(他プレイヤーの手牌)
    "ShowChongCards": 2,  # 跳ね牌のヒント
    "ShowHeapCards": 3,  # 牌山を表示
    "ShowAnim": 4,  # アニメーションを再生
    "HideName": 5,  # ニックネームを隠す
    "ShowReplayView": 6,  # 記録を確認する(リプレイ画面を表示)
}

EMjReplayEventType = {
    "GameStart": 1,
    "SendCurrentAction": 2,
    "SendOtherAction": 3,
    "ActionBrc": 4,
    "GameEnd": 5,
    "RoomEnd": 6,
    "GangBaoBrc": 7,
    "LiZhiBrc": 8,
    "UserZhenTing": 9,
    "Pause": 10,  # ルームの一時停止/再開
    "Ting": 11,
}

EMjLiZhiOperate = {"Normal": 0, "KaiLiZhi": 1}  # 通常立直  # 開立直

# Li_Zhi_Operate は後で削除される予定
EMjLiZhiType = {
    "Normal": 1,  # 通常立直
    "DoubleLiZhi": 2,  # 双立直
    "KaiLiZhi": 3,  # 開立直
    "DoubleKaiLiZhi": 4,  # 開立直
}
EMFanFuType = {
    "WuFanFu": 0,  # 符なし
    "OneFangFu": 1,  # 一符
    "TwoFangFu": 2,  # 二符
    "SiFangfu": 3,  # 四符
    "ManGuanFu": 4,  # 満貫符
    "MenQingFu": 5,  # 門前清符
}
EMjConst = {
    "MTCount": 136,
    "MTCount3": 108,
    "MTCount2": 36,
    "MTSeatCount": 34,  # 牌組数
    "MTSeatCount3": 36,  # 3人用牌壁数
    "MTSeatCount2": 36,  # 2人用牌壁数
    "BaoPaiIdx": 6,
    "BaoPaiIdx_PullNorth": 10,  # 北抜きルールの宝牌インジケータ
    "WangPaiIdx": 14,
    "WangPaiIdx_PullNorth": 14,
}

# 麻雀牌の位置
EMjTileNode = {
    "Heap": 1,
    "Private": 2,
    "Discard": 3,
    "Public": 4,
    "LockNode": 5,
}  # 牌山  # 手牌  # 捨て牌  # 副露牌  # 当前视角的手牌(# 現在の視点の手牌)

EMjSeatType = {
    "MST_OWNER": 1,
    "MST_LATTER": 2,
    "MST_OPPOSITE": 3,
    "MST_FORMER": 4,
    "MAX": 4,
}  # 自己  # 下家  # 对家  # 上家

EMjActionType = {
    "ActionNotOperate": 0,
    "ActionCheck": 1,
    "ActionZuoChi": 2,  # 左の牌を食う 56 を4で食う
    "ActionZhongChi": 3,  # 中の牌を食う 35を4で食う
    "ActionYouChi": 4,  # 右の牌を食う 56を7で食う
    "ActionPeng": 5,
    "ActionMingGang": 6,
    "ActionChiHu": 7,
    "ActionAnGang": 8,
    "ActionBuGang": 9,
    "ActionZiMo": 10,
    "ActionOutCard": 11,
    "ActionEndGame": 12,
    "ActionPullNorth": 13,  # 北抜き
    "ActionNextInCard": 100,  # gmテスト命令
    "ActionLiZhi": 200,  # 客户端自己定义
    "ActionDrawCard": 201,
    "ActionOfficalEnter": 202,  # 公式戦の楽しい声
    "ActionOfficalPromotion": 203,
    "ActionOfficalFinal": 204,
    "ActionKaiLiZhi": 205,
}

# ゲームタイプ
GamePlayType = {
    "All": 0,
    "Rank": 1001,  # 段位戦
    "Match": 1002,  # 大会
    "Friend": 1003,  # 友人戦
    "OneRoundFight": 1004,  # ワンラウンド戦
    "OneRoundFightLobby": 1005,  # ワンラウンド戦ロビー
}

# 一局戦ランクタイプ
OneRoundFightRankType = {
    "FangCoupon": 1,  # 一番券
    "OwlCoin": 2,  # 梟コイン
}

# プレイヤー人数
PlayerCount = {
    "Three": 3,
    "Four": 4,
    "Two": 2,
}

# ランクタイプ
StateType = {
    "NewStar": 1,  # 新星
    "BrightMoon": 2,  # 輝月
    "HotSun": 3,  # 炎陽
    "MilkyWay": 4,  # 銀河
}

RoundType = {
    "East": 1,  # 東場
    "South": 2,  # 南場
    "One": 3,  # 一局
    "Total": 4,
}

# ユーザートークンタイプ
UserTokenType = {
    "Unknown": 0,
    "Guest": 1,  # 匿名
    "FaceBook": 2,  # Facebook
    "Google": 3,  # Google
    "Apple": 4,  # Apple
    "Twitter": 5,  # Twitter
    "Email": 6,
    "Line": 7,
    "Steam": 8,
}


# ユーザーステータス
UserStatus = {
    "Normarl": 0,
    "Frozen": 1,
    "Deleted": 2,
    "ApplyPass": 3,
    "ApplyReject": 4,
}

# 和了の役種
HuSizeType = {
    "Not": 0,  # なし
    "One": 1,  # 1翻
    "Two": 2,  # 2翻
    "Three": 3,  # 3翻
    "Four": 4,  # 4翻
    "ManGuan": 5,  # 満貫
    "TiaoMan": 6,  # 跳満
    "BeiMan": 7,  # 倍満
    "ThreeBeiMan": 8,  # 三倍満
    "YiMan": 9,  # 役満
    "TwoYiMan": 10,  # ダブル役満
}

# 大会タイプ
MatchType = {
    "None": 0,  # なし
    "SelfBuild": 1,  # 自作大会
    "Full": 2,  # 満員開始大会
    "GrandPrix": 3,  # グランプリ
    "FLHSRace": 4,  # 風雷火山大会
}
