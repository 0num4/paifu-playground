import pydantic
from pydantic import BaseModel, HttpUrl
import typing


class PingResponse(BaseModel):
    code: int
    data: typing.Literal["post pong"]
    message: typing.Literal["ok"]
