from pydantic import BaseModel


class LikeCreate(BaseModel):
    uuid: str
    is_like: bool
    author: str


class LikeRemove(BaseModel):
    uuid: str


class LikeChange(BaseModel):
    uuid: str
    is_like: bool
