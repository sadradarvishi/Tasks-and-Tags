from passlib.context import CryptContext

from archipy.helpers.utils.jwt_utils import JWTUtils
from src.security.passwords import pwd_context
from src.repositories.auth.auth_repository import AuthRepository
from src.repositories.user.user_repository import UserRepository
from src.models.dtos.auth.domain_iterrface_dto.v1.auth_domain_iterface_dto import (
    SigninInputDTOV1,
    SigninOutputDTOV1,
    SignupInputDTOV1,
    ValidatePasswordInputDTOV1,
    ValidatePasswordOutputDTOV1,
    GetUserByUsernameInputDTOV1,
    GetUserByUsernameOutputDTOV1
)
from src.models.dtos.auth.repository_interface_dto.auth_repository_interface_dto import (
    AuthCommandDTO,
)
from src.models.dtos.user.repository_interface_dto.user_repository_interface_dto import (
    CreateUserCommandDTO,
    GetUserByUsernameCommandDTO
)

class AuthLogic:

    def __init__(
            self,
            auth_repository: AuthRepository,
            user_repository: UserRepository
    ):
        self._repository = auth_repository
        self._user_repository = user_repository

    async def sign_up(self, input_dto: SignupInputDTOV1) -> None:

        hashed_password = pwd_context.hash(input_dto.password)

        input_dto = CreateUserCommandDTO(
        firstname=input_dto.firstname,
        lastname=input_dto.lastname,
        username=input_dto.username,
        password=hashed_password,
        phone_number=input_dto.phone_number,
        )
        await self._user_repository.create_user(input_dto=input_dto)

    async def validate_password(self, input_dto: ValidatePasswordInputDTOV1) -> ValidatePasswordOutputDTOV1:
        user_input_dto = GetUserByUsernameCommandDTO(username=input_dto.username)
        user = await self._user_repository.get_user_by_username(user_input_dto)

        check_hash_password = pwd_context.verify_and_update(input_dto.password, user.password)

        if check_hash_password:
            return ValidatePasswordOutputDTOV1(validated=True)
        else:
            return ValidatePasswordOutputDTOV1(validated=False)




    async def sign_in(self, input_dto: SigninInputDTOV1) -> SigninOutputDTOV1:
        validate_pass_dto = ValidatePasswordInputDTOV1(
            username=input_dto.username,
            password=input_dto.password
        )

        validate_password = await self.validate_password(validate_pass_dto)

        user_input_dto = GetUserByUsernameCommandDTO(username=input_dto.username)

        user = await self._user_repository.get_user_by_username(user_input_dto)

        if validate_password:
            access_token: str =  JWTUtils.create_access_token(user_uuid=user.user_uuid)
            refresh_token: str =  JWTUtils.create_refresh_token(user_uuid=user.user_uuid)

            return SigninOutputDTOV1(access_token=access_token, refresh_token=refresh_token)

        else:
            return None