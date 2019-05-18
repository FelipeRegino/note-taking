from .database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, Date


class Note(Base):
    """Modelo de nota."""

    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    content = Column(Text, nullable=False)
    date = Column(Date)
    status = Column(Boolean, nullable=False)

    def __init__(self, title=None, content=None, date=None, status=None):
        self.title = title
        self.content = content
        self.date = date
        self.status = status

    def __repr__(self):
        return "<Title: {}>".format(self.title)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date': self.date,
            'status': self.status,
        }
