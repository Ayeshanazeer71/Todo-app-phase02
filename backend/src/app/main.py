import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from .api.deps import engine
from .api.tasks import router as tasks_router
from .api.auth.router import router as auth_router
from .core.config import settings as app_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_and_tables():
    logger.info("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created")

app = FastAPI(title="Phase II Todo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    logger.info("Starting FastAPI application...")
    try:
        create_db_and_tables()
        from sqlmodel import text
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database connection OK")
    except Exception as e:
        logger.error(f"Database startup error: {e}", exc_info=True)
        raise

app.include_router(tasks_router, prefix="/api/tasks", tags=["tasks"])
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

@app.get("/health")
def health():
    return {"status": "ok"}

# Ensure tables exist on serverless cold start (e.g. Vercel)
try:
    create_db_and_tables()
except Exception as e:
    logger.warning(f"Table creation on load (non-fatal): {e}")
