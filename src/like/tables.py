from sqlalchemy import Table, MetaData, Column, Integer, ForeignKey, String, Boolean

from src.auth.tables import user
from src.post.tables import post
from src.database_init import metadata

like = Table(
    "like",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("author", String, ForeignKey(user.c.email)),
    Column("post", String, ForeignKey(post.c.uuid)),
    Column("is_like", Boolean)
)
