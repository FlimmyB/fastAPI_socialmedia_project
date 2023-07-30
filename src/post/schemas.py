from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    context: str
    creator: str = None


class PostUpdate(BaseModel):
    title: str
    context: str
    uuid: str
    creator: str


class PostEdit(BaseModel):
    title: str
    context: str
    uuid: str
    creator: str = None
