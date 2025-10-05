from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import story, job
from core.config import setting
from db.database import create_tables
from models import story as story_models, job as job_models

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="api to generate cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix=setting.API_PREFIX)
app.include_router(job.router, prefix=setting.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)


