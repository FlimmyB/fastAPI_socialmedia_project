from fastapi import FastAPI

from auth.base_config import fastapi_user, auth_backend
from auth.user_schema import UserCreate, UserRead
from post.router import router as post_router
from like.router import router as like_router

app = FastAPI(title="FastAPI social app")

app.include_router(
    fastapi_user.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_user.get_register_router(UserRead, UserCreate)
)

app.include_router(post_router)
app.include_router(like_router)
