from src.repositories.user.adapter.user_adapter import UserAdapter
from src.models.dtos.auth.repository_interface_dto.auth_repository_interface_dto import (
    AuthCommandDTO,
    AuthResponseDTO,
    ValidatePasswordCommandDTO,
    ValidatePasswordResponseDTO
)
from src.models.dtos.user.repository_interface_dto.user_repository_interface_dto import (
    CreateUserCommandDTO
)

class AuthRepository:

    def __init__(
            self,
            user_postgres_adapter: UserAdapter,
    ):
        self._user_postgres_adapter = user_postgres_adapter

    async def sign_up(self, input_dto: CreateUserCommandDTO) -> None:
        await self._user_postgres_adapter.create_user(input_dto=input_dto)