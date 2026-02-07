import logging
from typing import Generator
from sqlmodel import Session, create_engine
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from ..core.config import settings

logger = logging.getLogger(__name__)

if settings.DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=False,
    )
else:
    parsed = urlparse(settings.DATABASE_URL)
    query_params = parse_qs(parsed.query)
    if "channel_binding" in query_params:
        del query_params["channel_binding"]
    new_query = urlencode(query_params, doseq=True)
    cleaned_url = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        new_query,
        parsed.fragment,
    ))
    engine = create_engine(
        cleaned_url,
        pool_pre_ping=True,
        pool_recycle=300,
        echo=False,
    )
    try:
        with engine.connect() as conn:
            logger.info("PostgreSQL connection OK")
    except Exception as e:
        logger.error(f"PostgreSQL connection failed: {e}")
        raise

def get_db() -> Generator:
    with Session(engine) as session:
        yield session
