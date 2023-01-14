from fastapi import FastAPI

from config import env, events
from routes import root_route

app = FastAPI(
    title="Auth Service",
    version="0.0.0",
    docs_url="/api/v1/docs/",
    redoc_url="/api/v1/redocs/",
    on_startup=events.on_startup(),
    on_shutdown=events.on_shutdown(),
    debug=env.DEBUG,
)

app.include_router(root_route.router)
