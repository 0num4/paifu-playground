# 7c9bc09e9eb29703a4a50f9c3edfc410.lua
from enum import Enum, IntEnum, StrEnum


class Award:
    def __init__(self, itemId: int, category: any, count: int):  # category: Category
        self.itemId = itemId
        self.category = category
        self.count = count


class EProceStateType(Enum):
    Login = "ProceStates/ProceLogin"
    Hall = "ProceStates/ProceHall"
    NormalRoom = "ProceStates/ProceNormalRoom"
    ReplayRoom = "ProceStates/ProceReplayRoom"
    Lottery = "ProceStates/ProceLottery"
    Guide = "ProceStates/ProceGuide"
    GuideGame = "ProceStates/ProceGameGuide"


class SceneType(Enum):
    Main = "Main"
    Hall = "Hall"
    Room = "Room"
    Loading = "Loading"
    NormalGame = "NormalGame"
    LotteryScene = "paomian"
    TablePreview = "TablePreview"
    TournamentMatchingResult = "TournamentMatchingResult"  # 公式戦マッチング完了後の3Dシーン
    MusicGame = "MusicGame"


class SoundType(Enum):
    back = 0  # BGM
    GameAct = 3  # ゲーム操作音
    UI = 4  # UI音
    FanType = 5  # 役の音
    RoleAct = 6  # 局の操作音（キャラクター固有の効果音）
    Voice = 7  # ボイス
    Guide = 8  # 新規音声
    RoleAuto = 9  # 自動で再生される効果音
    Chat = 10
    UIBg = 11  # 一部のUIの背景音
    BackLiZhi = 12  # 立直時の背景音楽
    Extension = 13  # 拡張音1、音量はGameActと同じ
    AnnualReport = 14  # 年次報告の背景音楽は別で制御
    AnnualReportUI = 15
    BackZhanDou = 16  # 戦闘時の背景音楽
    PreVoice = 17  # プレビュー音声
    StoryBGM = 18  # ストーリーBGM


class SoundCtrlType(Enum):
    BgMusic = "BgMusic_New"  # 背景音楽
    BgLiZhiMusic = "BgLiZhiMusic_New"  # 立直
    Audio = "Audio_New"  # 音響
    Voice = "Voice_New"  # ボイス（局内）
    VoiceOut = "VoiceOut_New"  # ボイス（局外）
    AllSound = "AllSound_New"  # 全体音量
    OperAudio = "OperAudio_New"  # 戦闘Bg音楽
    AnnualReport = "AnnualReport_New"
    PreVoice = "PreVoice_New"  # プレビュー音声


class SoudTypeToCtrlType(Enum):
    back = SoundCtrlType.BgMusic
    GameAct = SoundCtrlType.Audio
    Extension = SoundCtrlType.Audio
    UI = SoundCtrlType.Audio
    FanType = SoundCtrlType.Voice
    RoleAct = SoundCtrlType.Voice
    Voice = SoundCtrlType.Voice
    Guide = SoundCtrlType.Voice
    RoleAuto = SoundCtrlType.Voice
    Chat = SoundCtrlType.Voice
    UIBg = SoundCtrlType.Audio
    BackLiZhi = SoundCtrlType.BgLiZhiMusic
    BackZhanDou = SoundCtrlType.OperAudio
    AnnualReport = SoundCtrlType.AnnualReport
    AnnualReportUI = SoundCtrlType.AnnualReport


