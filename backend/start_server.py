"""
Run the FastAPI app with correct Python path. From backend dir: python start_server.py
"""
import os
import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent
src_dir = backend_dir / "src"
os.chdir(backend_dir)
os.environ.setdefault("PYTHONPATH", str(src_dir))
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
