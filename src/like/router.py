from fastapi import APIRouter, Depends
from sqlalchemy import insert, delete, select, update
from sqlalchemy.event import remove
from sqlalchemy.ext.asyncio import AsyncSession
from post.tables import post
from auth.base_config import fastapi_user
from auth.models import User
from like.schemas import LikeCreate, LikeRemove, LikeChange
from like.tables import like
from database_init import get_async_session

router = APIRouter(
    prefix="/like",
    tags=["like"]
)
current_user = fastapi_user.current_user()


@router.post("/like")
async def put_like(new_like: LikeCreate, curr_user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    find_post_statement = select(post).where(post.c.uuid == new_like.uuid)
    target_post = await session.execute(find_post_statement)
    target_post = target_post.all()[0]
    if target_post.creator != curr_user.email:
        new_like.author = curr_user.email
        statement = insert(like).values(new_like.model_dump())
        await session.execute(statement)
        await session.commit()
        return {
            "status": "Success",
            "data": None,
            "details": "Like put successfully"
        }
    else:
        return {
            "status": "Error",
            "data": None,
            "details": "Can't like own posts"
        }


@router.delete("/like_delete")
async def delete_like(new_like: LikeRemove, curr_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    statement = delete(like).where(like.c.uuid == new_like.uuid and like.c.author == curr_user.email)
    await session.execute(statement)
    await session.commit()
    return {
        "status": "Success",
        "data": None,
        "details": "Like deleted"
    }


@router.put("/change_like")
async def change_like(new_like: LikeChange, curr_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    find_like_statement = select(like).where(like.c.uuid == new_like.uuid)
    target_like = await session.execute(find_like_statement)
    if target_like.author == curr_user.email:
        statement = update(like).where(like.c.uuid == change_like.uuid).values(is_like=new_like.is_like)
        await session.execute(statement)
        await session.commit()
        return {
            "status": "Success",
            "data": None,
            "details": "Like changed"
        }
    else:
        return {
            "status": "Error",
            "data": None,
            "details": "Can't edit others like'"
        }