class EnumDefine:
    class MusicGameMode(IntEnum):
        Easy = 1  # 音ゲーモード - Easy
        Hard = 2  # 音ゲーモード - Hard

    class PromptType(IntEnum):
        Tips = 1  # ヒント
        Reward_Tips = 2  # 単一の報酬とヒント
        Rewards_Tips = 3  # 報酬一覧とヒント
        Address = 4  # アドレス
        Exchange = 5  # 交換

    class ButtonState(IntEnum):
        Normal = 0  # 通常
        Gray = 1  # グレー
        Active = 2  # アクティブ

    class ServerConnectState(IntEnum):
        START = 1  # 開始
        CONNECTED = 2  # 接続済み
        CONNECTE_FAILED = 3  # 接続失敗
        NOTReachable = 4  # 到達不能

    class AtlasName(StrEnum):
        Common = "Common"
        CommonWidget = "CommonWidget"
        CommonWidget2 = "CommonWidget2"
        CommonPopup = "CommonPopup"
        Mail = "Mails"
        RoomList = "RoomList"
        Skill = "Skill"
        Vip = "Vip"
        Room = "Room"
        LotteryDraw = "LotteryDraw"
        Desk = "Desk"
        Cards = "Cards"
        CardsBg = "CardsBg"
        RoomAnim = "RoomAnim"
        RoomOperTips = "RoomOperTips"

        RoomResultSingle = "RoomResultSingle"
        RoomResultLiuJu = "RoomResultLiuJu"
        PersonalInfo = "PersonalInfo"
        PersonalNewInfo = "PersonalNewInfo"

        ShopItems = "ShopItems"
        Shop = "Shop"
        ShopSkins = "ShopSkins"
        SpecialPack = "SpecialPack"
        ShopSkinShowBanner = "ShopSkinShowBanner"

        Tournament = "Tournament"
        TournamentResult = "TournamentResult"
        TournamentBuildHall = "TournamentBuildHall"
        Title = "Title"

        Hall = "Hall"
        HallBg = "HallBg"
        Item = "Item"
        Guide = "Guide"
        ActivitySign = "ActivitySign"
        Role = "Role"
        Champion = "Champion"
        PcPay = "PcPay"
        Log = "Log"
        Set = "Set"
        ActivityHedge = "ActivityHedge"
        ActivityCupGuess = "ActivityCupGuess"
        Draw = "Draw"
        LeaderBoard = "LeaderBoard"
        Login = "Login"
        ActivityNewerSevenDays = "ActivityNewerSevenDays"
        SummerLive = "ActivitySummer"
        TournamentRoleMgr = "TournamentRoleMgr"
        TournamentBuild = "TournamentBuild"
        Task = "TaskNew"
        ActivityHall = "ActivityHall"
        ActivityObon = "ActivityObon"
        ActivitySurvey = "ActivitySurvey"

        ActivityChallengeBattle = "ActivityChallengeBattle"
        ActivityChallengeRivalHead = "ActivityChallengeRivalHead"
        ActivityChallengeHouse = "ActivityChallengeHouse"
        ActivityChallengeRole = "ActivityChallengeRole"

        Reward = "Reward"

        ActivitySocialGroup = "ActivitySocialGroup"

        TournamentOffice = "TournamentOffice"

        ActivityHallNew = "ActivityHallNew"

        ActivityChristmas = "ActivityChristmas"
        ActivityChristmasBattle = "ActivityChristmasBattle"

        AnnualReportBigNews = "AnnualReportBigNews"
        AnnualReportRole = "AnnualReportRole"
        ShopNewBackGround = "ShopNewBackGround"

    class ShowRolePanel(StrEnum):
        ShowRole = "ShowRole"  # キャラクター立ち絵表示画面
        Role = "Role"  # キャラクター情報表示画面
        GameResultSingle = "GameResultSingle"
        GameResultFinal = "GameResultFinal"
        Matching = "Matching"
        MatchingResultLeft = "MatchingResultLeft"
        MatchingResultRight = "MatchingResultRight"
        MatchingResultTop = "MatchingResultTop"
        MatchingResultBottom = "MatchingResultBottom"
        RoomAnimLeft = "RoomAnimLeft"
        RoomAnimRight = "RoomAnimRight"
        RoomAnimTop = "RoomAnimTop"
        RoomAnimBottom = "RoomAnimBottom"
        ResultScoreLeft = "ResultScoreLeft"
        ResultScoreRight = "ResultScoreRight"
        ResultScoreTop = "ResultScoreTop"
        ResultScoreBottom = "ResultScoreBottom"
        PersonalPopup = "PersonalPopup"
        SkillSpine = "SkillSpine"
        DrawResult = "DrawResult"
        FriendRoomReady = "FriendRoomReady"
        SummerSettleMent = "SummerSettleMent"
        SummerSettleChampion = "SummerSettleChampion"
        UpStage = "UpStage"  # 昇段
        Shop = "Shop"  # ショップ
        AnnualReportHead = "AnnualReportHead"  # 年次報告のアバター
        AnnualReportRole = "AnnualReportRole"  # 年次報告のキャラクター
        PersonalCarte = "PersonalCarte"  # 名刺
        Hall = "Hall"

    class NetQuality(IntEnum):
        Good = 3  # 良好
        Fair = 2  # 普通
        Bad = 1  # 悪い
        Invalide = 0  # 無効

    class GamePlayType(IntEnum):
        All = 0  # 全て
        Rank = 1001  # 段位戦
        Match = 1002  # マッチ
        Friend = 1003  # 友人戦
        OneRoundFight = 1004  # 一局戦
        OneRoundFightLobby = 1005  # 一局戦ロビー

    class OneRoundFightRankType(IntEnum):
        FangCoupon = 1  # 翻券
        OwlCoin = 2  # フクロウコイン

    class PlayerCount(IntEnum):
        Three = 3  # 3人
        Four = 4  # 4人
        Two = 2  # 2人

    # 段位の種類
    # 1：新星 2：輝月 3：炎陽 4：銀河
    class StateType(IntEnum):
        NewStar = 1  # 新星
        BrightMoon = 2  # 輝月
        HotSun = 3  # 炎陽
        MilkyWay = 4  # 銀河

    class RoundType(IntEnum):
        East = 1  # 東場
        South = 2  # 南場
        One = 3  # 一局
        Total = 4  # 全体

    class MatchEnterRulesType(IntEnum):
        None_ = 1  # 制限なし
        Password = 2  # パスワードで入場
        Review = 3  # 審査で入場

    class MatchRulesType(IntEnum):
        Random = 1  # ランダムマッチング
        Assign = 2  # 指定マッチング
        Advance = 3  # 高度なマッチング

    class MatchTagType(IntEnum):
        SelfBuild = 1  # 自作戦
        My = 2  # 自分の
        Find = 3  # 検索

    class MatchType(IntEnum):
        None_ = 0  # なし
        SelfBuild = 1  # 自作戦
        Full = 2  # 定員になり次第開始
        GrandPrix = 3  # グランプリ
        FLHSRace = 4  # 風林火山レース

    class MatchStatus(IntEnum):
        Prepare = 1  # 未開始
        Playing = 2  # 進行中
        End = 3  # 終了

    class MatchUserStatus(IntEnum):
        Online = 1  # オンライン
        Ready = 2  # 準備完了
        Playing = 3  # プレイ中

    class SelfBuildStatus(IntEnum):
        Enter = 1  # 自作戦に参加
        Ready = 2  # 準備完了
        Playing = 3  # プレイ中
        NotEnter = 4  # 自作戦に未参加

    class UserTokenType(IntEnum):
        Unknown = 0  # 不明
        Guest = 1  # ゲスト
        FaceBook = 2  # Facebook
        Google = 3  # Google
        Apple = 4  # Apple
        Twitter = 5  # Twitter
        Email = 6  # メールアドレス
        Line = 7  # LINE
        Steam = 8  # Steam

    class ItemStatus(IntEnum):
        NotOnline = 1  # オンラインでない
        NotUnlock = 2  # ロック解除されていない
        Own = 3  # 所有済み

    class ItemSource(IntEnum):
        System = 1  # システムから付与
        Draw = 2  # ガチャから入手
        Activity = 3  # イベントから入手
        Official = 4  # 公式から付与
        Exchange = 5  # 交換で入手
        Awaken = 6  # 覚醒で入手
        Buy = 7  # ショップで購入

    class SkinSource(IntEnum):
        Awaken = 1  # 覚醒で入手
        System = 2  # システムから付与
        Draw = 3  # ガチャから入手
        Buy = 4  # ショップで購入
        Exchange = 5  # 交換で入手
        Activity = 6  # イベントから入手
        Task = 7  # タスクから入手
        SpecialPack = 9  # 特別ギフトパックから入手
        NewPoolGift = 10  # 専用ギフトから入手

    class RoleSource(IntEnum):
        System = 1  # システムから付与
        Draw = 2  # ガチャから入手
        Activity = 3  # イベントから入手
        Official = 4  # 公式から付与
        Exchange = 5  # 交換で入手
        Buy = 6  # ショップで購入
        LimitDraw = 7  # 期間限定ガチャ

    class CultivateStatus(IntEnum):
        UnableCultivate = 1  # 育成不可
        AbleCultivate = 2  # 育成可能
        AbleAwaken = 3  # 覚醒可能
        FinishedAwaken = 4  # 覚醒完了/誓約育成状

    ##############################################

    class BagShowType(IntEnum):
        None_ = 0  # 制限なし
        henHave = 1  # 所有しているアイテムのみ表示
        Never = 2  # 絶対に表示しない

    class ItemType(IntEnum):
        Currency = 10  # 通貨
        Gift = 11  # ギフト
        Awaken = 12  # 覚醒
        RiichiStick = 13  # リーチ棒
        CardBack = 14  # 牌背
        Tablecloth = 15  # テーブルクロス
        SpecialEffect = 16  # 特殊効果
        LiZhiEffect = 17  # リーチ効果
        HallBGM = 18  # ロビーBGM
        RankBGM = 19  # ランク戦BGM
        LZBGM = 20  # ランク戦BGM
        ChangeName = 21  # 改名カード
        MatchBGM = 22  # 大会戦BGM
        SceneEffect = 24  # シーン効果
        HallBg = 25  # ロビー背景
        CardFace = 26  # 牌面（ハロウィンで追加）
        AvatarFrame = 30  # アバターフレーム
        GiftBag = 31  # ギフトパック
        OptionalGift = 32  # 自由選択ギフト
        ProbGiftBag = 34  # 確率ギフトパック
        SpecialBag = 35  # 特別ギフトパック（ギフトパック-縁結びの狐、ギフトパック-純白の恋歌）
        TableEdge = 36  # テーブルエッジ

    class OfficialSign(IntEnum):
        Pre = 1  # 事前登録、次のラウンドの準備中
        NotDeal = 2  # 登録未処理
        Deal = 3  # 登録処理済み
        InDeal = 4  # 登録処理中-マッチング中
        Eliminated = 5  # 敗退
        Win = 666  # 勝利

    class TitleState(IntEnum):
        Acquired = 1  # 取得済み
        using = 2  # 使用中
        lock = 3  # ロック中

    class VirtualItemID(IntEnum):
        Ticket = 10001  # 一番券
        Coin = 10002  # フクロウコイン
        SkinGold = 10003  # キャラクタースキン回収コイン
        GiftGold = 10004  # ギフト粉砕回収コイン
        ItemGold = 10005  # アイテム回収コイン
        TournamentScore = 10025  # 大会戦スコア
        OutfitTokens = 10026  # 衣装券
        NewerPoolCoupon = 10035  # 新規プールクーポン
        GoldenTicket = 10037  # ゴールデンチケット

    class ItemID(IntEnum):
        FangCoupon = 10001  # 番券
        OwlCoin = 10002  # フクロウコインID
        RecycleRole = 10003  # キャラクタースキン回収コイン
        RecycleGift = 10004  # ギフト粉砕回収コイン
        RecycleProp = 10005  # アイテム回収コイン
        DrawExchange = 10006  # ガチャ交換コイン
        DrawCoupon = 10007  # ガチャ券
        XueHua = 10008  # 雪花
        YingHua = 10009  # 桜花
        ChangeNameCard = 21001  # 改名カード
        Stamp = 10011  # スタンプ
        TournamentScore = 10025  # 大会戦スコア
        OutfitTokens = 10026  # 衣装券
        GoldenTicket = 10037  # ゴールデンチケット
        DailyGift = 34017  # デイリーギフト、現在はブラインドボックスに変更
        ChristmasLife = 10027  # クリスマスイベントライフ
        FukaseCoin = 10028  # 深瀬コイン
        AnniversaryOptionalGift = 32002  # 周年記念自由選択ギフト
        GiftOptionalGift = 32003  # 育成自由選択ギフト（特別なギフトを開けられる）
        AwkenOptionalGift = 32001  # 覚醒自由選択ギフト
        SkinGiftBagCoupon = 10039  # スキンギフトパック8割引クーポン
        FLHSHelp = 10041  # 応援コイン
        LoveValue = 10052  # MO連動-LLP
        MatrialValue = 10053  # MO連動-クラフト素材
        MelodyNote = 10051  # リズムノート、2周年イベント-音律華章の通貨

    class UnknowID(IntEnum):
        SkinID = -1
        RoleID = -1

    class SoundName(StrEnum):
        BGLobby = "bg_lobby"
        BGGame = "bg_game"
        BGGameLiZhi = "bg_lizhi"
        BGMatch = "bg_match_win"
        BGHallSummer = "bg_hall_summer"
        NewThemeSong = "new_theme_song"
        BGMTwoYear = "bgm_login_bang"
        MOBGM = "bgm_mo_With_memories_LP"
        VoiceLobbyStart = "voice_lobby_gamestart"
        GameZiMoHe = "game_zimo_he"  # 自摸和了
        GameStartDice = "game_dice"  # ゲーム開始時のサイコロ
        GameStartFlipCard = "hands_flip"  # 開局時の牌のめくり効果
        GameClickCard = "click_pai"  # ゲーム中の牌のクリック
        GameOutCard = "discard_tile"  # 打牌
        GameChiPengGang = "oper_chi_peng_gang"  # ゲーム中のチー、ポン、カンのトリガー効果（手牌を移動させるとき）
        GameResultSingle = "game_result_single"
        GameResultSingleSpecialFan = "game_result_single_special_fan"  # 単局画面で特殊な役が出現
        GameResultFinal = "game_result_final"
        GameResultScore = "game_result_score"
        GameResultScoreBao = "game_result_score_bao"  # 供託点棒払い音声
        HuEffLightning = "hu_eff_lightning"  # 和了時の雷効果
        GameOperCountDown = "countdown5"  # 操作カウントダウン
        GamePushHands = "game_push_hands"  # 麻雀牌を広げる
        HuZiMo = "hu_zimo"
        CardMoPai = "card_mopai"
        RotateBaoPai = "game_rotate_baopai"
        MoPoolBgm = "bgm_mo_With_memories_LP"

        BtnClick = "btn_click"  # UIクリック
        Tips = "tips"  # トーストのヒント
        TabSwitch = "tab_switch"
        YiManKeNeng = "yimankeneng"
        YiManQueDing = "yimanqueding"
        LiuJu = "liuju"

        MatchSuccess = "match_success"  # マッチング成功
        SkillEff = "skill_eff"  # 必殺技
        MatchPromotion = "match_promotion"  # 試合の昇格

        DrawDropDown = "draw_drop_down"  # ガチャ
        DrawOne = "draw_one"
        DrawTen = "draw_ten"
        DrawGetRole = "draw_get_role"
        TournamentResultChampion = "tournament_result_champion"
        ActionTips = "action_tips"
        Hu_EffectCat = "hu_eff_cat"
        Hu_EffectHole = "eff_black_hole"
        Hu_EffectDragon = "eff_baddragon"
        Hu_EffectTurrent = "eff_turret"
        Hu_EffectStar = "eff_star"
        Hu_EFfectMelody = "eff_melody"
        Hu_EffectHalloween = "eff_halloween"
        Hu_EffectWind = "eff_wind"
        Hu_EffectSword = "hu_eff_sword"
        Hu_EffectStage = "hu_eff_stage"
        Hu_EffectCube = "eff_cube"
        Hu_EffectCm = "eff_christmas"
        Hu_EffectLovely = "eff_lovely"
        Reward = "reward"
        FeelBubble = "feelbubble"
        RankShow = "rankshow"
        NumRoll = "numroll"
        StageUp = "stageup"
        StageDown = "stagedown"
        Hu_Dragon = "dragon"
        AchPop = "ach_pop_up"
        JinJiChengGong = "jinjichenggong"

    class LiveType(IntEnum):
        LiveTag = 1  # 配信者モードのタグ
        PersonalInfo = 2  # 個人情報
        Game = 3  # マッチングと対局のニックネーム
        Friend = 4  # 友人戦とフレンド
        Watch = 5  # 観戦
        Log = 6  # 牌譜
        Rank = 7  # ランキング

    class Category(IntEnum):
        Item = 0  # アイテム
        Skin = 1  # スキン
        Role = 2  # キャラクター
        Emotion = 3  # 感情
        Title = 4  # タイトル

    class PopUpType(IntEnum):
        Passive = 0  # 受動的にポップアップ
        Active = 1  # 能動的にポップアップ
        Jump = 2  # ジャンプしてポップアップ

    class PopUpLocation(IntEnum):
        Outline = 0  # アクティビティの外枠
        Single = 1  # 単独のポップアップ

    class Gender(IntEnum):
        WoMan = 1  # 女性
        Man = 2  # 男性
        Unknow = 3  # 不明

    class HandID(IntEnum):
        WoMan = 1  # 女性の手
        Man = 2  # 男性の手
        Panda = 3  # パンダの手
        BlackWoman = 4  # 黒人女性の手

    class RoleSoundUnlockType(IntEnum):
        Default = 0  # デフォルトで所有
        Awake = 1  # 覚醒で所有
        Ancient = 2  # 古役

    class RoleSubViewType(IntEnum):
        RoleDes = 1  # キャラクター説明
        RoleSound = 2  # キャラクターボイス
        RoleSkin = 3  # キャラクタースキン
        RoleCharging = 4  # キャラクターチャージング
        RoleAwake = 5  # キャラクター覚醒

    class EmailJump(IntEnum):
        EmailBind = 1  # メールアドレスの紐付け

    class PcPayWay(IntEnum):
        VISA = 1
        MASTER = 2
        AMEX = 3
        UNIONPAY = 4
        LINEPAAY = 5
        PAYME = 6
        KAKAAOPAY = 7
        XSOLLA = 8
        UNIONPAY2 = 9
        PAYPAL = 10
        MAYCARD = 11
        JCB = 12
        KONBINI = 13
        TOSS = 14
        ALIPAY = 15
        BtiCash = 16
        PayEasy = 17
        GrabPay = 18
        TNG = 19
        Boost = 20
        FPX = 21
        Dana = 22
        DOKUWallet = 23
        GCash = 24
        DragonPay = 25
        ALIPAY2 = 26
        WeChat = 27

    class CountryCode(StrEnum):
        JP = "JP"  # Japan
        KR = "KR"  # Korea, Republic of
        TW = "TW"  # Taiwan, Province of China
        HK = "HK"  # Hong Kong
        US = "US"  # United States of America
        SG = "SG"  # Singapore
        MY = "MY"  # Malaysia
        ID = "ID"  # Indonesia
        PH = "PH"  # Philippines
        OTHER = "OTHER"  # その他
        CN = "CN"  # 中国本土

    class FriendMatchPlayerAction(IntEnum):
        Enter = 0  # 入場
        Start = 1  # 開始
        Ready = 2  # 準備完了
        Cancel = 3  # キャンセル
        Kick = 4  # キック
        Leave = 5  # 退出
        ChangeRule = 6  # ルール変更
        ChangeRoleSkin = 7  # キャラクタースキン変更
        AddRobot = 8  # ロボット追加
        DelRobot = 9  # ロボット削除
        Move = 10  # 移動

    class HedgeShopType(IntEnum):
        TopSecretExchange = 1  # 極秘交換
        ConfidentialExchange = 2  # 機密交換
        HedgeExchange = 3  # 秘密交換

    class AvatarTabType(IntEnum):
        All = 0  # 全て
        Activity = 1  # アクティビティ
        Draw = 2  # ガチャ
        Shop = 3  # ショップ
        Official = 4  # 公式
        Nurturancered = 5  # 育成
        Defaule = 30000  # デフォルト、非常に特殊

    class CampMeleeTabType(IntEnum):
        All = 0  # 全て
        Camp1 = 1  # 帝皇
        Camp2 = 2  # 佐賀ワールド
        Camp3 = 3  # Dawn命運の騎士
        Camp4 = 4  # 星辰
        Camp5 = 5  # 三途インダストリー
        Camp6 = 6  # 雀丘
        Camp7 = 7  # 桜満茶社
        Camp8 = 8  # RiichiCreators

    class TitleTabType(IntEnum):
        All = -1  # 全て
        Battle = 1  # 対戦
        Recharge = 2  # 課金
        Activity = 3  # アクティビティ
        Nurturance = 4  # 育成
        Achievement = 5  # 実績

    class ItemGetWayType(IntEnum):
        Welfare = 5  # チャージ特典

    class LeaderBoardMainType(IntEnum):
        FourPlayers = 1  # 四人戦
        ThreePlayers = 2  # 三人戦
        OneFan = 3  # 1番戦
        YiManWeek = 4  # 役満週間ランキング
        Activity = 5  # アクティビティランキング

    class LeaderBoardSubType(IntEnum):
        RankType1 = 1  # （三人戦/四人戦）段位 / 三麻1番週間ランキング
        RankType2 = 2  # （三人戦/四人戦）Rポイント / 四麻1番週間ランキング

    class LeaderBoardServerType(IntEnum):
        FourPlayers_SegmentRank = 1  # 四麻段位ランキング
        FourPlayers_RValueRank = 2  # 四麻Rポイントランキング
        ThreePlayers_SegmentRank = 3  # 三麻段位ランキング
        ThreePlayers_RValueRank = 4  # 三麻Rポイントランキング
        OneFan = 5  # 1番ランキング [非推奨]
        OneFan_Four = 6  # 四麻1番週間ランキング
        OneFan_Three = 7  # 三麻1番週間ランキング

    class LeaderBoardActivitySortType(IntEnum):
        PT_Total = 1  # 総PT
        First_TIMES = 2  # 1位回数
        PT_Max = 3  # 最大PT

    class SelfIdentity(IntEnum):
        Invite = 1  # 招待リスト
        Blacklist = 2  # ブラックリスト
        Administrator = 3  # 管理者

    class SpecialPackType(IntEnum):
        FirstPay = 1  # 初回課金
        VipPay = 2  # VIP課金
        LovelyFox = 3  # 縁結びの狐
        LovelySong = 4  # 純白の恋歌
        CherryTime = 5  # 悠然時光ギフトパック
        CherryNight = 6  # 夜桜ギフトパック
        ChasingWaves = 7  # 逐浪
        SeasidePractice = 8  # 海辺修行
        SpecialLive = 9  # 特別ライブ
        MidsummerSeaBreeze = 10  # 盛夏の海風
        DrinkAndBullet = 11  # 酒杯と弾丸
        NewPoolGift = 12  # 10連券ギフトパック
        HeartJump = 13  # 心跳ギフトパック
        HeartHot = 14  # 心花の如く
        SprintFlowers = 15  # 疾駆る緋花
        LycoriQianShu = 16  # 千束ギフトパック
        LycoriLongNai = 17  # 瀧奈ギフトパック
        LycoriRuiXi = 18  # 瑞希ギフトパック
        LycoriHuTao = 19  # 胡桃ギフトパック
        NewGiftQM = 20  # 新人ギフトパック--清美
        NewGiftHN = 21  # 新人ギフトパック--環奈
        ThoughtsBgm = 22  # BGMギフトパック
        SpeedFastIntegrate = 23  # 極速狂飆三合一ギフトパック
        MichiyukiAndShiotsukiIntegrate = 24  # 天海汐月と原道雪
        DreamLand = 25  # 不破2023ハロウィンスキンギフトパック
        Purity = 26  # 小倉奏2023ハロウィンスキンギフトパック
        Charm = 27  # 三宅2023ハロウィンスキンギフトパック
        MagicGril = 28  # 雪魔女の恋慕
        WinSoldier = 29  # 窓辺の兵士
        ChristmasEve = 30  # 「聖夜」視聴アルバムギフトパック
        CrystalClear = 31  # 澄澈の境
        Bliss = 32  # 花火映る流年
        WeddingDress = 33  # 花嫁の誓い
        OldTimes = 34  # 旧時代の金属
        YearRoundBuPo = 35  # 綺恋の歌
        YearRoundAlice = 36  # パーフェクトビート
        YearRoundXiaoCangZou = 37  # 絶妙なステージ計画
        MoPackBaiHe = 38  # MO月下独奏
        MoPackLinQi = 39  # MO天使の園
        MoPackKeLuoAi = 40  # MO温もりの冬日
        MoPackNuoAiEr = 41  # MO学園祭のステージ

    class PayCurrency(StrEnum):
        USD = "USD"
        JPY = "JPY"
        KRW = "KRW"
        TWD = "TWD"

    class TaskType(IntEnum):
        Daily = 1  # デイリータスク
        Growth = 2  # 成長タスク
        Weekly = 3  # ウィークリータスク

    class TaskAction(IntEnum):
        RoleClick = 2002  # キャラクターとのインタラクション
        RoleIntroduce = 2005  # キャラクター紹介を見る
        WatchGame = 2006  # 観戦
        BookMark = 2007  # 牌譜のブックマーク
        WatchRank = 2008  # ランキングを見る
        ReviewPaiPu = 3006  # 牌譜を見る

        ViewDrawContent = 2010  # 招待一覧を見る
        ViewDrawStore = 2011  # 招待ストアを見る
        ViewRoleArchive = 2012  # 雀士資料を見る
        ViewRoleVertical = 2013  # 雀士の立ち絵を見る
        ViewFeatured = 2014  # 特別おすすめを見る
        ViewFeaturedStore = 2015  # 精選ストアを見る
        ViewShopWafare = 2016  # ショップ特典を見る
        ViewCoinStore = 2017  # フクロウコインストアを見る
        ViewStampStore = 2018  # スタンプストアを見る
        ViewTPStore = 2019  # ポイントストアを見る
        ViewotherStore = 2020  # 雑貨店を見

    class PlayGameState(IntEnum):
        Leisure = 1  # 空き時間
        Playing = 2  # ゲーム中
        OffLine = 3  # オフライン

    class RedPointEnum(IntEnum):
        StageThree = 1  # 段位戦3人麻雀
        FriendLableShow = 2  # 友人入口
        FriendApplyShow = 3  # 申請タブの赤点
        DrawCardShopRed = 4  # ガチャショップへのジャンプ赤点
        SlienceSet = 5  # ミュート設定
        PersonalCarte = 6  # 名刺閲覧赤点

    class GuideEvent(IntEnum):
        SelectGoods = 1  # ギフトを選択
        SendGift = 2  # ギフトを贈る
        EnterMatch = 3  # 段位戦に参加
        OpenCalt = 4  # 育成を開く
        OpenFanType = 5  # 役種を開く
        CloseSingle = 6
        CloseScore = 7
        CloseFinal = 8
        ShowRole = 9
        ClickNewRole = 10
        OpenRoleNameEditor = 11  # キャラクターの改名を開く
        AddCpu = 12

    class NoticeGuideEvent(IntEnum):
        SettingClose = 1  # 設定画面を閉じた
        RoleCenterClose = 2  # 個人情報を閉じた
        SingleOpen = 3  # 単局決算を開いた
        ScoreOpen = 4  # スコア画面を開いた
        FinalOpen = 5  # 最終決算を開いた
        ScoreClose = 6

    class AdjustEventToken(StrEnum):
        FirstDayFinishOneRank = "8fcrs0"  # 新規ユーザーが初日に段位戦を1回クリア
        FirstDayRankUpgrade = "symflc"  # 新規ユーザーが初日に最初の段位アップを達成したユーザー数
        ChargeTryFirstDay = "7bqj43"  # 商品をクリック、月間パスの購入ボタンをクリック、初回課金ギフトパックの【チャージへ】ボタンをクリック

    class arenaPhase(IntEnum):
        C = 0
        B = 1
        A = 2
        S = 3
        SS = 4

    class TargetFrameType(IntEnum):
        None_ = 0  # 未初期化
        Frame30 = 1
        Frame60 = 2

    class ItemQualitySample(dict[str, int]):
        common_frame_red = 5
        common_frame_yellow = 4
        common_frame_purple = 3
        common_frame_blue = 2
        common_frame_green = 1

    class UserStatus(IntEnum):
        Normarl = 0  # 通常
        Frozen = 1  # 凍結
        Deleted = 2  # 削除済み
        ApplyPass = 3  # 申請合格
        ApplyReject = 4  # 申請拒否

    class RoleModel(IntEnum):
        Normal = 0  # 通常
        Black = 1  # 黒夜
        Father = 2  # 父
        Mother = 3  # 母

    class CardPoolType(IntEnum):
        Anniversary = 1  # 周年記念ガチャ
        NatsuumiMarin = 2  # 虎娘ガチャ
        KukiRenshin = 3  # 九鬼蓮心ガチャ
        CommonMale = 4  # Boy常駐ガチャ
        CommonGril = 5  # Gril常駐ガチャ
        FukaseAlice = 6  # 愛麗絲
        ShirahaAsuka = 7  # 飛鳥
        HujiIkki = 8  # 不二
        Saeko = 9  # 五十嵐紗子
        AmamiAndKuki = 10
        TohoNagi = 11  # 東方凪
        MichiyukiAndIkuko = 12  # 原道雪&音無郁子
        YurikaAndAthena = 13  # 五月女百合香&赤羽雅典娜
        NewbePool = 1000  # 新人ガチャ
        NaoYaPool = 14  # 五月女直哉
        NatsuumiAndSaotome = 15  # 夏海+五月女
        Enomiya = 16  # 榎宮澪ガチャ
        AuRoRa = 17  # 吸血鬼
        ShirahaAsukaNew = 18  # 飛鳥
        JanMaru = 19  # 雀丸
        KokuraKanade = 20  # 小倉奏
        SaekoAndRenshin = 21  # 沙子と蓮心
        LycorisRecoil = 22  # コラボキャラクターガチャ
        MichiyukiAndShiotsuki = 23  # 原道雪&天海汐月
        AliceAndMenia = 24  # 愛麗絲&メニア
        FuwaMahiru = 25  # 不破真昼
        NatsuumiAndSaotome2 = 26  # 夏海+五月女復刻
        HujiNew = 27  # 不二一気ガチャ
        YurikaNew = 28  # 赤羽雅典娜ガチャ
        YangCai = 29  # 犬飼陽菜ガチャ
        Tach = 30  # 立花薫ガチャ
        YuZhu = 31  # 鈺燭ガチャ 126001
        TransPool1 = 32  # 小倉奏&不破真昼&深瀬愛麗絲ガチャ 127001
        TransPool2 = 33  # 白羽飛鳥&九鬼蓮心ガチャ 127001
        TransPool3 = 34  # 夏海真凜&五十嵐紗子ガチャ 127001
        TransPool4 = 35  # 原道雪&メニアガチャ 127001
        TransPool5 = 36  # 音無郁子&天海汐月ガチャ 127001
        MoPool = 37  # Moガチャ

    class GrandPrix:
        PlayerCountPerTeam = 32  # 各チームの人数
        GroupCount = [8, 8, 8, 8, 4, 2, 1]  # 各ステージのグループ数

    # 元々[1]に代入しようとしてる
    # class RoleCampDesc(Enum):
    #     1 = "EM"
    #     2 = "DK"
    #     3 = "IN"
    #     4 = "SW"
    #     5 = "SA"
    #     6 = "TS"
    #     7 = "CH"

    class GameHelpType(IntEnum):
        FanType = 1  # 役種
        PointCalculate = 2  # 点数計算
        Segment = 3  # セグメント
        Meeting = 4  # ミーティング
        Friend = 5  # 友人
        RoleCharging = 6  # キャラクターチャージ
        LeaderBoard = 7  # リーダーボード
        OneRoundFight = 8  # 一局戦

    class LeaderBoardRuleType(IntEnum):
        Segment = 1  # セグメント
        OnefanWeek = 2  # 一番戦週間
        YimanWeek = 3  # 役満週間
        Activity = 4  # アクティビティ

    class GameOfficeType(IntEnum):
        OfficeSelf = 1  # 自作戦
        OfficePerson = 2  # 人数戦 (毎日戦)
        OfficeTiming = 3  # 定時戦 (グランプリ)

    class RollAimType(IntEnum):
        None_ = 0  # なし
        ToIn = 1  # 入場
        ToOut = 2  # 退場
        ToInQuick = 3  # 高速入場、最後のフレームまで

    class NurturanceRedStatus(IntEnum):
        HeadFarme = 1  # ID->アバターフレームID
        Title = 2  # ID->称号ID
        Record = 3  # ID->キャラクターID*100+記録番号
        Achievement = 4  # ID->実績ID
        RoleSpecialTask = 5  # ID->キャラクターID
        ATSystem = 6  # ID-> 1, アバターフレーム、2，称号

    class AchievementType(IntEnum):
        RankingRiser = 1  # 雀道修行
        MatchConqueror = 2  # 牌海紀行
        YakuCollector = 3  # 聖天半子
        BusinessMogul = 4  # 一番大富豪
        TalesOfTheCity = 5  # 都市物語
        TeamMemories = 6  # 心躍る思い出

    class SpecialRole(IntEnum):
        AURORA = 10012  # オーロラ
        EnomiyaMio = 10016  # 榎宮澪
        LongGirl = 10024  # ロングガール

    class RoleDisplayType(IntEnum):
        None_ = 0  # なし
        OpenEye = 1  # 目を開く

    class HuSizeType(IntEnum):
        Not = 0  # なし
        One = 1  # 1翻
        Two = 2  # 2翻
        Three = 3  # 3翻
        Four = 4  # 4翻
        ManGuan = 5  # 満貫
        TiaoMan = 6  # 跳満
        BeiMan = 7  # 倍満
        ThreeBeiMan = 8  # 三倍満
        YiMan = 9  # 役満
        TwoYiMan = 10  # 二倍役満

    class EXTeamRankKind(IntEnum):
        Unknown = 0  # 不明
        NewerPlayerPT = 1  # 強豪ランキング
        OldPlayerPT = 2  # 精鋭ランキング
        MaxPoint = 3  # 気勢ランキング
        IncrExp = 4  # 応援ランキング (月間)
        MaxExp = 5  # 応援ランキング (総合)
        Reward = 6  # 純粋な報酬表示

    class EXTeamRankItemKind(IntEnum):
        Unknown = 0  # 不明
        NewerPlayerPT = 5  # 強豪ランキング
        OldPlayerPT = 4  # 精鋭ランキング
        MaxPoint = 3  # 気勢ランキング
        IncrExp = 4  # 応援ランキング (月間)
        MaxExp = 5  # 応援ランキング (総合)
        Reward = 3  # 純粋な報酬表示

    class FLHSRankTaskType(IntEnum):
        Weekly = 4  # 週間タスク
        Mounth = 5  # 月間タスク

    class FLHSPopType(IntEnum):
        PreRaceGet = 1  # 予選突破
        MatchGet = 2  # 本選突破
        MatchRace1 = 3  # 優勝おめでとう
        MatchRace2 = 4  # 準優勝おめでとう
        MatchRace3 = 5  # 3位おめでとう
        NotMatchGet = 6  # 本選進出ならず
        MatchRaceXX = 7  # 最終順位：XX位！

    class UserClickFromType(IntEnum):
        Other = 1  # その他
        RoleSendGift = 2  # キャラクターへのギフト贈呈
        RoleAwake = 3  # キャラクター覚醒
        Draw = 4  # ガチャ
        Sign = 5  # サイン

    class TwoPlayerCardType(IntEnum):
        WanZi = 1  # 萬子
        TiaoZi = 2  # 條子
        TongZi = 3  # 筒子

    class ActivityAction(IntEnum):
        HuiYiSe = 10  # 混一色を1回和了る
        QingYiSe = 11  # 清一色
        DuiDuiHe = 12  # 対々和
        LiBaoPai = 13  # 裏ドラ
        LiZhi = 14  # 立直
        FuLou = 15  # 副露
        He = 30  # 任意の場で和了る
        ZiMO = 31  # 任意の場で自摸
        Chi = 32  # 任意の場でロン
        NotChong = 33  # 任意の場で放銃しない
        HePoints = 34  # 和了点数の累計
        TongHuiYiSe = 40  # 筒子混一色で和了る
        TongQingYiSe = 41  # 筒子清一色で和了る
        HeHongWuTong = 42  # 5筒を含む和了
        HeBaoPai = 43  # ドラを含む和了
        HeYaoJiu = 44  # 役：断么九を含む和了
        HeHuiYiSeOrQingYiSe = 45  # 役：混一色または役：清一色を含む和了
        HeOneFan = 46  # 1翻の役を含む和了、ドラなしの役なし翻型は含まない
        HeGteTwoFan = 47  # 2翻以上
        HeGteManGuan = 48  # 満貫以上の和了
        TopOne = 90  # 1位を1回獲得
        TopTwo = 91  # 1位または2位を1回獲得
        StageDongFeng = 100  # 段位戦の任意の東風戦での対局
        StageDongFengHe = 101  # 段位戦の任意の東風戦での和了
        StageDongFengMan = 102  # 段位戦の任意の東風戦での満貫以上の和了
        StageDongNan = 200  # 段位戦の任意の南風戦での対局
        StageDongNanHe = 201  # 段位戦の任意の南風戦での和了
        StageDongNanMan = 202  # 段位戦の任意の南風戦での満貫以上の和了
        StageGame = 203  # 段位戦の任意の対局
        StageGameChi = 204  # 段位戦の任意の対局でのロン
        StageGameZiMo = 205  # 段位戦の任意の対局での自摸
        StageGameNo1 = 206  # 段位戦の任意の対局で1位を獲得
        StageNotChong = 207  # 段位戦で放銃しない
        Game = 208  # 対局
        OfficialMatch = 300  # 公式戦への参加
        OfficialMatchTopTwo = 301  # 公式戦への参加し、2位以上を獲得
        SendEmotion = 401  # 対局中に絵文字を送信
        SendVoice = 402  # 対局中に音声を送信
        TianHaiPlayer = 500  # 天海汐月を使用して対局
        Point50000 = 600  # 50000点以上で1位
        FriendMatchGame = 700  # 友人戦での対局
        FriendMatchVoice = 701  # 友人戦で音声を送信
        FriendMatchEmotion = 702  # 友人戦で絵文字を送信
        FriendMatchOpenShaoJi = 703  # 友人戦で焼き鳥対戦を開始
        FriendMatchOpenLuck = 704  # 友人戦で祝儀対戦を開始
        FriendMatchKaiLiZhi = 705  # 友人戦で立直を開いて和了る
        RoleFeelLevel = 800  # 九鬼蓮心または五十嵐紗子の好感度が3に達する
        RecycleItem = 801  # ギフトを粉砕回収
        RoleFeed = 802  # キャラクターに餌を与える/ギフトを贈る
        StoreCoinBuy = 803  # フクロウコインストアでアイテムを1回購入
        UseSecretCoins = 1000  # 秘密コインを使用
        ExchangeSecret = 1001  # 秘密ストアで累計
        DailyLogin = 2000  # 毎日ログイン
        FourStageGame = 2001  # 四人段位戦での対局
        ThreeStageGame = 2002  # 三人段位戦での対局
        StageSendEmotion = 2003  # 段位戦で絵文字を送信
        StageSendVoice = 2004  # 段位戦で音声を送信
        StageHe = 2005  # 段位戦で和了
        GiveLiveGift = 2006  # 配信者に投げ銭
        MakeIceCream = 2007  # デザートスタンドでアイスクリームケーキを作る
        ArenaFight = 2008  # 燃魂アリーナで戦闘に参加
        JoinCommunityDiscord = 2009  # コミュニティに参加 - Discord
        JoinCommunityOther = 2010  # コミュニティに参加 - その他
        ActivityRoleClick = 2011  # アクティビティ画面でキャラクターとインタラクション
        ActivityRollDice = 2012  # アクティビティでサイコロを振る
        ActivityVisit = 2013  # アクティビティページへのアクセス
        ActivityDailyTaskDone = 2014  # アクティビティのデイリータスクを完了
        AnniverisaryCard = 2020  # マイサークルでチェックイン
        AnniverisaryNewsLike = 2021  # ヘッドラインへのいいね
        AnniverisaryNewsCommend = 2022  # ヘッドラインへのコメント
        DailyGainMagicCrystal = 2023  # ファンタジーストーリーで魔法の水晶を獲得
        TotalGainMagicCrystal = 2024  # ファンタジーストーリーで魔法の水晶を累計獲得
        UserCherryFlower = 2025  # 桜花を消費
        VisitCherryActivity = 2026  # 桜花アクティビティ画面を開く
        StageObtainCherry = 2027  # 段位戦で桜花を獲得
        CherryDaily = 2028  # 桜花デイリーアクティビティ
        PlayLiveGame = 2029  # 海辺試練
        WheelGame = 2030  # 周年ルーレット
        OpenOneGame = 2031  # 一局戦アクティビティを開く
        JoinOneGame = 2032  # 一局戦に参加
        ExDailyAward = 2033  # デイリー報酬を受け取る
        ExContinueDailyAward = 2034  # デイリー報酬を連続で受け取る
        ExWeekTask = 2035  # 応援タスク
        TotalGainItem10042 = 2040  # 天和リコリス-非殺傷性弾丸の累計獲得
        ShniningLadderSendGift = 2081  # 天和リコリス-非殺傷性弾丸の累計獲得

    class TaskActionServer(IntEnum):
        LiZhi = 0  # 立直
        MenQingZiMO = 1  # 門前清自摸和
        YiFa = 2  # 一発
        LingShangKaihua = 3  # 嶺上開花
        HaiDiLaoYue = 4  # 海底摸月
        HeDiLaoYu = 5  # 河底撈魚
        QiangGang = 6  # 槍槓
        YiPaiZhong = 7  # 役牌 中
        YiPaiFa = 8  # 役牌 發
        YiPaiBai = 9  # 役牌 白
        YiPaiQuan = 10  # 役牌 圈風牌
        YiPaiMen = 11  # 役牌 門風牌
        YiBeiKou = 12  # 一盃口
        PingHe = 13  # 平和
        DuanYaoJiu = 14  # 断么九
        ShuangLiZhi = 15  # 両立直
        DuiDuiHe = 16  # 対々和
        QiDuiZi = 17  # 七対子
        SanAnKe = 18  # 三暗刻
        SanGangZi = 19  # 三槓子
        HuiYaoJiu = 20  # 混么九
        HuiQuanDaiYaoJiu = 21  # 混全帯么九
        YiQiTongGuan = 22  # 一気通貫
        SanSeTongShui = 23  # 三色同順
        XiaoSanYuan = 24  # 小三元
        SanSeTongKe = 25  # 三色同刻
        ChunQuanDaiYaoJiu = 26  # 純全帯么九
        HuiYiSe = 27  # 混一色
        ErBeiKou = 28  # 二盃口
        QingYiSe = 29  # 清一色
        LiuJuManGuan = 30  # 流局満貫
        TianHe = 31  # 天和
        DiHe = 32  # 地和
        RenHe = 33  # 人和
        GuoShiWuShuang = 34  # 国士無双
        GuoShiWuShuang13 = 35  # 国士無双13面待ち
        JiuLianBaoDeng = 36  # 九蓮宝燈
        ChunaJiuLianBaoDeng = 37  # 純正九蓮宝燈
        SiAnKe = 38  # 四暗刻
        SiAnKeDan = 39  # 四暗刻単騎待ち
        SiGangZi = 40  # 四槓子
        QingLaoTou = 41  # 清老頭
        ZiYiSe = 42  # 字一色
        DaSiXi = 43  # 大四喜
        XiaoSiXi = 44  # 小四喜
        DaSanYuan = 45  # 大三元
        LvYiSe = 46  # 緑一色
        ChunLvYiSe = 47  # 純緑一色
        BaLianZhuang = 48  # 八連荘
        QiBaoPai = 49  # 赤宝牌
        BaoPai = 50  # 宝牌
        LiBaoPai = 51  # 裏宝牌
        Kailizhi = 52  # 開立直
        Kaishuanglizhi = 53  # 開両立直
        Kaiyiman = 54  # 開立直役満
        PullNorth = 55  # 抜北
        MenQingHe = 98  # 門前清自摸和
        LiZHiHe = 99  # 立直和了
        StageLiZhi = 100  # 立直
        StageMenQingZiMO = 101  # 門前清自摸和
        StageYiFa = 102  # 一発
        StageLingShangKaihua = 103  # 嶺上開花
        StageHaiDiLaoYue = 104  # 海底摸月
        StageHeDiLaoYu = 105  # 河底撈魚
        StageQiangGang = 106  # 槍槓
        StageYiPaiZhong = 107  # 役牌 中
        StageYiPaiFa = 108  # 役牌 發
        StageYiPaiBai = 109  # 役牌 白
        StageYiPaiQuan = 110  # 役牌 圈風牌
        StageYiPaiMen = 111  # 役牌 門風牌
        StageYiBeiKou = 112  # 一盃口
        StagePingHe = 113  # 平和
        StageDuanYaoJiu = 114  # 断么九
        StageShuangLiZhi = 115  # 両立直
        StageDuiDuiHe = 116  # 対々和
        StageQiDuiZi = 117  # 七対子
        StageSanAnKe = 118  # 三暗刻
        StageSanGangZi = 119  # 三槓子
        StageHuiYaoJiu = 120  # 混么九
        StageHuiQuanDaiYaoJiu = 121  # 混全帯么九
        StageYiQiTongGuan = 122  # 一気通貫
        StageSanSeTongShui = 123  # 三色同順
        StageXiaoSanYuan = 124  # 小三元
        StageSanSeTongKe = 125  # 三色同刻
        StageChunQuanDaiYaoJiu = 126  # 純全帯么九
        StageHuiYiSe = 127  # 混一色
        StageErBeiKou = 128  # 二盃口
        StageQingYiSe = 129  # 清一色
        StageLiuJuManGuan = 130  # 流局満貫
        StageTianHe = 131  # 天和
        StageDiHe = 132  # 地和
        StageRenHe = 133  # 人和
        StageGuoShiWuShuang = 134  # 国士無双
        StageGuoShiWuShuang13 = 135  # 国士無双13面待ち
        StageJiuLianBaoDeng = 136  # 九蓮宝燈
        StageChunaJiuLianBaoDeng = 137  # 純正九蓮宝燈
        StageSiAnKe = 138  # 四暗刻
        StageSiAnKeDan = 139  # 四暗刻単騎待ち
        StageSiGangZi = 140  # 四槓子
        StageQingLaoTou = 141  # 清老頭
        StageZiYiSe = 142  # 字一色
        StageDaSiXi = 143  # 大四喜
        StageXiaoSiXi = 144  # 小四喜
        StageDaSanYuan = 145  # 大三元
        StageLvYiSe = 146  # 緑一色
        StageChunLvYiSe = 147  # 純緑一色
        StageBaLianZhuang = 148  # 八連荘
        StageQiBaoPai = 149  # 赤宝牌
        StageBaoPai = 150  # 宝牌
        StageLiBaoPai = 151  # 裏宝牌
        StageKailizhi = 152  # 開立直
        StageKaishuanglizhi = 153  # 開両立直
        StageKaiyiman = 154  # 開立直役
        StagePullNorth = 155  # 抜北
        He = 981  # 和了
        ActionLizhi = 982  # 立直
        ActionFuLouOrLizhi = 983  # 立直または副露
        StageHuPoint = 984  # 段位戦での和了点数の累計
        StageFuLou = 985  # 副露
        StagePoint5200 = 986  # 一回の和了で5200点以上
        StageHe = 987  # 和了
        StageContinueNotChong = 988  # 連続で放銃しない
        StageAllYiMan = 989  # 段位戦-全ての役満
        StageUpYiMan = 990  # 段位戦-役満の累計
        StageYiMan = 991  # 段位戦-役満
        StageZiMO = 992  # 段位戦-自摸
        StageChi = 993  # 段位戦-ロン
        ZiMO = 994  # 自摸
        Chi = 995  # ロン
        NotChong = 996  # 放銃しない
        HeMan = 997  # 満貫以上の和了
        MenOrQuan = 998  # 自風牌または場風牌を含む和了
        SanYuan = 999  # 三元牌を含む和了
        FourStageDongFeng = 1000  # 段位戦四人打ち任意の東風戦での対局
        FourStageDongNan = 1001  # 段位戦四人打ち任意の南風戦での対局
        ThreeStageDongFeng = 1002  # 段位戦三人打ち任意の東風戦での対局
        ThreeStageDongNan = 1003  # 段位戦三人打ち任意の南風戦での対局
        FourStageDongFengTop2 = 1004  # 段位戦四人打ち任意の東風戦で2位以上の成績を獲得
        FourStageDongNanTop2 = 1005  # 段位戦四人打ち任意の南風戦で2位以上の成績を獲得
        ThreeStageDongFengTop2 = 1006  # 段位戦三人打ち任意の東風戦で2位以上の成績を獲得
        ThreeStageDongNanTop2 = 1007  # 段位戦三人打ち任意の南風戦で2位以上の成績を獲得
        OfficialMatch = 1008  # 公式戦への参加
        OfficialMatchTop1 = 1009  # 大会戦の公式戦任意のルールで優勝
        FourStageNo1 = 1010  # 段位戦で、四人麻雀で1位を獲得
        FourStageNo2 = 1011  # 段位戦で、四人麻雀で2位を獲得
        FourStageNo3 = 1012  # 段位戦で、四人麻雀で3位を獲得
        FourStageNo4 = 1013  # 段位戦で、四人麻雀で4位を獲得
        ThreeStageNo1 = 1014  # 段位戦で、三人麻雀で1位を獲得
        ThreeStageNo2 = 1015  # 段位戦で、三人麻雀で2位を獲得
        ThreeStageNo3 = 1016  # 段位戦で、三人麻雀で3位を獲得
        DongStageNo1 = 1017  # 段位戦で、東起家で1位を獲得
        NanStageNo1 = 1018  # 段位戦で、南起家で1位を獲得
        XiStageNo1 = 1019  # 段位戦で、西起家で1位を獲得
        BeiStageNo1 = 1020  # 段位戦で、北起家で1位を獲得
        StageManGuan = 1021  # 段位戦で、満貫を和了
        StageTiaoMan = 1022  # 段位戦で、跳満を和了
        StageBeiMan = 1023  # 段位戦で、倍満を和了
        StageThreeBeiMan = 1024  # 段位戦で、三倍満を和了
        FourStage25000 = 1025  # 段位戦で、四人麻雀の最終点数が25000点以上
        FourStage50000 = 1026  # 段位戦で、四人麻雀の最終点数が50000点以上
        FourStage75000 = 1027  # 段位戦で、四人麻雀の最終点数が75000点以上
        FourStage100000 = 1028  # 段位戦で、四人麻雀の最終点数が100000点以上
        FriendMatch = 1040  # 友人戦での対局完了
        ThreeStage35000 = 1041  # 段位戦で、三人麻雀の最終点数が35000点以上
        ThreeStage70000 = 1042  # 段位戦で、三人麻雀の最終点数が70000点以上
        ThreeStage105000 = 1043  # 段位戦で、三人麻雀の最終点数が105000点以上
        StageGame = 1044  # 段位戦での対局
        StageTop2 = 1045  # 段位戦の任意の場で2位以上の成績を1回獲得
        MatchGame = 1046  # 大会戦での対局
        Game = 1047  # 任意の対局
        ThreeGame = 1048  # 三人打ちでの対局
        RoundChallenge = 1049  # 一局戦
        StageToD3 = 1050  # 段位（三人打ちまたは四人打ち）がD3に到達
        StageToD2 = 1051  # 段位（三人打ちまたは四人打ち）がD2に到達
        StageToD1 = 1052  # 段位（三人打ちまたは四人打ち）がD1に到達
        StageToC2 = 1053  # 段位（三人打ちまたは四人打ち）がC2に到達
        StageToC1 = 1054  # 段位（三人打ちまたは四人打ち）がC1に到達
        StageToB2 = 1055  # 段位（三人打ちまたは四人打ち）がB2に到達
        StageToB1 = 1056  # 段位（三人打ちまたは四人打ち）がB1に到達
        StageToA2 = 1057  # 段位（三人打ちまたは四人打ち）がA2に到達
        StageToA1 = 1058  # 段位（三人打ちまたは四人打ち）がA1に到達

        FourStageTo1 = 1300  # 段位四人打ちが初段に到達
        FourStageTo4 = 1301  # 段位四人打ちが四段に到達
        FourStageTo7 = 1302  # 段位四人打ちが七段に到達
        FourStageToLegend = 1303  # 段位四人打ちが天鳳位に到達
        ThreeStageTo1 = 1304  # 段位三人打ちが初段に到達
        ThreeStageTo4 = 1305  # 段位三人打ちが四段に到達
        ThreeStageTo7 = 1306  # 段位三人打ちが七段に到達
        ThreeStageToLegend = 1307  # 段位三人打ちが天鳳位に到達
        FourStageContTop1 = 1308  # 段位戦で、四人麻雀で連続1位を獲得
        FourStageContTop2 = 1309  # 段位戦で、四人麻雀で連続2位以上を獲得
        ThreeStageContTop1 = 1310  # 段位戦で、三人麻雀で連続1位を獲得
        ThreeStageContTop2 = 1311  # 段位戦で、三人麻雀で連続2位以上を獲得
        FourStageTop2 = 1312  # 段位戦で、四人麻雀で2位以上を獲得
        ThreeStageTop2 = 1313  # 段位戦で、三人麻雀で2位以上を獲得

        StageHeOnceAllBaoPai4 = 1330  # 段位戦で、一回の和了で4枚以上の宝牌を使用（表裏赤抜き北宝牌を含む）
        StageHeOnceAllBaoPai8 = 1331  # 段位戦で、一回の和了で8枚以上の宝牌を使用（表裏赤抜き北宝牌を含む）
        StageHeOnceAllBaoPai12 = 1332  # 段位戦で、一回の和了で12枚以上の宝牌を使用（表裏赤抜き北宝牌を含む）
        StageHeOnceAllBaoPai13 = 1333  # 段位戦で、一回の和了で13枚以上の宝牌を使用（表裏赤抜き北宝牌を含む）
        StageHeAllBaoPai = 1334  # 段位戦で、和了で使用した宝牌の枚数の累計（表裏赤抜き北宝牌を含む）
        StageKnockOut = 1335  # 段位戦で、累計飛ばした人数
        StageOnceKnockOut2 = 1336  # 段位戦で、一局で2人を同時に飛ばした
        StageShuangLiZhiChong = 1337  # 段位戦で、両立直和了せず放銃
        StageTiedNo1 = 1338  # 段位戦で、最終点数が同点で1位を獲得
        StageAllFang1 = 1339  # 段位戦で、全ての1翻役を達成
        StageAllFang2 = 1340  # 段位戦で、全ての2翻役を達成
        StageAllFang3To6 = 1341  # 段位戦で、全ての3翻から6翻の役を達成
        FourStageTurnTide = 1342  # 段位戦で、四人麻雀で4位から1位に逆転し即終局

        OfficialDaily8Top1 = 1400  # 大会戦で、四人打ち8人戦で1位を1回獲得
        OfficialDaily32Top1 = 1401  # 大会戦で、四人打ち32人戦で1位を1回獲得
        OfficialDaily9Top1 = 1402  # 大会戦で、三人打ち9人戦で1位を1回獲得
        OfficialDaily27Top1 = 1403  # 大会戦で、三人打ち27人戦で1位を1回獲得
        OfficialDailyGame = 1404  # 大会戦・毎日の大会に参加

        RoleFeed = 2001  # キャラクターに餌を与える
        RoleClick = 2002  # キャラクターとのインタラクション
        RecycleItem = 2003  # ギフトを粉砕
        ChangeRole = 2004  # 使用キャラクターを変更
        RoleIntroduce = 2005  # キャラクター紹介をクリック
        WatchGame = 2006  # 観戦
        BookMark = 2007  # 牌譜をブックマーク
        WatchRank = 2008  # ランキングを見る
        FirstRoleFeed = 2009  # キャラクターに餌を与える、初めて雀士にギフトを贈る
        ViewDrawContent = 2010  # 招待内容一覧を見る
        ViewDrawStore = 2011  # 招待ストアを見る
        ViewRoleArchive = 2012  # 雀士資料を見る
        ViewRoleVertical = 2013  # 雀士の立ち絵を見る
        ViewFeatured = 2014  # 特別おすすめを見る
        ViewFeaturedStore = 2015  # 精選ストアを見る
        ViewShopWalfare = 2016  # ショップ特典を見る
        ViewCoinStore = 2017  # フクロウコインストアを見る
        ViewStampStore = 2018  # スタンプストアを見る
        ViewTPStore = 2019  # ポイントストアを見る
        ViewOtherStore = 2020  # 雑貨店を見る
        ViewMission = 2021  # タスクを見る
        ViewMissionAward = 2022  # タスク報酬
        ViewCareerPage = 2023  # 経歴データを見る
        ViewStatsPage = 2024  # 個人データを見る
        ChangeFrame = 2025  # アバターフレームを変更
        ChangeTitle = 2026  # 称号を変更
        ViewAchievement = 2027  # 実績ホールを見る
        SaveAchievement = 2028  # スタンプ編集を保存
        ViewBadge = 2029  # スタンプコレクションを見る
        ViewShopRoleFeed = 2040  # キャラクター餌やりを見る
        ViewFangPage = 2041  # 「役一覧」を見る
        ViewCharsList = 2042  # 雀士一覧を見る
        ViewCharsOutfit = 2043  # 雀士の衣装を見る
        ViewExchange = 2044  # ショップ-交換ショップを見る
        ChangeRoleName = 2045  # 雀士の名前を変更
        SteamActivityAward = 2046  # Steam報酬を受け取る
        ChangeTilesOrTableTop = 2047  # 「麻雀台」または「牌背」を変更
        ViewRoundChallenge = 2048  # 一局戦を見る
        ViewPlayrtInfo = 2049  # 他のプレイヤーの情報を見る
        ViewMatchRule = 2050  # 大会戦ルールを見る
        NewerGiftCode = 2051  # 新人交換コード
        FriendMatchCPUGame = 2052  # 「友人戦」でCPUと対局1
        AddFriend = 2053  # 友達を1人追加
        AdjustHallRole = 2054  # ロビーキャラクターを調整
        CheckSelfProfile = 2055  # 自分のプロフィールを確認

        FeelValue100 = 2100  # 任意のキャラクターの好感度が100に到達（レベル1）
        FeelValue500 = 2101  # 任意のキャラクターの好感度が500に到達（レベル2）
        FeelValue1000 = 2102  # 任意のキャラクターの好感度が1000に到達（レベル3）
        FeelValue2000 = 2103  # 任意のキャラクターの好感度が2000に到達（レベル4）
        FeelValue5000 = 2104  # 任意のキャラクターの好感度が5000に到達（レベル5）
        DailyActiveNum50 = 2110  # デイリータスクのアクティブ宝箱値（今日の里程）が50に到達
        DailyActiveNum100 = 2111  # デイリータスクのアクティブ宝箱値（今日の里程）が100に到達
        DailyActiveNum150 = 2112  # デイリータスクのアクティブ宝箱値（今日の里程）が150に到達
        DailyActiveNum210 = 2113  # デイリータスクのアクティブ宝箱値（今日の里程）が210に到達
        Login = 3000  # ログイン
        Recharge = 3001  # チャージ
        Share = 3002  # シェア
        Draw = 3003  # ガチャ
        ObtainRole = 3004  # キャラクター獲得
        RoleAwaken = 3005  # キャラクター覚醒
        ReviewPaiPu = 3006  # 牌譜を見る
        SendEmotion = 3007  # 絵文字を使用
        SendVoice = 3008  # 音声を送信
        NewFriend = 3009  # 友達を追加

        FirstLogin = 3100  # 初回ゲームログイン
        Sign = 3101  # 累計サイン
        ContSign = 3102  # 連続サイン
        FirstObtainSkin = 3103  # 初めてスキンを獲得（覚醒スキンを含む）
        ObtainSkin = 3104  # 異なるスキンを獲得（覚醒スキンを含む）
        FirstRoleAwaken = 3105  # 初めてキャラクターを覚醒
        FirstObtainRole = 3106  # 初めて雀士を招待
        ChapterAnswer = 3017  # チャプター質問に答える
        BindEmail = 3018  # メールアドレスをバインド

        StoreCoinCost = 4000  # 金貨の累計消費
        StoreOrderComplete = 4001  # ショップ注文の購入完了
        StoreDailyBonus = 4002  # ショップでデイリー特典を受け取る

        StoreBuyVip = 4003  # 月間吉祥物を1回アクティベート
        StoreCoinBuy = 4004  # 交換ショップ-フクロウコインストアで1回購入
        StoreCoinRefresh = 4005  # 交換ショップ-フクロウコインストアで1回リフレッシュ
        StoreStampBuy = 4006  # 交換ショップ-スタンプストアで1回購入
        StorePointsBuy = 4007  # 交換ショップ-大会ポイントストアで1回購入
        StoreSundryBuy = 4008  # 交換ショップ-雑貨店で1回購入
        ObtainItem10002 = 4100  # フクロウコインの累計獲得
        ObtainTitle = 4600  # 称号の累計獲得
        ObtainAchieve = 4601  # 実績/スタンプの累計獲得

        ObtainRole10003 = 5000  # 雀士-東方凪を獲得
        ObtainRole10004 = 5001  # 雀士-九鬼蓮心を獲得
        ObtainRole10005 = 5002  # 雀士-五十嵐紗子を獲得
        ObtainRole10006 = 5003  # 雀士-天海汐月を獲得
        ObtainRole10007 = 5004  # 雀士-五月女百合香を獲得
        ObtainRole10008 = 5005  # 雀士-雅典娜を獲得
        ObtainRole10009 = 5006  # 雀士-夏海真凛を獲得
        ObtainRole10010 = 5007  # 雀士-深瀬愛麗絲を獲得
        ObtainRole10011 = 5008  # 雀士-メニアを獲得
        ObtainRole10012 = 5009  # 雀士-AU.RO.RAを獲得
        ObtainRole10013 = 5010  # 雀士-白羽飞鸟を獲得
        ObtainRole10014 = 5011  # 雀士-原道雪を獲得
        ObtainRole10015 = 5012  # 雀士-音无郁子を獲得
        ObtainRole10016 = 5013  # 雀士-榎宫澪を獲得
        ObtainRole20001 = 5500  # 雀士-雀丸を獲得
        ObtainRole20002 = 5501  # 雀士-天宫健一を獲得
        ObtainRole20003 = 5502  # 雀士-五月女直哉を獲得
        ObtainRole20004 = 5503  # 雀士-不二一气を獲得

        RoleAwaken10001 = 6000  # 雀士-一色清美を覚醒
        RoleAwaken10002 = 6001  # 雀士-三宅环奈を覚醒
        RoleAwaken10003 = 6002  # 雀士-東方凪を覚醒
        RoleAwaken10004 = 6003  # 雀士-九鬼蓮心を覚醒
        RoleAwaken10005 = 6004  # 雀士-五十嵐紗子を覚醒
        RoleAwaken10006 = 6005  # 雀士-天海汐月を覚醒
        RoleAwaken10007 = 6006  # 雀士-五月女百合香を覚醒
        RoleAwaken10008 = 6007  # 雀士-雅典娜を覚醒
        RoleAwaken10009 = 6008  # 雀士-夏海真凛を覚醒
        RoleAwaken10010 = 6009  # 雀士-深瀬愛麗絲を覚醒
        RoleAwaken10011 = 6010  # 雀士-メニアを覚醒
        RoleAwaken10012 = 6011  # 雀士-AU.RO.RAを覚醒
        RoleAwaken10013 = 6012  # 雀士-白羽飞鸟を覚醒
        RoleAwaken10014 = 6013  # 雀士-原道雪を覚醒
        RoleAwaken10015 = 6014  # 雀士-音无郁子を覚醒
        RoleAwaken10016 = 6015  # 雀士-榎宫澪を覚醒
        RoleAwaken20001 = 6500  # 雀士-雀丸を覚醒
        RoleAwaken20002 = 6501  # 雀士-天宫健一を覚醒
        RoleAwaken20003 = 6502  # 雀士-五月女直哉を覚醒
        RoleAwaken20004 = 6503  # 雀士-不二一气を覚醒

    class BodyPartType(IntEnum):
        Other = 1  # その他の位置
        Head = 2  # 頭部

    class CarteComponentType(IntEnum):
        Component1 = 100  # アバターとアバターフレーム
        Component2 = 101  # ニックネーム
        Component3 = 102  # UID
        Component4 = 201  # 段位情報
        Component5 = 202  # 展示雀士
        Component6 = 300  # アクティビティ時間
        Component7 = 301  # 好みのモード
        Component8 = 302  # 好みの役種
        Component9 = 303  # 雀風
        Component10 = 304  # 一言

    class TipWhereType(IntEnum):
        RoomSet = 1


