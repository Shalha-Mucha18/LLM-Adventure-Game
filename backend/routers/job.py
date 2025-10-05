import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Cookie, BackgroundTasks,Response
from db.database import get_db,SessionLocal

from models.job import StoryJob
from sqlalchemy.orm import Session
from schemas.job import StoryJobResponse


router = APIRouter(
    
    prefix="/job",
    tags=["jobs"]

)

@router.get("/{job_id}",response_model = StoryJobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    
    return job