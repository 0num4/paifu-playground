from typing import List, Optional


class HandEventRecord:
    def __init__(self, data: str, eventPos: int, eventType: int, handId: str, startTime: int, userId: int):
        self.data = data
        self.eventPos = eventPos
        self.eventType = eventType
        self.handId = handId
        self.startTime = startTime
        self.userId = userId


class HandRecord:
    def __init__(
        self,
        benChangNum: int,
        changCi: int,
        handCardEncode: str,
        handCardsSHA256: str,
        handEventRecord: List[HandEventRecord],
        handID: str,
        handPos: int,
    ):
        self.benChangNum = benChangNum
        self.changCi = changCi
        self.handCardEncode = handCardEncode
        self.handCardsSHA256 = handCardsSHA256
        self.handEventRecord = [HandEventRecord(**her) for her in handEventRecord]
        self.handID = handID
        self.handPos = handPos


class Player:
    def __init__(
        self,
        cardBackID: int,
        gameMusicId: int,
        headTag: int,
        identity: int,
        matchMusicId: int,
        model: int,
        nickname: str,
        points: int,
        position: int,
        profileFrameId: int,
        riichiEffectID: int,
        riichiMusicId: int,
        riichiStickID: int,
        roleID: int,
        skinID: int,
        specialEffectID: int,
        tableclothID: int,
        titleID: int,
        userId: int,
    ):
        self.cardBackID = cardBackID
        self.gameMusicId = gameMusicId
        self.headTag = headTag
        self.identity = identity
        self.matchMusicId = matchMusicId
        self.model = model
        self.nickname = nickname
        self.points = points
        self.position = position
        self.profileFrameId = profileFrameId
        self.riichiEffectID = riichiEffectID
        self.riichiMusicId = riichiMusicId
        self.riichiStickID = riichiStickID
        self.roleID = roleID
        self.skinID = skinID
        self.specialEffectID = specialEffectID
        self.tableclothID = tableclothID
        self.titleID = titleID
        self.userId = userId


class GameData:
    def __init__(self, code: int, data: dict):
        self.code = code
        self.players = [Player(**player) for player in data.get("players", [])]
        self.handRecords = [HandRecord(**handRecord) for handRecord in data.get("handRecord", [])]
