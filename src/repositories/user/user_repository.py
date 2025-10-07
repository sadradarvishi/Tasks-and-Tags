from src.repositories.user.adapter.user_adapter import UserAdapter

from src.models.dtos.user.repository_interface_dto.user_repository_interface_dto import (
    CreateUserCommandDTO,
    ValidateUserCommandDTO,
    ValidateUserResponseDTO,
    GetUserByUsernameCommandDTO,
    GetUserByUsernameResponseDTO
)

class UserRepository:

    def __init__(self, adapter: UserAdapter):
        self._adapter = adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> None:
        await self._adapter.create_user(input_dto=input_dto)

    async def get_user_by_username(self, input_dto: GetUserByUsernameCommandDTO) -> GetUserByUsernameResponseDTO:
        return await self._adapter.get_user_by_username(input_dto=input_dto)

    async def validate_password(self, input_dto: ValidateUserCommandDTO) -> ValidateUserResponseDTO:
        await self._adapter.validate_password(input_dto=input_dto)