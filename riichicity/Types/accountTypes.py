import pydantic
from pydantic import BaseModel, HttpUrl
import typing


class PingResponse(BaseModel):
    code: int
    data: typing.Literal["post pong"]
    message: typing.Literal["ok"]


class UserGetLastLoginResponseData(BaseModel):
    isAdidTwitter: bool
    tokenType: int


class UserGetLastLoginResponse(BaseModel):
    code: int
    data: UserGetLastLoginResponseData
    message: str
