import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Piloto(Base):
    __tablename__ = "pilotos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String, nullable=False)
    dinero = Column(Integer, default=1000)
    nivel = Column(Integer, default=1)

    # Nuevo: relación con equipos
    equipo_id = Column(String, ForeignKey("equipos.id"), nullable=True)
    equipo = relationship("Equipo", back_populates="pilotos")
