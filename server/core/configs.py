from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_URL: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:p3mi$Zme8r@localhost:5432/mapse_db'
    
    class Config:
        case_sensitive = True
        
        
settings: Settings = Settings()