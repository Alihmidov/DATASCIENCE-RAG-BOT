from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str 
    EMBEDDING_MODEL: str 
    CHROMA_PATH: str 
    CHUNK_SIZE: int 
    CHUNK_OVERLAP: int 
    OLLAMA_BASE_URL: str
    LLM_MODEL: str
    PROJECT_NAME: str
    DEBUG: bool

    class Config:
        env_file = ".env"
        
settings = Settings()