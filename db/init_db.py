from db.session import engine
from db.base import Base

# Importamos los modelos para que SQLAlchemy los conozca
from db.models.piloto import Piloto
from db.models.equipo import Equipo

# Crear todas las tablas que aún no existen
Base.metadata.create_all(bind=engine)
print("✅ Base de datos creada")
