from sqlalchemy import Column, Integer, String

from app.db.db import Base


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f'PostModel id={self.id}, title={self.title}'
