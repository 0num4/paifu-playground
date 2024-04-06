from pydantic import BaseModel
import typing

import pydantic
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


class UsersRetrieveAccountResponseData(BaseModel):
    mail: pydantic.EmailStr
    nickname: str
    profileFrameId: int
    roleID: int
    roleModule: int
    skinID: int
    uidStr: str


class UsersRetrieveAccountResponse(BaseModel):
    code: int
    data: UsersRetrieveAccountResponseData
    message: str
