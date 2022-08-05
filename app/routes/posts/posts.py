from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependecies.database_dependecies import get_db_session
from app.repositories.posts.post import PostRepository
from app.schemas.posts import post as post_schemas

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.get('/', response_model=List[post_schemas.Post])
async def get_all_posts(db: AsyncSession = Depends(get_db_session)):
    return await PostRepository.fetch_all(db)


@router.post('/create', response_model=post_schemas.Post)
async def create_post(post: post_schemas.PostCreate, db: AsyncSession = Depends(get_db_session)):
    return await PostRepository.create(db, post)
