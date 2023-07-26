import uuid

from sqlalchemy import Integer, String, Table, Column, Boolean, MetaData

metadata = MetaData()
user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("email", String, unique=True),
    Column("hashed_password", String),
    Column("is_active", Boolean),
    Column("is_superuser", Boolean),
    Column("is_verified", Boolean)
)
