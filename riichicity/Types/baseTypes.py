# baseTypes?commonTypes?とりあえずログイン系などの基盤となる型
from pydantic import BaseModel
import typing


class FetchDomainNameResponse(BaseModel):
    domain_name: typing.Literal["alicdn.mahjong-jp.net"]
    is_open: bool
