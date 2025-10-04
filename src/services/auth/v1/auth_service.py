from fastapi import APIRouter

from src.models.dtos.auth.domain_iterrface_dto.v1.auth_domain_iterface_dto import (
    AuthInputDTOV1,
    AuthOutputDTOV1,
    SigninInputDTOV1,
    SigninOutputDTOV1
)
from src.logics.auth.auth_logic import AuthLogic

routerV1 = APIRouter(tags=["auth"])


@routerV1.post(
    path="/auth/signup"
)
async def sign_up(
    auth_input_dto: AuthInputDTOV1,
    logic: AuthLogic
) -> AuthOutputDTOV1:
    input_dto = AuthInputDTOV1(
        firstname=auth_input_dto.firstname,
        lastname=auth_input_dto.lastname,
        username=auth_input_dto.username,
        password=auth_input_dto.password,
        phone_number=auth_input_dto.phone_number,
    )

    return await logic.sign_up(input_dto)


@routerV1.post(
    path="/auth/sign_in"
)
async def sign_in(
        sing_in_input_dto: SigninInputDTOV1
) -> SigninOutputDTOV1:
    input_dto = SigninInputDTOV1(
        username=sing_in_input_dto.username,
        password=sing_in_input_dto.password
    )