class AwardType(IntEnum):
    Daily = 0
    Persistent = 1
    Accumulate = 2
    All = 3


class ActivityType(IntEnum):
    Sing = 0
    Game = 1
    SummerLive = 3
    ClubGuess = 4
    ClubGuess_1 = 4001
    ClubGuess_2 = 4002
    Obon = 5
    Steam = 6
    Challenge = 7
    NewerSevenDays = 8
    DrawPool = 9
    Sale = 10
    JoinCommunity = 11
    Halloween = 12
    Outfit = 13
    Xmas = 14
    Vip = 15
    XmasSkin = 16
    XmasPacket = 17
    FirstRechargeDouble = 18
    NewerChallenge = 19
    NewYear = 30
    NewYearSkin = 31
    Anniversary = 32
    AnniversarySign = 33
    AnnualReport = 34
    AnniversaryGift = 35
    AnniversaryLucky = 36
    AnniversaryCardPool = 37
    AnniversaryAllRoleSkins = 38
    AnniversaryNewSkin = 39
    NatsuumiMarinCardPool = 41
    KukiCardPool = 42
    WhiteLover = 43
    WhiteLoverGift = 45
    StageSurvey = 46
    GiftBagFox = 47
    GifBagLovely = 48
    WhiteLoverSaleSkin = 49
    AliceCardPool = 50
    ShirahaCardPool = 51
    HujiCardPool = 52
    BindMail = 53
    SaekoCardPool = 54
    CherryFestival = 55
    CherrySkin = 56
    PackCherryTime = 57
    PackCherryNight = 58
    AmamiAndKukiPool = 59
    CherrySkinCopy = 60
    TohoPool = 61
    SummerLive2023 = 62
    ChasingWavesAndSeasidePractice = 63
    SpecialLiveAndMidsummerSeaBreeze = 64
    SummerLiveDrawCardBag = 65
    MichiyukiAndIkukoPool = 66
    YurikaAndAthenaPool = 67
    SummerSkinYesterDay = 68
    NewbePool = 69
    SummerNewSkin = 70
    GrandPrixTournament = 71
    NaoYaPool = 72
    Survey = 200
    CruiseShip = 74
    BunnyGirlSkin = 75
    DrinkAndBullet = 76
    AnniversaryCopy = 77
    OneRoundFight = 78
    DrawCardPack = 80
    NatsuumiAndSaotomePool = 81
    MahjongStrongest = 83
    OneRoundPackets = 84
    ComeBack = 85
    LycorisRecoil = 86
    ShirahaCardNewPool = 88
    JanMaruPool = 89
    StarActivity = 87
    FuriousSprint = 90
    KokuraPool = 91
    SaekoAndRenshinPool = 92
    HeartJump = 93
    HeartHot = 94
    SprintFlowers = 95
    aleFSDrawGift = 96
    Role1000410005Up = 97
    LycoriQianShu = 98
    LycoriLongNai = 99
    LycoriRuiXi = 100
    LycoriHuTao = 101
    LycoriCardPool = 102
    MichiyukiShiotsukiPool = 103
    LycoriPreview = 104
    ThoughtsBgmSale = 105
    LycorisDrawCardBag = 106
    LycorisSkinSale = 107
    AliceAndMeniaUp = 108
    Halloween2023 = 109
    InviteUser = 110
    CopyNaoYaPool = 111
    MagicRealm = 112
    YurikaNewPool = 113
    HujiNewPool = 114
    YangCaiPool = 115
    Tach = 116
    YuZhu = 126
    TransPool1 = 127
    TransPool2 = 128
    TransPool3 = 129
    TransPool4 = 130
    TransPool5 = 131
    ActPackLinQi = 132
    ActPackKeLuoAi = 133
    ActPackNuoAiEr = 134
    MoShopSkin = 135
    MoCardPool = 136
    SaleHWFestive = 150
    Festivecountdown = 151
    SaleWeddingDress = 152
    KillerPrincess = 160
    YearRoundOutfits = 161
    FirstChargeReset = 162
    SaleHWDreamLand = 201
    SaleHWPurity = 202
    SaleHWCharm = 203
    SaleSkinHWCopy = 204
    FuwaMahiru = 205
    NatsuumiAndSaotome2 = 206
    SaleSkinHWNew = 207
    ShiningLadder = 208
    SaleHWCrystalClear = 209
    SaleHWBliss = 210
    CampMelee = 211
    Anniversary2Melody = 212
    Anniversary2Gift = 214
    OldTimes = 215
    YearRoundBuPo = 216
    YearRoundAlice = 217
    YearRoundXiaoCangZou = 218
    MoSign = 220
    SpecialPackBanner1 = 50001
    SpecialPackBanner2 = 50002
    SpecialPackBanner3 = 50003
    SpecialPackBanner4 = 50004
    SpecialPackBanner5 = 50005


