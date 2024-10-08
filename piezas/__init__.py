direcciones = {
    'rey': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
    'caballo': [
        (2, 1), (2, -1),   # Dos hacia arriba, una a la derecha/izquierda
        (-2, 1), (-2, -1), # Dos hacia abajo, una a la derecha/izquierda
        (1, 2), (1, -2),   # Una hacia arriba, dos a la derecha/izquierda
        (-1, 2), (-1, -2)  # Una hacia abajo, dos a la derecha/izquierda
    ]
}

# Uso de las direcciones
direcciones_king = direcciones['rey']
direcciones_horse = direcciones['caballo']

direcciones_torre = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direcciones_alfil =[(1, 1), (1, -1), (-1, 1), (-1, -1)]