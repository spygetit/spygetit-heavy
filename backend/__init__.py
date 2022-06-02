import uvicorn

from .main import app


def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)
