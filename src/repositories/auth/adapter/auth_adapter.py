from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from src.models.models.user import UserEntity
from src.models.dtos.auth.repository_interface_dto.auth_repository_interface_dto import (
    AuthResponseDTO,
    AuthCommandDTO
)

class AuthAdapter(SQLAlchemyFilterMixin):

    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter):
        self._adapter = adapter

    async def sign_in(self, input_dto: AuthCommandDTO) -> None:
        payload = input_dto.model_dump()
        entity = UserEntity(**payload)
        await self._adapter.create(entity)


