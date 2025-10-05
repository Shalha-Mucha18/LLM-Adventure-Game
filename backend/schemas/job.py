from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class StoryJobBase(BaseModel):
    theme: str


class StoryJobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None
    
    # FIX: Use model_config instead of inner Config class
    model_config = ConfigDict(from_attributes=True)


class StoryJobCreate(StoryJobBase):
    pass