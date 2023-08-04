import uuid

from sqlalchemy import Table, Integer, String, ForeignKey, Column, MetaData
from src.auth.tables import user
from src.database_init import metadata

post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("uuid", String, unique=True, default=str(uuid.uuid4()), nullable=False),
    Column("title", String),
    Column("context", String),
    Column("creator", ForeignKey(user.c.email))
)


