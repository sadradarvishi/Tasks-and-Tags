from archipy.models.dtos.base_dtos import BaseDTO


class AuthInputDTOV1(BaseDTO):
    firstname: str
    lastname: str
    username: str
    password: str
    phone_number: str

class AuthOutputDTOV1(BaseDTO):
    access_token: str
    refresh_token: str

class SigninInputDTOV1(BaseDTO):
    username: str
    password: str

class SigninOutputDTOV1(BaseDTO):
    access_token: str
    refresh_token: str

