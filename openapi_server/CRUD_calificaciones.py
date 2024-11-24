from sqlalchemy.orm import Session
from openapi_server.databaseCalificaciones import Calificacion as CalificacionDB
from datetime import datetime

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

def obtener_calificaciones_por_contenido(db: Session, id_contenido: int):
    try:
        calificaciones = db.query(CalificacionDB).filter(CalificacionDB.id_contenido == id_contenido).all()
        return [calificacion.to_dict() for calificacion in calificaciones]
    except Exception as e:
        raise e