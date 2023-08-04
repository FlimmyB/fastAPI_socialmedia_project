from fastapi import FastAPI
from src.auth.base_config import fastapi_user, auth_backend
from src.auth.user_schema import UserCreate, UserRead
from src.post.router import router as post_router
from src.like.router import router as like_router
from src.pages.router import router as pages_router

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
app.include_router(pages_router)
