import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db.base import Base

class Equipo(Base):
    __tablename__ = "equipos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String, nullable=False)
    bonus_fichaje = Column(Integer, default=200)  # dinero extra al fichar
    nivel_minimo = Column(Integer, default=1)     # nivel mínimo para fichar

    # Relación inversa con pilotos
    pilotos = relationship("Piloto", back_populates="equipo")
