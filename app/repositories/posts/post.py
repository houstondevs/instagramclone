from app.schemas.posts import post as post_schemas
from app.models.posts.post import PostModel
from sqlalchemy.orm import Session


class PostRepository:
    model = PostModel

    @classmethod
    async def create(cls, db: Session, post: post_schemas.PostCreate):
        db_item = cls.model(title=post.title, text=post.text)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @classmethod
    async def fetch_all(cls, db: Session):
        data = db.query(cls.model).all()
        return data
