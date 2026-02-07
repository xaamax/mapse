from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_URL: str
    DB_URL: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
        
        
settings: Settings = Settings()