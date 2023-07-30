from sqlalchemy import Table, MetaData, Column, Integer, ForeignKey, String, Boolean

from auth.tables import user
from post.tables import post

metadata = MetaData()
like = Table(
    "like",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("author", String, ForeignKey(user.c.email)),
    Column("post", String, ForeignKey(post.c.uuid)),
    Column("is_like", Boolean)
)
