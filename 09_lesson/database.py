from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), nullable=False, unique=True),
)