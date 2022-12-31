from starlette.config import Config

config = Config(".env")

PROJECT_NAME = config("PROJECT_NAME",cast=str,default="PROJECT HERE")

LOGGING_CONF = config("LOGGING_CONF",cast=str,default="logging.yml")

POSTGRES_URL = config("POSTGRES_URL",cast=str,default="postgresql+asyncpg://postgres:123456@localhost:5432/musicc")

REDIS_URL = config("REDIS_URL",cast=str,default="")

JWT_SECRET = config("JWT_SECRET",cast=str,default="jwt_secret_example")
JWT_METHOD = config("JWT_METHOD",cast=str,default="HS256")
JWT_EXPIRE = config("JWT_EXPIRE",cast=int,default=24*60) # 1 day

