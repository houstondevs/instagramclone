from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.posts import post as post_schemas
from app.models.posts.post import PostModel


class PostRepository:
    model = PostModel

    @classmethod
    async def create(cls, db: AsyncSession, post: post_schemas.PostCreate):
        db_item = cls.model(title=post.title, text=post.text)
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item

    @classmethod
    async def fetch_all(cls, db: AsyncSession):
        data = await db.execute(select(cls.model))
        data = data.scalars().all()
        return data
