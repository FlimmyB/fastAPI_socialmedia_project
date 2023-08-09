from fastapi import FastAPI, APIRouter, Depends

from src.auth.user_manager import UserManager, get_user_manager
from src.auth.base_config import fastapi_user, auth_backend
from src.auth.user_schema import UserCreate, UserRead, UserUpdate
from src.post.router import router as post_router
from src.like.router import router as like_router
from src.pages.router import router as pages_router

app = FastAPI(title="FastAPI social app")

app.include_router(
    fastapi_user.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(post_router)
app.include_router(like_router)
app.include_router(pages_router)
app.include_router(fastapi_user.get_users_router(UserCreate, UserUpdate, requires_verification=False),
                   prefix="/users",
                   tags=["users"])
test_router = APIRouter(prefix="/test", tags=["test"])


app.include_router(test_router)
