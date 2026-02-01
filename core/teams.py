import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db.base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    signing_bonus = Column(Integer, default=200)  # extra money when signing a driver
    min_level = Column(Integer, default=1)       # minimum level to sign

    # Inverse relationship with Drivers
    drivers = relationship("Driver", back_populates="team")
