import uvicorn
from fastapi import FastAPI
from database import engine
import models
from routes import tasks, health


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(tasks.router)
app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)