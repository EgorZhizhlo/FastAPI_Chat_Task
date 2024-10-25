from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    first_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    phone_number: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    extend_existing = True
