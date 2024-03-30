# baseTypes?commonTypes?とりあえずログイン系などの基盤となる型
from pydantic import BaseModel, HttpUrl
import typing


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
