from uuid import UUID
from sqlalchemy import UUID as ORM_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func, Text, ForeignKey
from datetime import datetime

from archipy.models.entities.sqlalchemy.base_entities import BaseEntity
from src.models.models.user import UserEntity


class TaskEntity(BaseEntity):

    __tablename__ = "task_entity"

    task_uuid: Mapped[UUID] = mapped_column(
        ORM_UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    owner_uuid: Mapped[UUID] = mapped_column(
        ORM_UUID(as_uuid=True),
        ForeignKey("user_entity.user_uuid", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    task_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True,
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
    owner: Mapped["UserEntity"] = relationship(back_populates="tasks")