# i18NStrからの変換
class ItemName(Enum):
    item_name_9000 = "一番割引券"
    item_name_10001 = "一番券"
    item_name_10002 = "アウル"
    item_name_10003 = "雀士スキンカード"
    item_name_10004 = "プレゼントの欠片"
    item_name_10005 = "アイテムの欠片"
    item_name_10006 = "一番街スタンプカード"
    item_name_10007 = "雀券"
    item_name_10008 = "雪花"
    item_name_10009 = "サクラ"
    item_name_10010 = "秘密コイン"
    item_name_10011 = "一番の印鑑"
    item_name_10012 = "ギフトコイン"
    item_name_10013 = "加速券"
    item_name_10014 = "ミックス粉"
    item_name_10015 = "アイスケーキ"
    item_name_10016 = "QP"
    item_name_10017 = "うちわ"
    item_name_10018 = "灯籠"
    item_name_10019 = "行動点"
    item_name_10020 = "EXP"
    item_name_10021 = "決戦コイン"
    item_name_10022 = "栄光コイン"
    item_name_10023 = "創作のヒント"
    item_name_10024 = "パンプキンランタン"
    item_name_10025 = "TP"
    item_name_10026 = "着せ替え券"
    item_name_10027 = "体力"
    item_name_10028 = "深瀬コイン"
    item_name_10029 = "星辰コイン"
    item_name_10030 = "魔素"
    item_name_10031 = "サクラ"
    item_name_10032 = "桜餅"
    item_name_10033 = "星辰Gコイン"
    item_name_10034 = "星辰ガチャポン"
    item_name_10035 = "特別推薦10連券"
    item_name_10036 = "ゴールドチップ"
    item_name_10037 = "ゴールドチケット"
    item_name_10038 = "指定地区決定戦出場権"
    item_name_10039 = "着せ替えパック2割引券（90日）"
    item_name_10040 = "メンバーポイント"
    item_name_10041 = "応援コイン"
    item_name_10042 = "非殺傷弾"
    item_name_10043 = "本週QP"
    item_name_10044 = "旗"
    item_name_10045 = "タイヤ"
    item_name_10046 = "正式キャプテン証明書"
    item_name_10047 = "カボチャ"
    item_name_10048 = "キャンディ"
    item_name_10049 = "不思議な交換チケット"
    item_name_10050 = "龍息の結晶片"
    item_name_10051 = "リズム音符"
    item_name_10052 = "ラブラブパワー"
    item_name_10053 = "工芸材料"
    item_name_10054 = "てるてる坊主"
    item_name_10055 = "Lucky Seibi"
    item_name_10500 = "優秀キャプテンの勲章"
    item_name_11001 = "マスク"
    item_name_11002 = "コーラ"
    item_name_11003 = "ミルク"
    item_name_11004 = "ラーメン"
    item_name_11005 = "すし"
    item_name_11006 = "タピオカ"
    item_name_11007 = "緑茶"
    item_name_11008 = "帽子"
    item_name_11009 = "靴"
    item_name_11010 = "すき焼き"
    item_name_11011 = "ペンダント"
    item_name_11012 = "フィギュア"
    item_name_11013 = "香水"
    item_name_11014 = "焼き肉"
    item_name_11015 = "カメラ"
    item_name_11016 = "ノートPC"
    item_name_11017 = "マスク"
    item_name_11018 = "コーラ"
    item_name_11019 = "ミルク"
    item_name_11020 = "ラーメン"
    item_name_11021 = "すし"
    item_name_11022 = "タピオカ"
    item_name_11023 = "緑茶"
    item_name_11024 = "帽子"
    item_name_11025 = "靴"
    item_name_11026 = "すき焼き"
    item_name_11027 = "ペンダント"
    item_name_11028 = "フィギュア"
    item_name_11029 = "香水"
    item_name_11030 = "焼き肉"
    item_name_11031 = "カメラ"
    item_name_11032 = "ノートPC"
    item_name_11033 = "イチゴケーキ"
    item_name_11034 = "猫のぬいぐるみ"
    item_name_11035 = "リップ"
    item_name_11036 = "抹茶プリン"
    item_name_11037 = "桜の扇子"
    item_name_11038 = "天ぷら"
    item_name_11039 = "ロリータ風ワンピ"
    item_name_11040 = "セーラー服"
    item_name_11041 = "オムライス"
    item_name_11042 = "愛のボックス"
    item_name_11043 = "伝説の戦術書"
    item_name_11044 = "ラッキースター"
    item_name_12001 = "知恵の書"
    item_name_12002 = "運命の書"
    item_name_12003 = "二択の書"
    item_name_12004 = "心境の書"
    item_name_12005 = "判断の書"
    item_name_12006 = "集中力の書"
    item_name_13001 = "立直棒・デフォルト"
    item_name_13002 = "立直棒・バット"
    item_name_13003 = "立直棒・万年筆"
    item_name_13004 = "立直棒・サーフボード"
    item_name_13005 = "立直棒・マイク"
    item_name_13006 = "立直棒・カニ"
    item_name_13007 = "立直棒・ハリセン"
    item_name_13008 = "立直棒・バナナ"
    item_name_13009 = "立直棒・ペンライト"
    item_name_13010 = "立直棒・注射器"
    item_name_13011 = "立直棒・音符"
    item_name_13012 = "立直棒・警棒"
    item_name_13013 = "立直棒・メイクブラシ"
    item_name_13014 = "立直棒・ヘアカットハサミ"
    item_name_13015 = "立直棒・チャンピオンベルト"
    item_name_13016 = "立直棒・魔法ステッキ"
    item_name_13017 = "立直棒・猫の抱き枕"
    item_name_13018 = "立直棒・アリスの鍵"
    item_name_13019 = "立直棒・夜の仮面"
    item_name_13020 = "立直棒・血呪のバッジ"
    item_name_13021 = "立直棒・縁起の白狐"
    item_name_13022 = "立直棒・大吉のくじ"
    item_name_13023 = "立直棒・桜餅"
    item_name_13024 = "立直棒・桜の匕首"
    item_name_13025 = "立直棒・手作りパッド"
    item_name_13026 = "立直棒・ミスリルダガー"
    item_name_13027 = "立直棒・みたらし団子"
    item_name_13028 = "立直棒・ホットチョコパフェ"
    item_name_13029 = "立直棒・スターライトグロス"
    item_name_13030 = "立直棒・青"
    item_name_13031 = "立直棒・赤"
    item_name_13032 = "立直棒・黒"
    item_name_13033 = "立直棒・ゴールド記念"
    item_name_13034 = "立直棒・EX風林火山"
    item_name_13035 = "立直棒・扇子"
    item_name_13036 = "立直棒・紫色のスズラン"
    item_name_13037 = "立直棒・バイオリンのブローチ"
    item_name_13038 = "立直棒・金メッキの龍のヘアピン"
    item_name_13039 = "立直棒・てるてる坊主"
    item_name_14001 = "麻雀牌・デフォルト"
    item_name_14002 = "麻雀牌・立春"
    item_name_14003 = "麻雀牌・玉子焼き"
    item_name_14004 = "麻雀牌・ドラドラ"
    item_name_14005 = "麻雀牌・ギフトケース"
    item_name_14006 = "麻雀牌・サーモン"
    item_name_14007 = "麻雀牌・スイカ"
    item_name_14008 = "麻雀牌・タイガー"
    item_name_14009 = "麻雀牌・パンダ"
    item_name_14010 = "麻雀牌・桜"
    item_name_14011 = "麻雀牌・子アザラシ"
    item_name_14012 = "麻雀牌・アザラシ"
    item_name_14013 = "麻雀牌・海の波"
    item_name_14014 = "麻雀牌・ネコちゃん"
    item_name_14015 = "麻雀牌・ネコの手"
    item_name_14016 = "麻雀牌・四つ葉のクローバー"
    item_name_14017 = "麻雀牌・謎の牌"
    item_name_14018 = "麻雀牌・魚"
    item_name_14019 = "麻雀牌・七夕祝い"
    item_name_14020 = "麻雀牌・虹色"
    item_name_14021 = "麻雀牌・光の虹"
    item_name_14022 = "麻雀牌・ユニコーン"
    item_name_14023 = "麻雀牌・縁起だるま"
    item_name_14024 = "麻雀牌・蝶々結び"
    item_name_14025 = "麻雀牌・うさぎさん"
    item_name_14026 = "麻雀牌・元気一杯ゲーマー"
    item_name_14027 = "麻雀牌・ボクシンググローブ"
    item_name_14028 = "麻雀牌・インドネシア"
    item_name_14029 = "麻雀牌・ピンク"
    item_name_14030 = "麻雀牌・黒"
    item_name_14031 = "麻雀牌・百合の花"
    item_name_14032 = "麻雀牌・無邪気な鬼"
    item_name_14033 = "麻雀牌・KA"
    item_name_14034 = "麻雀牌・ネコ"
    item_name_14035 = "麻雀牌・流れ星"
    item_name_14036 = "麻雀牌・あんぶれら"
    item_name_14037 = "麻雀牌・雪花"
    item_name_14038 = "麻雀牌・ドラゴンフルーツ"
    item_name_14039 = "麻雀牌・天海"
    item_name_14040 = "麻雀牌・ロウバイ"
    item_name_14041 = "麻雀牌・1周年の約束"
    item_name_14042 = "麻雀牌・クジラ"
    item_name_14043 = "麻雀牌・キツネちゃん"
    item_name_14044 = "麻雀牌・ハトちゃん"
    item_name_14045 = "麻雀牌・オメガ"
    item_name_14046 = "麻雀牌・雀V勝者"
    item_name_14047 = "麻雀牌・ハイビスカス"
    item_name_14048 = "麻雀牌・ピクセル"
    item_name_14049 = "麻雀牌・みかん"
    item_name_14050 = "麻雀牌・Engage Virtual"
    item_name_14051 = "麻雀牌・KeMF"
    item_name_14052 = "麻雀牌・鳥帰巣"
    item_name_14053 = "麻雀牌・鏡の花"
    item_name_14054 = "麻雀牌・天海"
    item_name_14055 = "麻雀牌・あんぶれら(人狼)"
    item_name_14056 = "麻雀牌・太陽の紋章"
    item_name_14057 = "麻雀牌・黄色"
    item_name_14058 = "麻雀牌・魔法陣"
    item_name_14059 = "麻雀牌・蟹爪"
    item_name_14060 = "麻雀牌・ゲームパッド"
    item_name_14061 = "麻雀牌・かき氷"
    item_name_14062 = "麻雀牌・プチるり"
    item_name_14063 = "麻雀牌・イーピン君"
    item_name_14064 = "麻雀牌・うさ耳"
    item_name_14065 = "麻雀牌・赤と黒"
    item_name_14066 = "麻雀牌・闇の白"
    item_name_14067 = "麻雀牌・漢気拳"
    item_name_14068 = "麻雀牌・光の黒"
    item_name_14069 = "麻雀牌・怪盗猫"
    item_name_14070 = "麻雀牌・トリオ麻雀"
    item_name_14071 = "麻雀牌・ぷ"
    item_name_14072 = "麻雀牌・月見"
    item_name_14073 = "麻雀牌・えんぺん"
    item_name_14074 = "麻雀牌・暖色"
    item_name_14075 = "麻雀牌・寒色"
    item_name_14076 = "麻雀牌・中間色"
    item_name_14077 = "麻雀牌・ロボ太の証"
    item_name_14078 = "麻雀牌・ファーストの証"
    item_name_14079 = "麻雀牌・セカンドの証"
    item_name_14080 = "麻雀牌・喫茶リコリコの証"
    item_name_14081 = "麻雀牌・伝説のハッカーの証"
    item_name_14082 = "麻雀牌・ファイアノヴァ"
    item_name_14083 = "麻雀牌・ゴールへ一直線"
    item_name_14084 = "麻雀牌・チェッカーフラッグ"
    item_name_14085 = "麻雀牌・相撲"
    item_name_14086 = "麻雀牌・誓いの指輪"
    item_name_14087 = "麻雀牌・ティーカップ"
    item_name_14088 = "麻雀牌・黒ウサギ"
    item_name_14089 = "麻雀牌・ベル"
    item_name_14090 = "麻雀牌・蝶々"
    item_name_14091 = "麻雀牌・懐かしのポルカ"
    item_name_14092 = "麻雀牌・キャロット大豊作"
    item_name_14093 = "麻雀牌・PML"
    item_name_14094 = "麻雀牌・微妙三角"
    item_name_14095 = "麻雀牌・Kson総長"
    item_name_14096 = "麻雀牌・うるプロ染専"
    item_name_14097 = "麻雀牌・PON"
    item_name_14098 = "麻雀牌・EX風林火山"
    item_name_14099 = "麻雀牌・緑色"
    item_name_14100 = "麻雀牌・山"
    item_name_14101 = "麻雀牌・雪猿"
    item_name_14102 = "麻雀牌・温泉"
    item_name_14103 = "麻雀牌・力士"
    item_name_14104 = "麻雀牌・芸妓"
    item_name_14105 = "麻雀牌・The Queen"
    item_name_14106 = "麻雀牌・天使の小道具"
    item_name_14107 = "麻雀牌・フランケン"
    item_name_14108 = "麻雀牌・ハロウィン雀V"
    item_name_14109 = "麻雀牌・トナカイもん"
    item_name_14110 = "麻雀牌・くるみ割り人形"
    item_name_14111 = "麻雀牌・輝くステージ"
    item_name_14112 = "麻雀牌・トウヒレン"
    item_name_14113 = "麻雀牌・りんご飴"
    item_name_14114 = "麻雀牌・ビール犬"
    item_name_14115 = "麻雀牌・ピンク兎"
    item_name_14116 = "麻雀牌・魔神虎"
    item_name_14117 = "麻雀牌・異次猿"
    item_name_14118 = "麻雀牌・絶凶龍"
    item_name_14119 = "麻雀牌・にじ馬"
    item_name_14120 = "麻雀牌・旅行羊"
    item_name_14121 = "麻雀牌・乾杯"
    item_name_14122 = "麻雀牌・辰"
    item_name_14123 = "麻雀牌・君のための歌"
    item_name_14124 = "麻雀牌・依存しすぎないでね"
    item_name_14125 = "麻雀牌・ベース"
    item_name_14126 = "麻雀牌・三色イナズマ"
    item_name_14127 = "麻雀牌・ほたるの傘"
    item_name_14128 = "麻雀牌・いのりの天使"
    item_name_14129 = "麻雀牌・クロエのリボン"
    item_name_14130 = "麻雀牌・ノエルのしらす"
    item_name_14131 = "麻雀牌・春月杯"
    item_name_14132 = "麻雀牌・SAKURA"
    item_name_14133 = "麻雀牌・渾沌"
    item_name_14134 = "麻雀牌・HP麻雀"
    item_name_14135 = "麻雀牌・小縁猫"
    item_name_14136 = "麻雀牌・うるたまリーグ"
    item_name_15001 = "雀卓背景・デフォルト"
    item_name_15002 = "雀卓背景・青"
    item_name_15003 = "雀卓背景・クリスマス"
    item_name_15004 = "雀卓背景・恋のプレゼント"
    item_name_15005 = "雀卓背景・二人の温泉"
    item_name_15006 = "雀卓背景・新年初夢"
    item_name_15007 = "雀卓背景・お花見"
    item_name_15008 = "雀卓背景・バニーガール"
    item_name_15009 = "雀卓背景・夏祭り"
    item_name_15010 = "雀卓背景・お菓子ガール"
    item_name_15011 = "雀卓背景・のんびり休日"
    item_name_15012 = "雀卓背景・暗闇の使者"
    item_name_15013 = "雀卓背景・勝利の喜び"
    item_name_15014 = "雀卓背景・新学期"
    item_name_15015 = "雀卓背景・夏の競技"
    item_name_15016 = "雀卓背景・星の界"
    item_name_15017 = "雀卓背景・午後の休憩時間"
    item_name_15018 = "雀卓背景・灯籠祭り"
    item_name_15019 = "雀卓背景・スナップショットタイム"
    item_name_15020 = "雀卓背景・スタートレック"
    item_name_15021 = "雀卓背景・決戦の日"
    item_name_15022 = "雀卓背景・赤"
    item_name_15023 = "雀卓背景・パープル"
    item_name_15024 = "雀卓背景・青紫"
    item_name_15025 = "雀卓背景・7日の旅"
    item_name_15026 = "雀卓背景・パンプキンの魂"
    item_name_15027 = "雀卓背景・見習い魔女"
    item_name_15028 = "雀卓背景・流れ星"
    item_name_15029 = "雀卓背景・雪合戦"
    item_name_15030 = "雀卓背景・周年祭"
    item_name_15031 = "雀卓背景・狐の日"
    item_name_15032 = "雀卓背景・恋のラッパ"
    item_name_15033 = "雀卓背景・桜吹雪"
    item_name_15034 = "雀卓背景・水の月"
    item_name_15035 = "雀卓背景・深海"
    item_name_15036 = "雀卓背景・灰色"
    item_name_15037 = "雀卓背景・海の魔法使い"
    item_name_15038 = "雀卓背景・剣道修行？"
    item_name_15039 = "雀卓背景・夕陽の光陰"
    item_name_15040 = "雀卓背景・真夏の夜の約束"
    item_name_15041 = "雀卓背景・黒"
    item_name_15042 = "雀卓背景・ev"
    item_name_15043 = "雀卓背景・新参者"
    item_name_15044 = "雀卓背景・銃と彼岸花"
    item_name_15045 = "雀卓背景・第2回トリオ麻雀"
    item_name_15046 = "雀卓背景・千束の海"
    item_name_15047 = "雀卓背景・たきなの海"
    item_name_15048 = "雀卓背景・ミズキの海"
    item_name_15049 = "雀卓背景・クルミの海"
    item_name_15050 = "雀卓背景・よそ見しないで！"
    item_name_15051 = "雀卓背景・走り通せ！"
    item_name_15052 = "雀卓背景・あの一瞬の出来事"
    item_name_15053 = "雀卓背景・ヴァーゴ"
    item_name_15054 = "雀卓背景・もちもちだんご"
    item_name_15055 = "雀卓背景・笹の夢"
    item_name_15056 = "雀卓背景・曙の合奏曲"
    item_name_15057 = "雀卓背景・儀式のドア"
    item_name_15058 = "雀卓背景・春の酒でほろ酔い"
    item_name_15059 = "雀卓背景・君と秘密の時間"
    item_name_15060 = "雀卓背景・愛の料理"
    item_name_15061 = "雀卓背景・仕事の時間"
    item_name_15062 = "雀卓背景・PML"
    item_name_15063 = "雀卓背景・EX風林火山"
    item_name_15064 = "雀卓背景・彼女のチェス"
    item_name_15065 = "雀卓背景・奪われた心"
    item_name_15066 = "雀卓背景・ガオー！"
    item_name_15067 = "雀卓背景・少し寒い冬"
    item_name_15068 = "雀卓背景・隅っこの守護者"
    item_name_15069 = "雀卓背景・汚れ無き白月"
    item_name_15070 = "雀卓背景・光陰歌の如し"
    item_name_15071 = "雀卓背景・練習は孤独なもの"
    item_name_15072 = "雀卓背景・カタオモイ"
    item_name_15073 = "雀卓背景・セッション"
    item_name_15074 = "雀卓背景・ベーシストの秘技"
    item_name_15075 = "雀卓背景・登波離橋"
    item_name_15076 = "雀卓背景・教会"
    item_name_15077 = "雀卓背景・澄空学園ゲート"
    item_name_15078 = "雀卓背景・喫茶YuKuRu"
    item_name_15079 = "雀卓背景・Whale Cup"
    item_name_15080 = "雀卓背景・エーデルワイス"
    item_name_15081 = "雀卓背景・紫金のメロディー"
    item_name_15082 = "雀卓背景・水瓶座"
    item_name_15083 = "雀卓背景・寒香の導き"
    item_name_15084 = "雀卓背景・SAKURA"
    item_name_16001 = "和了エフェクト・デフォルト"
    item_name_16002 = "和了エフェクト・竜巻"
    item_name_16003 = "和了エフェクト・勇者の剣"
    item_name_16004 = "和了エフェクト・舞台照明"
    item_name_16005 = "和了エフェクト・ネコネコ爆弾"
    item_name_16006 = "和了エフェクト・真空音爆弾"
    item_name_16007 = "和了エフェクト・無限の闇"
    item_name_16008 = "和了エフェクト・邪竜の眼"
    item_name_16009 = "和了エフェクト・星の転生"
    item_name_16010 = "和了エフェクト・陽炎の旋律"
    item_name_16011 = "和了エフェクト・ハロウィンの夜"
    item_name_16012 = "和了エフェクト・電子キューブ"
    item_name_16013 = "和了エフェクト・聖夜の贈り物"
    item_name_16014 = "和了エフェクト・水晶の花火"
    item_name_16015 = "和了エフェクト・煌めく双竜"
    item_name_16016 = "和了エフェクト・ターゲットロックオン"
    item_name_16017 = "和了エフェクト・海の怒り"
    item_name_16018 = "和了エフェクト・雨過天晴"
    item_name_17001 = "立直エフェクト・デフォルト"
    item_name_17002 = "立直エフェクト・リコリス"
    item_name_17003 = "立直エフェクト・爆ぜる火花"
    item_name_17004 = "立直エフェクト・氷雪の息吹"
    item_name_17005 = "立直エフェクト・轟く雷鳴"
    item_name_17006 = "立直エフェクト・翠の薫風"
    item_name_18001 = "BGM(ロビー)・デフォルト"
    item_name_18002 = "BGM(ロビー)・真夏の商店街"
    item_name_18003 = "BGM(ロビー)・あの夏の再現"
    item_name_18004 = "BGM(ロビー)・余暇"
    item_name_18005 = "BGM(ロビー)・聖夜の誘い"
    item_name_18006 = "BGM(ロビー)・Palpitation【期間限定】"
    item_name_19001 = "BGM(対局中)・デフォルト"
    item_name_19002 = "BGM(対局中)・ゆったりとした時間"
    item_name_19003 = "BGM(対局中)・猫とのじゃれ合い"
    item_name_19004 = "BGM(対局中)・冬のぽかぽか"
    item_name_19005 = "BGM(対局中)・勇者たちの決戦の時"
    item_name_19006 = "BGM(対局中)・暖流"
    item_name_20001 = "BGM(リーチ)・デフォルト"
    item_name_20002 = "BGM(リーチ)・勝利は目の前だ"
    item_name_20003 = "BGM(リーチ)・勇者の挑戦"
    item_name_20004 = "BGM(リーチ)・執着"
    item_name_20005 = "BGM(リーチ)・凍りついた視線"
    item_name_21001 = "改名カード"
    item_name_21002 = "サイン変更券"
    item_name_22001 = "BGM(大会戦)・デフォルト"
    item_name_24001 = "ロビー演出・デフォルト"
    item_name_24002 = "ロビー演出・雪"
    item_name_24003 = "ロビー演出・桜"
    item_name_24004 = "ロビー演出・舞い落ちる羽根"
    item_name_24005 = "ロビー演出・雨過天晴"
    item_name_24006 = "ロビー演出・雨"
    item_name_24007 = "ロビー演出・雨【期間限定】"
    item_name_25001 = "ロビー・デフォルト"
    item_name_25002 = "ロビー・雪"
    item_name_25003 = "ロビー・シンプルな部屋"
    item_name_25004 = "ロビー・クリスマスの商店街"
    item_name_26001 = "牌画・デフォルト"
    item_name_26002 = "牌画・パンプキン"
    item_name_26003 = "牌画・ワンダーハロウィン"
    item_name_26004 = "牌画・雅致"
    item_name_26005 = "牌画・壱の龍"
    item_name_30000 = "アイコンフレーム・デフォルト"
    item_name_30101 = "アイコンフレーム・決戦の剣"
    item_name_30102 = "アイコンフレーム・桜の刃"
    item_name_30103 = "アイコンフレーム・三麻宇宙飛行士"
    item_name_30104 = "アイコンフレーム・一番王"
    item_name_30105 = "アイコンフレーム・覇者の炎"
    item_name_30106 = "アイコンフレーム・魚"
    item_name_30107 = "アイコンフレーム・夏の砂浜"
    item_name_30108 = "アイコンフレーム・灯籠祭り"
    item_name_30109 = "アイコンフレーム・カラフルライフ"
    item_name_30110 = "アイコンフレーム・闘技キング"
    item_name_30111 = "アイコンフレーム・大会の使者"
    item_name_30112 = "アイコンフレーム・聖夜"
    item_name_30113 = "アイコンフレーム・新年"
    item_name_30114 = "アイコンフレーム・乱闘キング"
    item_name_30115 = "アイコンフレーム・1周年祭"
    item_name_30116 = "アイコンフレーム・友情芳草の如し"
    item_name_30201 = "アイコンフレーム・ラーメン喰うお客"
    item_name_30202 = "アイコンフレーム・ラーメン喰う達人"
    item_name_30203 = "アイコンフレーム・ラーメン喰う名人"
    item_name_30204 = "アイコンフレーム・ラーメン喰う伝説"
    item_name_30205 = "アイコンフレーム・ラーメン喰う国士"
    item_name_30206 = "月間マスコット"
    item_name_30207 = "アイコンフレーム・ラーメン喰う仙人"
    item_name_30301 = "アイコンフレーム・ヒヨコ"
    item_name_30302 = "アイコンフレーム・一番街の春"
    item_name_30303 = "アイコンフレーム・一番街の夏"
    item_name_30304 = "アイコンフレーム・一番街の秋"
    item_name_30305 = "アイコンフレーム・一番街の冬"
    item_name_30306 = "アイコンフレーム・七夕祝い"
    item_name_30307 = "アイコンフレーム・虹色"
    item_name_30308 = "アイコンフレーム・キラキラステージ"
    item_name_30401 = "アイコンフレーム・黄金の冠"
    item_name_30402 = "アイコンフレーム・麻雀の龍"
    item_name_30403 = "アイコンフレーム・猫耳イヤホン"
    item_name_30404 = "アイコンフレーム・ドラドラ"
    item_name_30405 = "アイコンフレーム・クリスマス大作戦"
    item_name_30406 = "アイコンフレーム・進む旅人"
    item_name_30407 = "アイコンフレーム・EX風林火山"
    item_name_30408 = "アイコンフレーム・輝くステージ"
    item_name_30409 = "アイコンフレーム・2024新年"
    item_name_30410 = "アイコンフレーム・春月杯"
    item_name_30411 = "アイコンフレーム・約束を守る誓い"
    item_name_30501 = "アイコンフレーム・一色清美専用"
    item_name_30502 = "アイコンフレーム・三宅環奈専用"
    item_name_30503 = "アイコンフレーム・東方凪専用"
    item_name_30504 = "アイコンフレーム・九鬼蓮心専用"
    item_name_30505 = "アイコンフレーム・五十嵐紗子専用"
    item_name_30506 = "アイコンフレーム・天海汐月専用"
    item_name_30507 = "アイコンフレーム・五月女百合香専用"
    item_name_30508 = "アイコンフレーム・赤羽アテナ専用"
    item_name_30509 = "アイコンフレーム・夏海真凜専用"
    item_name_30510 = "アイコンフレーム・深瀬アリス専用"
    item_name_30511 = "アイコンフレーム・メニヤ専用"
    item_name_30512 = "アイコンフレーム・AU.RO.RA専用"
    item_name_30513 = "アイコンフレーム・白羽飛鳥専用"
    item_name_30514 = "アイコンフレーム・原道雪専用"
    item_name_30515 = "アイコンフレーム・音無郁子専用"
    item_name_30516 = "アイコンフレーム・榎宮澪専用"
    item_name_30517 = "アイコンフレーム・錦木千束専用"
    item_name_30518 = "アイコンフレーム・井ノ上たきな専用"
    item_name_30519 = "アイコンフレーム・中原ミズキ専用"
    item_name_30520 = "アイコンフレーム・クルミ専用"
    item_name_30521 = "アイコンフレーム・小倉奏専用"
    item_name_30522 = "アイコンフレーム・不破真昼専用"
    item_name_30523 = "アイコンフレーム・犬飼陽菜専用"
    item_name_30524 = "アイコンフレーム・鈺燭専用"
    item_name_30525 = "アイコンフレーム・白河ほたる専用"
    item_name_30526 = "アイコンフレーム・陵いのり専用"
    item_name_30527 = "アイコンフレーム・嘉神川クロエ専用"
    item_name_30528 = "アイコンフレーム・嘉神川ノエル専用"
    item_name_30571 = "アイコンフレーム・雀丸専用"
    item_name_30572 = "アイコンフレーム・天宮健一専用"
    item_name_30573 = "アイコンフレーム・五月女直哉専用"
    item_name_30574 = "アイコンフレーム・不二一気専用"
    item_name_30575 = "アイコンフレーム・立花薫専用"
    item_name_31001 = "パック・夏の通常版"
    item_name_31002 = "パック・夏の豪華版"
    item_name_31003 = "パック・夏の特殊版"
    item_name_31004 = "週間パックA"
    item_name_31005 = "週間パックB"
    item_name_31006 = "月間パックA"
    item_name_31007 = "月間パックB"
    item_name_31008 = "毎日ボーナス"
    item_name_31009 = "パック・Ｘmas初回版"
    item_name_31010 = "パック・Ｘmas通常版"
    item_name_31011 = "パック・Ｘmas豪華版"
    item_name_31012 = "パック・1周年初回版"
    item_name_31013 = "パック・1周年通常版"
    item_name_31014 = "パック・1周年豪華版"
    item_name_31015 = "パック・ホワイトデー Ⅰ"
    item_name_31016 = "パック・ホワイトデー Ⅱ"
    item_name_31017 = "パック・ホワイトデー Ⅲ"
    item_name_31018 = "パック・夏の通常版"
    item_name_31019 = "パック・夏の豪華版"
    item_name_31020 = "パック・夏の特殊版"
    item_name_31021 = "特別推薦10連券"
    item_name_31022 = "育成パックA"
    item_name_31023 = "育成パックB"
    item_name_31024 = "育成パックC"
    item_name_31028 = "周年記念パックA"
    item_name_31029 = "周年記念パックB"
    item_name_31030 = "周年記念パックC"
    item_name_31031 = "Gチケパック・並"
    item_name_31032 = "Gチケパック・大"
    item_name_31033 = "Gチケパック・極"
    item_name_31034 = "カムバックパック·シンプル"
    item_name_31035 = "カムバックパック·スタンダード"
    item_name_31036 = "カムバックパック·アドバンス"
    item_name_31037 = "カムバックパック·プレミアム"
    item_name_31038 = "雀券パック・初回版"
    item_name_31039 = "雀券パック・通常版"
    item_name_31040 = "雀券パック・豪華版"
    item_name_31043 = "ゼノリンクパック・並"
    item_name_31044 = "ゼノリンクパック・大"
    item_name_31045 = "ゼノリンクパック・極"
    item_name_31046 = "料理少女物語・基礎款"
    item_name_31047 = "料理少女物語・進階款"
    item_name_31048 = "料理少女物語・特別款"
    item_name_31049 = "悦びの朝・基礎款"
    item_name_31050 = "悦びの朝・進階款"
    item_name_31051 = "悦びの朝・特別款"
    item_name_32001 = "選択パック・覚醒の本"
    item_name_32002 = "周年スペシャル雀士福袋"
    item_name_32003 = "SPギフトパック（指定）"
    item_name_33001 = "月間マスコット（30日）"
    item_name_33002 = "月間マスコット（90日）"
    item_name_33003 = "月間マスコット（180日）"
    item_name_33004 = "月間マスコット（1日）"
    item_name_34001 = "クリスマス福袋"
    item_name_34002 = "雀士福袋・ピンク"
    item_name_34003 = "雀士福袋・オレンジ"
    item_name_34004 = "雀士福袋・青"
    item_name_34005 = "アウルランダムBOX"
    item_name_34006 = "麻雀牌ランダムBOX"
    item_name_34007 = "ランダムロックギフトボックス（紫）"
    item_name_34008 = "ランダムロックギフトボックス（金）"
    item_name_34009 = "ドラのお財布"
    item_name_34010 = "ランダムギフトボックス（緑）"
    item_name_34011 = "ランダムギフトボックス（青）"
    item_name_34012 = "ランダムギフトボックス（紫）"
    item_name_34013 = "ランダムギフトボックス（金）"
    item_name_34014 = "ランダムギフトボックス（特殊）"
    item_name_34015 = "ランダムロックギフトボックス（緑）"
    item_name_34016 = "クリスマス福袋（2023）"
    item_name_34017 = "ランダムボックス"
    item_name_34018 = "住民信用ランダムボックス"
    item_name_36001 = "雀卓フレーム・デフォルトブラック"
    item_name_36002 = "雀卓フレーム・デフォルトホワイト1"
    item_name_36003 = "雀卓フレーム・デフォルトホワイト2"

    @staticmethod
    def search_by_value(itemId: int = 11001) -> str:
        try:
            return ItemName[f"item_name_{itemId}"].value
        except ValueError:
            return "not found item"
