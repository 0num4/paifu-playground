import json

from pydantic import BaseModel, Field


# 最初の型
class OriginalLobbysReadStageClassifiesResponseUserInfoStage(BaseModel):
    isRedDot: bool
    rValue: int
    stageLevel: int
    stageNextPt: int
    stagePt: int
    timingStart: int


class OriginalLobbysReadStageClassifiesResponseUserInfo(BaseModel):
    player_3: OriginalLobbysReadStageClassifiesResponseUserInfoStage = None
    player_4: OriginalLobbysReadStageClassifiesResponseUserInfoStage = None

    class Config:
        fields = {"player_3": "3", "player_4": "4"}


class OriginalLobbysReadStageClassifiesResponse(BaseModel):
    code: int
    data: None
    message: str
    userInfo: OriginalLobbysReadStageClassifiesResponseUserInfo


# 提案された型
class ProposedLobbysReadStageClassifiesResponseUserInfoStage(BaseModel):
    isRedDot: bool
    rValue: int
    stageLevel: int
    stageNextPt: int
    stagePt: int
    timingStart: int


class ProposedLobbysReadStageClassifiesResponseUserInfo(BaseModel):
    player_3: ProposedLobbysReadStageClassifiesResponseUserInfoStage = Field(None, alias="3")
    player_4: ProposedLobbysReadStageClassifiesResponseUserInfoStage = Field(None, alias="4")


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


class ProposedLobbysReadStageClassifiesResponse(BaseModel):
    code: int
    data: list[LobbysReadStageClassifiesResponseData]
    message: str
    userInfo: ProposedLobbysReadStageClassifiesResponseUserInfo


# テストコード
def test_lobbys_read_stage_classifies_response_equality(input: dict):

    # original_response = OriginalLobbysReadStageClassifiesResponse(**input)
    proposed_response = ProposedLobbysReadStageClassifiesResponse(**input)
    # original_response_dict = original_response.model_dump()
    proposed_response_dict = proposed_response.model_dump()
    # print(original_response_dict)
    print(proposed_response_dict)
    # assert original_response_dict == proposed_response_dict
    # assert original_response.model_dump() == proposed_response.model_dump()


# test_lobbys_read_stage_classifies_response_equality(
#     input={
#         "code": 0,
#         "data": None,
#         "message": "Success",
#         "userInfo": {
#             "3": {
#                 "isRedDot": False,
#                 "rValue": 100,
#                 "stageLevel": 1,
#                 "stageNextPt": 200,
#                 "stagePt": 150,
#                 "timingStart": 1620000000,
#             },
#             "4": {
#                 "isRedDot": True,
#                 "rValue": 200,
#                 "stageLevel": 2,
#                 "stageNextPt": 300,
#                 "stagePt": 250,
#                 "timingStart": 1620000000,
#             },
#         },
#     }
# )
json_str = open("lobbys_read_stage_classifies.json", "r").read()
# print(json_str)
test_lobbys_read_stage_classifies_response_equality(json.loads(json_str))
print("テストが成功しました")
