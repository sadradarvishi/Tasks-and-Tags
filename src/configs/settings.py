from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Use RS256 for multi-service deployments; HS256 is fine for single service.
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = Field(..., env="JWT_SECRET")    # for HS256
    # If you use RS256, load key pair:
    # JWT_PRIVATE_KEY: str = Field(..., env="JWT_PRIVATE_KEY")
    # JWT_PUBLIC_KEY: str = Field(..., env="JWT_PUBLIC_KEY")

    ACCESS_TOKEN_MIN: int = 15         # access TTL: 15 minutes
    REFRESH_TOKEN_DAYS: int = 30       # refresh TTL: 30 days
    ISSUER: str = "my-api"
    AUDIENCE: str = "my-web"

    class Config:
        env_file = ".env"

settings = Settings()
