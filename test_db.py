from db.session import SessionLocal
from db.models.piloto import Piloto
from db.models.equipo import Equipo
from game.carrera import correr_carrera


db = SessionLocal()

# Crear un piloto
piloto = Piloto(nombre="Aaron Planas")
equipo1 = Equipo(nombre="Equipo A", bonus_fichaje=300, nivel_minimo=2)
equipo2 = Equipo(nombre="Equipo B", bonus_fichaje=500, nivel_minimo=3)
db.add_all([equipo1, equipo2])
db.commit()
db.refresh(piloto)  # para asegurarnos de obtener los datos actualizados

equipos = [equipo1, equipo2]

piloto = correr_carrera(piloto, carrera=type('Carrera', (), {'coste_inscripcion':100,'recompensa_max':500})(), posicion=2, incidentes=[50], equipos_disponibles=equipos)

db.commit()
print(piloto.nombre, piloto.dinero, piloto.equipo.nombre if piloto.equipo else None)
