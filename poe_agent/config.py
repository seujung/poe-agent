from starlette.config import Config

config = Config(".env")
API_KEY = config("API_KEY", cast=str, default="")