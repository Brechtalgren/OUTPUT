from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str = "bytelaugh_user"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
