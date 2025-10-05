from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
import os
from pathlib import Path

class Settings(BaseSettings):
   model_config = SettingsConfigDict(
      env_file=Path(__file__).parent.parent / ".env",
      env_file_encoding="utf-8",
      case_sensitive=True
   )
   
   API_PREFIX: str = "/api"
   DEBUG: bool = False
   DATABASE_URL: str
   ALLOWED_ORIGINS: str = ""
   GROQ_API_KEY: str

   @field_validator("ALLOWED_ORIGINS")
   def parse_allowed_origins(cls,v: str) -> List[str]:
      return v.split(",") if v else []

setting = Settings()      
         