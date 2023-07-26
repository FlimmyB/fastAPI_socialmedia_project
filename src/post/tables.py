import uuid

from sqlalchemy import Table, Integer, String, ForeignKey, Column, MetaData
from auth.tables import user

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("uuid", String, unique=True, default=str(uuid.uuid4()), nullable=False),
    Column("title", String),
    Column("context", String),
    Column("creator", ForeignKey(user.c.email))
)
like = Table(
    "like",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("from", String, ForeignKey(user.c.email)),
    Column("to", String, ForeignKey(post.c.uuid)),
)
