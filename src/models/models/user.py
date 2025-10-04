from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime, func
from uuid import UUID
from sqlalchemy import UUID as ORM_UUID
from datetime import datetime
from typing import List

from archipy.models.entities.sqlalchemy.base_entities import BaseEntity
from src.models.models.task import TaskEntity

class UserEntity(BaseEntity):

    __tablename__ = "user_entity"

    user_uuid: Mapped[UUID] = mapped_column(
        ORM_UUID(as_uuid=True),
        primary_key=True,
    )

    firstname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    lastname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )




    # --- relationship side ---
    tasks: Mapped[List["TaskEntity"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
        passive_deletes=True
    )




