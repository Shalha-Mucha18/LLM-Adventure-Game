import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Cookie, BackgroundTasks,Response
from db.database import get_db,SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from sqlalchemy.orm import Session
from schemas.story import CreateStoryRequest, CompleteStoryResponse, CompleteStoryNodeResponse
from schemas.job import StoryJobResponse
from core.llm_adapter import LLMAdapter

router = APIRouter(
    
    prefix="/story",
    tags=["stories"]

)

def get_session_id(session_id: Optional[str]= Cookie(None)):
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id


@router.post("/create", response_model = StoryJobResponse)
def create_story(

   request: CreateStoryRequest,
   background_task : BackgroundTasks,
   response : Response,
   session_id : str = Depends(get_session_id),
   db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id)

    job_id = str(uuid.uuid4())

    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme,
        status="pending",
        created_at=datetime.now()
    )
    db.add(job)
    db.commit()

    background_task.add_task(
        generate_story_task,
        job_id=job_id,
        theme=request.theme,
        session_id=session_id
    )

    return job

def generate_story_task(job_id:str, theme: str, session_id: str):
    
    db = SessionLocal()

    try: 
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
        
        try:
            job.status = "in_progress"
            db.commit()
            story = LLMAdapter.generate_story(db, session_id, theme)
            job.story_id = story.id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
        except Exception as e:
            job.status = "failed"
            job.error = str(e)
    
            db.commit()    

    finally:
        db.close()        

@router.get("/{story_id}/completed",response_model = CompleteStoryResponse)

def get_complete_story(story_id: int, db: Session = Depends(get_db)):

    story = db.query(Story).filter(Story.id == story_id).first()

    if not story:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Story not found")
    
    complete_story = build_complete_story(db,story)

    return complete_story


def build_complete_story(db: Session, story: Story):

    nodes = db.query(StoryNode).filter(StoryNode.story_id == story.id).all()

    node_dict = {}
    for node in nodes:
        # Convert options format from nextNodeId to node_id
        options = []
        if node.options:
            for option in node.options:
                options.append({
                    "text": option["text"],
                    "node_id": option.get("nextNodeId")
                })
        
        node_response = CompleteStoryNodeResponse(
            id=node.id,
            content=node.content,
            is_ending=node.is_ending,
            is_winning_ending=node.is_winning_ending,
            options=options
        )
        node_dict[node.id] = node_response

    root_node = next((node for node in nodes if node.is_root), None)
    if not root_node:
        raise HTTPException(status_code=500, detail="Story root node not found")

    return CompleteStoryResponse(
        id=story.id,
        title= story.title,
        session_id=story.session_id,
        created_at=story.created_at,
        root_node=node_dict[root_node.id],
        all_nodes=node_dict
    )

    



