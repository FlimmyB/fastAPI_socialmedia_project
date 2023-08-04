from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.base_config import fastapi_user
from src.auth.models import User
from src.database_init import get_async_session
from src.post.schemas import PostCreate, PostEdit
from src.post.tables import post

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

current_user = fastapi_user.current_user()


@router.post("/create")
async def create_post(post_create: PostCreate, creator: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    post_create.creator = creator.email
    await session.execute(insert(post).values(**post_create.model_dump()))
    await session.commit()
    return {
        "status": "Success",
        "data": post_create,
        "details": "Post created successfully"
    }


@router.put("/edit")
async def edit_post(post_edit: PostEdit, curr_user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    post_edit.creator = curr_user.email
    statement = update(post).where(post_edit.uuid == post.c.uuid and curr_user.email == post.c.creator).values(
        post_edit.model_dump())
    await session.execute(statement)
    await session.commit()
    return {"status": "Success",
            "data": post_edit,
            "details": "Post edited successfully"
            }


@router.get("/check_permission")
async def delete_post(post_delete: PostEdit, curr_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    if post_delete.creator == curr_user.email:
        statement = delete(post).where(post.c.uuid == post_delete.uuid)
        await session.execute(statement)
        await session.commit()
        return {
            "status": "Success",
            "data": post_delete,
            "details": "Post deleted successfully"
        }
    else:
        return {
            "status": "Error",
            "data": None,
            "details": "Can not delete others post"
        }


@router.get("/see_posts")
async def see_posts(page: int = 0, session: AsyncSession = Depends(get_async_session)):
    stmt = select(post).where(post.c.id <= page + 10)
    result = await session.execute(stmt)
    return {
        "status": "Success",
        "data": result,
        "details": f"Result for page№{page}"
    }
