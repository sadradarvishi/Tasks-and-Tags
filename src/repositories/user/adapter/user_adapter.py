from archipy.models.types import FilterOperationType
from sqlalchemy import select
from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from src.models.models.user import UserEntity
from src.models.dtos.user.repository_interface_dto.user_repository_interface_dto import (
    CreateUserCommandDTO,
    ValidateUserCommandDTO,
    ValidateUserResponseDTO,
    GetUserByUsernameCommandDTO,
    GetUserByUsernameResponseDTO,
    GetUserByUsernameDTO
)

class UserAdapter(SQLAlchemyFilterMixin):

    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter):
        self._adapter = adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> None:
        payload = input_dto.model_dump()
        entity = UserEntity(**payload)
        await self._adapter.create(entity)

    async def get_user_by_username(self, input_dto: GetUserByUsernameCommandDTO) -> GetUserByUsernameResponseDTO:
        query = (
            select(UserEntity)
        )

        query = self._apply_filter(
            query=query,
            field=UserEntity.username,
            value=input_dto.username,
            operation=FilterOperationType.EQUAL
        )

        entity = (await self._adapter.scalars(query)).one_or_none()

        dto = GetUserByUsernameDTO(
            firstname=entity.firstname,
            lastname=entity.lastname,
            username=entity.username,
            phone_number=entity.phone_number
        )



        return GetUserByUsernameResponseDTO(
            user=dto
        )




    async def validate_password(self, input_dto: ValidateUserCommandDTO) -> ValidateUserResponseDTO:


    async def validate_user(self, filters: ValidateUserCommandDTO) -> ValidateUserResponseDTO:
        query = (
            select(UserEntity)
            .where(
                UserEntity.username == filters.username
            )
        )


