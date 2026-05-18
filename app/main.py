from fastapi import FastAPI
from app.routers import tasks

## temporary
from app.database import Base, engine
from app.models import TaskModel

Base.metadata.create_all(bind=engine)
## Until here

app = FastAPI(title="Task API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(tasks.router)