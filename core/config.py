from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel



BASE_DIR = Path(__file__).parent.parent






# class AuthJWT(BaseModel):
#     private_key_path: Path = BASE_DIR / "certs" / "certs" / "jwt-private.pem"
#     public_key_path: Path = BASE_DIR / "certs" / "certs" / "jwt-public.pem"
#     # public_key_path: Path = Path("e:/projvscode/fastapi_sqlalchemy/certs/jwt-public.pem")
#     algorithm: str = "RS256"
#     # default_token_lifetime: int = 3
#     access_token_expire_minutes: int = 3
#     refresh_token_expire_days: int = 30



class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    # db_url: str = f"sqlite+aiosqlite:///{Path(__file__).parent.parent}/mydb.sqlite"
    db_url: str = "postgresql+asyncpg://postgres:matvei225CC@:5432/fastapi-users"
    db_echo: bool = True
    # auth_jwt: AuthJWT = AuthJWT()





settings = Setting()