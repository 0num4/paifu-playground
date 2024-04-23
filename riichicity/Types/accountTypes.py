from pydantic import BaseModel
import typing

import pydantic
from . import consts


class HeaderCookies(BaseModel):
    channel: str = "default"
    lang: str = "en"
    deviceid: str
    sid: str
    uid: int
    region: str = "cn"
    platform: str = "pc"
    version: str


class Headers(BaseModel):
    User_Agent: str = "UnityPlayer/2020.3.42f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)"
    Content_Type: str = "application/json"
    Cookies: str
    Accept: str = "application/json"
    X_Unity_Version: str = "2020.3.42f1c1"  # TODO: ここが変わっていく

    # @pydantic.field_serializer("Cookies")
    # @classmethod
    # def serialize_cookies(self, c: HeaderCookies) -> str:
    #     cookieObj = HeaderCookies(**c, strict=True)
    #     return cookieObj.model_dump_json()


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
    mail: pydantic.EmailStr | typing.Literal[""]
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


class UsersInitSessionResponse(BaseModel):
    code: int
    data: str
    message: str
