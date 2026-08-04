from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Multi-Agent Research Assistant",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Multi-Agent Research Assistant API"
    }