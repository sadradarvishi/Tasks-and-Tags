from typing import List
from uuid import UUID
from archipy.models.dtos.base_dtos import BaseDTO

class CreateUserCommandDTO(BaseDTO):
    firstname: str
    lastname: str
    username: str
    password: str
    phone_number: str

class GetUserByUsernameDTO(BaseDTO):
    firstname: str
    lastname: str
    username: str
    phone_number: str

class GetUserByUsernameCommandDTO(BaseDTO):
    username: str

class GetUserByUsernameResponseDTO(BaseDTO):
    user: GetUserByUsernameDTO | None

class ValidateUserCommandDTO(BaseDTO):
    username: str
    password: str

class ValidateUserResponseDTO(BaseDTO):
    validated: bool