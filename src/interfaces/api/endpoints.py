from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, str | int | float]:
    return {"message": "working"}
