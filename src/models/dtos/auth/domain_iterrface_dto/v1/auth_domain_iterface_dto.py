from uuid import UUID
from archipy.models.dtos.base_dtos import BaseDTO

class SignupInputDTOV1(BaseDTO):
    firstname: str
    lastname: str
    username: str
    password: str
    phone_number: str

class SigninInputDTOV1(BaseDTO):
    username: str
    password: str

class SigninOutputDTOV1(BaseDTO):
    access_token: str
    refresh_token: str

class ValidatePasswordInputDTOV1(BaseDTO):
    username: str
    password: str

class ValidatePasswordOutputDTOV1(BaseDTO):
    validated: bool
