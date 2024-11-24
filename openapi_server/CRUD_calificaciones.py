def agregar_calificacion(db: Session, id_contenido: int, id_usuario: int, puntuacion: int, comentario: str = None):
    try:
        nueva_calificacion = CalificacionDB(
            id_contenido=id_contenido,
            id_usuario=id_usuario,
            puntuacion=puntuacion,
            comentario=comentario,
            fecha=datetime.now()
        )
        db.add(nueva_calificacion)
        db.commit()
        db.refresh(nueva_calificacion)
        return nueva_calificacion.to_dict()
    except Exception as e:
        db.rollback()
        raise e