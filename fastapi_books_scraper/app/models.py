import uuid
from sqlalchemy import Column, String, DateTime, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(512), nullable=False)
    description = Column(String, nullable=True)
    url = Column(String(1024), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint('url', name='uq_item_url'),
    )
