from archipy.models.dtos.base_dtos import BaseDTO


class AuthCommandDTO(BaseDTO):
    firstname: str
    lastname: str
    username: str
    password: str
    phone_number: str

class AuthResponseDTO(BaseDTO):
    access_token: str
    refresh_token: str

class ValidatePasswordCommandDTO(BaseDTO):
    username: str
    password: str

class ValidatePasswordResponseDTO(BaseDTO):
    validated: bool
