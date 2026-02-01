import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    money = Column(Integer, default=1000)
    level = Column(Integer, default=1)

    # Relationship with Team
    team_id = Column(String, ForeignKey("teams.id"), nullable=True)
    team = relationship("Team", back_populates="drivers")
