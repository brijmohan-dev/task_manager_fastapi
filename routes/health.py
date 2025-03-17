from fastapi import APIRouter
from database import db_dependency
from sqlalchemy.sql import text
import logging

router = APIRouter(
    prefix='/health',
    tags=['health']
)

# Health check router
@router.get("/")
async def health_check(db: db_dependency):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as error:
        logging.error('Error while health check', error)
        return {"status": "unhealthy"}