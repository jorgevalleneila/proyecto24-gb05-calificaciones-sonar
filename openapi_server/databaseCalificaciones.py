from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Calificacion(Base):
    __tablename__ = 'calificaciones'

    id_calificacion = Column(Integer, primary_key=True, autoincrement=True)
    id_contenido = Column(Integer, nullable=False)
    id_usuario = Column(Integer, nullable=False)
    puntuacion = Column(Integer, nullable=False)
    comentario = Column(String(255))
    fecha = Column(Date, nullable=False)

    def to_dict(self):
        return {
            "id_calificacion": self.id_calificacion,
            "idContenido": self.id_contenido,
            "idUsuario": self.id_usuario,
            "puntuacion": self.puntuacion,
            "comentario": self.comentario,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }


