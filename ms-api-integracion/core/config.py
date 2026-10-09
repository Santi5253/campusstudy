from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tareas_url: str = "http://localhost:8001"
    grupos_url: str = "http://localhost:8002"
    estadisticas_url: str = "http://localhost:8003"
    notificaciones_url: str = "http://localhost:8004"
    usuarios_url: str = "http://localhost:8005"
    materias_url: str = "http://localhost:8006"
    jwt_secret: str = "cambiar-en-produccion"
    request_timeout: float = 5.0

    class Config:
        env_file = ".env"

settings = Settings()
