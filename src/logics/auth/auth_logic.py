

class AuthLogic:

    def __init__(
            self,
            repository
    ):
        self._repository = repository

    async def sign_up(self, input_dto):
