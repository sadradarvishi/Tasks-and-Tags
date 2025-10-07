from dependency_injector import containers, providers

from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from src.logics.auth.auth_logic import AuthLogic
from src.repositories.auth.auth_repository import AuthRepository
from src.repositories.user.user_repository import UserRepository
from src.repositories.user.adapter.user_adapter import UserAdapter
from src.repositories.auth.adapter.auth_adapter import AuthAdapter

class ServiceContainer(containers.DeclarativeContainer):

    postgres_adapter = providers.ThreadSafeSingleton(AsyncPostgresSQLAlchemyAdapter)

    auth_postgres_adapter = providers.ThreadSafeSingleton(
        AuthAdapter,
        adapter=postgres_adapter
    )

    user_postgres_adapter = providers.ThreadSafeSingleton(
        UserAdapter,
        adapter=postgres_adapter
    )

    user_repository = providers.ThreadSafeSingleton(
        UserRepository,
        adapter=user_postgres_adapter
    )

    auth_repository = providers.ThreadSafeSingleton(
        AuthRepository,
        user_postgres_adapter=auth_postgres_adapter
    )

    auth_logic = providers.ThreadSafeSingleton(
        AuthLogic,
        auth_repository=auth_repository,
        user_repository=user_repository
    )