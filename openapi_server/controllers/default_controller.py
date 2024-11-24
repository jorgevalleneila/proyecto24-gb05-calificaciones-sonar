def calificar_contenido():
    """Calificar contenido"""
    if not connexion.request.is_json:
        return jsonify({'mensaje': 'Datos inválidos, se esperaba JSON'}), 400

    try:
        calificacion_data = connexion.request.get_json()
        required_fields = ['idContenido', 'idUsuario', 'puntuacion']
        for field in required_fields:
            if field not in calificacion_data:
                return jsonify({'mensaje': f'Falta el campo requerido: {field}'}), 400

        id_contenido = calificacion_data['idContenido']
        id_usuario = calificacion_data['idUsuario']
        puntuacion = calificacion_data['puntuacion']
        comentario = calificacion_data.get('comentario', None)

        db = SessionLocal()
        nueva_calificacion = CRUD_calificaciones.agregar_calificacion(
            db, id_contenido, id_usuario, puntuacion, comentario
        )
        return jsonify(nueva_calificacion), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()