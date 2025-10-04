from dependency_injector import containers, providers

from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from src.logics.auth.auth_logic import AuthLogic

class ServiceContainer(containers.DeclarativeContainer):

    postgres_adapter = providers.ThreadSafeSingleton(AsyncPostgresSQLAlchemyAdapter)

    auth_logic = providers.ThreadSafeSingleton(
        AuthLogic
    )