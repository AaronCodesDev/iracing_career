def correr_carrera(piloto, carrera, posicion, incidentes, equipos_disponibles):
    piloto.dinero -= carrera.coste_inscripcion
    recompensa = max(carrera.recompensa_max - (posicion - 1) * 50, 0)
    piloto.dinero += recompensa
    piloto.dinero -= sum(incidentes)

    if piloto.dinero > 2000:
        piloto.nivel += 1

    # Intentar fichaje
    for equipo in equipos_disponibles:
        if piloto.nivel >= equipo.nivel_minimo and piloto.equipo_id is None:
            piloto.equipo_id = equipo.id
            piloto.dinero += equipo.bonus_fichaje
            print(f"🎉 {piloto.nombre} ha sido fichado por {equipo.nombre} +${equipo.bonus_fichaje}")
            break

    return piloto
