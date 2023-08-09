from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi_users.exceptions import UserAlreadyExists

from src.auth.user_schema import UserCreate
from src.auth.user_manager import create_user
from src.post.router import see_posts

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/see_posts")
def get_post_req_page(request: Request, page=Depends(see_posts)):
    return templates.TemplateResponse("see_posts.html", {"request": request, "posts": page["data"]})


@router.get("/see_posts/{page}")
def get_posts_page(request: Request, page=Depends(see_posts)):
    return templates.TemplateResponse("see_posts.html", {"request": request, "posts": page["data"]})


@router.get("/register/")
def get_register_page(request: Request):
    print("IM HERE 1")
    return templates.TemplateResponse("register_template.html", {"request": request})


@router.post("/register_user/")
async def register_user(request: Request):
    user_data = await request.json()
    user_valid_data = UserCreate(**user_data)
    try:
        new_user = await create_user(user_valid_data)
        return {
            "status": "Success",
            "data": new_user,
            "details": f"User {new_user.username} registered"
        }
    except UserAlreadyExists:
        return {
            "status": "Error",
            "data": "User Already Exists",
            "details": "Error"
        }


@router.get("/register/register_success")
async def success(request: Request):
    return templates.TemplateResponse("register_success.html", {"request": request})
