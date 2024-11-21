import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.calificacion import Calificacion  # noqa: E501
from openapi_server import util


def calificaciones_id_get(id):  # noqa: E501
    """Obtener calificaciones de un contenido

    Muestra las calificaciones y comentarios promedio para un contenido específico. # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[Calificacion, Tuple[Calificacion, int], Tuple[Calificacion, int, Dict[str, str]]
    """
    return 'do some magic!'


def calificar_contenido(calificacion):  # noqa: E501
    """Calificar contenido

    Permite a los usuarios calificar un contenido y añadir comentarios. # noqa: E501

    :param calificacion: 
    :type calificacion: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        calificacion = Calificacion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
