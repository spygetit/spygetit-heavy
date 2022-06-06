import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    # noinspection PyTypeChecker
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
