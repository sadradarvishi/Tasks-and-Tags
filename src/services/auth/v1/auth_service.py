from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.configs.container import ServiceContainer
from src.models.dtos.auth.domain_iterrface_dto.v1.auth_domain_iterface_dto import (
    SigninInputDTOV1,
    SigninOutputDTOV1,
    SignupInputDTOV1
)
from src.logics.auth.auth_logic import AuthLogic

routerV1 = APIRouter(tags=["auth"])


@routerV1.post(
    path="/auth/signup"
)
@inject
async def sign_up(
    auth_input_dto: SignupInputDTOV1,
    logic: AuthLogic = Depends(Provide[ServiceContainer.auth_logic])
) -> None:
    input_dto = SignupInputDTOV1(
        firstname=auth_input_dto.firstname,
        lastname=auth_input_dto.lastname,
        username=auth_input_dto.username,
        password=auth_input_dto.password,
        phone_number=auth_input_dto.phone_number,
    )

    await logic.sign_up(input_dto)


@routerV1.post(
    path="/auth/sign_in"
)
@inject
async def sign_in(
        sing_in_input_dto: SigninInputDTOV1,
        logic: AuthLogic = Depends(Provide[ServiceContainer.auth_logic])
) -> SigninOutputDTOV1:
    input_dto = SigninInputDTOV1(
        username=sing_in_input_dto.username,
        password=sing_in_input_dto.password
    )

    await logic.sign_in(input_dto)