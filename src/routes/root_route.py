from fastapi import APIRouter

from routes import user_route

router = APIRouter(prefix="/api/v1")

router.include_router(user_route.router)
