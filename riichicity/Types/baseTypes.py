# baseTypes?commonTypes?とりあえずログイン系などの基盤となる型
import typing

from pydantic import BaseModel, HttpUrl


class FetchDomainNameResponse(BaseModel):
    domain_name: typing.Literal["alicdn.mahjong-jp.net"]
    is_open: bool


class CheckVersionResponseData(BaseModel):
    ApkSize: int = 0
    ApkUrl: HttpUrl
    Country: str
    DownApkUrl: str = ""
    HotUpdateUrl: HttpUrl
    IsDefaultDomain: bool
    MinVersion: str
    Version: str


class CheckVersionResponse(BaseModel):
    ApkSize: int = 0
    code: int = 0
    data: CheckVersionResponseData
    message: str


class ReceiveSignAwardResponseData(BaseModel):
    category: int
    count: int
    isVip: bool
    itemId: int


class ReceiveSignAwardResponse(BaseModel):
    awards: list[ReceiveSignAwardResponseData | None]  # 7日ログインとかはここに出てくる
    code: int
    message: str


class UserSignProgressData(BaseModel):
    isVip: bool
    persistentDay: int
    persistentStatusList: list[int]  # [3,3,1](vip)や[1,1,1]、下の方に出てるボーナス
    repairLeft: int  # 1?
    signDay: int  # ログインした日数
    signStatusList: list[int]  # 7の固定配列、ログインすると3でそれ以外は0
    vipStatus: int


class UserSignProgressResponse(BaseModel):
    code: int
    data: UserSignProgressData
    message: str
