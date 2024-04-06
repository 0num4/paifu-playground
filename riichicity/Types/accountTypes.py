from pydantic import BaseModel
import typing
from . import consts


class PingResponse(BaseModel):
    code: int
    data: typing.Literal["post pong"]
    message: typing.Literal["ok"]


class UserGetLastLoginResponseData(BaseModel):
    isAdidTwitter: bool
    tokenType: consts.EnumDefine.UserTokenType


class UserGetLastLoginResponse(BaseModel):
    code: int
    data: UserGetLastLoginResponseData
    message: str
