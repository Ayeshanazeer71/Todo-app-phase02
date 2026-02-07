"""
Vercel serverless entry for FastAPI.
Deploy with Root Directory = backend. All requests are routed here.
"""
import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
src_dir = backend_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from app.main import app

# Vercel Python runtime looks for an ASGI app named "app" at this entrypoint.
