from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pinecone_api_key: str = ""
    pinecone_index_name: str = ""
    pinecone_namespace: str = "mem"
    model: str = "gpt-3.5-turbo"

SETTINGS = Settings()