# [1.1.27] 19-09-2024
### Agregado 
- Se agrego un test_rook que verifica los movimientos horizontales cuando hay compañeros del mismo
  color en el camino.
- Se agrego un test_rook que verifica los movimientos verticales cuando hay compañeros del mismo
  color en el camino.
- Se hicieron cambios en el init de rook.
- Se agrego un "possibles.sort()" que ordena las posiciones para asegurar el orden correcto.
----------------------------------------------------


# [1.1.26] 18-09-2024
### Agregado 
- Se arreglo una funcion que verifica si en el camino de la pieza rook hay compañeros 
  del mismo color. 
- Se agregaron cosas en la funcion captura.
- Se hicieron arreglos en la funcion de movimientos verticales.
- Se hicieron arreglos en la funcion de movimientos horizontales.
- Se hizo un test_rook que verifica los movimientos de  una pieza blanca cuando hay un
  compañero del mismo color. 
- Se hizo un test_rook que verifica los movimientos de  una pieza negra cuando hay un
  compañero del mismo color. 
----------------------------------------------------

# [1.1.25] 17-09-2024
### Agregado 
- Se agrego un test en test_rook que verifica que la pieza torre coma cuando hay una pieza 
  de otro color.
- Se trabajo en arreglos.
----------------------------------------------------


# [1.1.24] 16-09-2024
### Agregado 
- Se agregaro un test en test_rook que verifica que la pieza de la torre avance
- Se agrego otro test en test_rook que verifica que si hay una pieza del mismo color pare.
- Se arreglaron algunos problemas. 
----------------------------------------------------
# [1.1.23] 15-09-2024
### Agregado 
- Se hicieron pequeños cambios en piece.
- Se hicieron pequeños cambios en rook.
- Los arreglos del test_rook estan en procesos. 
----------------------------------------------------

# [1.1.22] 11-09-2024
### Agregado 
- Se realizaron modificaciones en el init de PIECE.
- Sa agrego la condicion de que la torre no siga avanzando si ve alguna pieza del 
  mismo color(vertical descendente)
----------------------------------------------------

# [1.1.21] 10-09-2024
### Agregado 
- Se agrego una base de la funcion de captura de la torre.
----------------------------------------------------

# [1.1.20] 09-09-2024
### Agregado 
- Se creo el test que verifica la captura diagonal.
- Se creo la clase MockBoard en test_pawn.
- Se creo la clase MockPiece en test_pawn.
----------------------------------------------------

# [1.1.19] 08-09-2024
### Agregado 
- Se creo el metodo que le permite al peon capturar de forma diagonal.
----------------------------------------------------

# [1.1.18] 07-09-2024
### Agregado 
- Se modifico la funcion del movimiento hacia adelante del peon.
- Se modifico el dobre salto en el primer movimiento del peon.
- Se agrego un test que verifica que el peon blanco o negro pueda realizar doble movimiento o  
  uno solo si es su primer turno.
- Se agrego un test que verifica el movimiento de solo una casilla del peon blanco.
- Se agrego un test que verifica el movimiento de solo una casilla del peon negro.

----------------------------------------------------
# [1.1.17] 06-09-2024
### Agregado 
- Se agrego la funcion que realiza el doble salto del peon.
----------------------------------------------------

# [1.1.16] 05-09-2024
### Agregado 

- Se agrego el movimiento hacia adelante del peon.
- Se agrego el archivo test_pawn.
- Se agrego las posciones de los peones en BOARD.
- Se afrego un test_pawn que se debe arreglar. 
----------------------------------------------------

# [1.1.15] 04-09-2024
### Agregado 

- Se agrego el test que verifica el movimiento horizontal hacia la derecha de la torre.
- Se agrego el test que verifica el movimiento horizontal hacia la izquierda de la torre.
----------------------------------------------------

# [1.1.14] 03-09-2024
### Agregado 

- Se agrego el movimiento horizontal de la torre hacia la derecha.
- Se agrego el movimiento horizontal de la torre hacia la izquierda.
- Se agrego el archivo exceptions.py con las excepciones.
- Se modifico el get_piece de BOARD.
- Se agrego el metodo move en BOARD.
- Se modifico el archivo CLI.
----------------------------------------------------

# [1.1.13] 02-09-2024
### Agregado 

- Se agrego un test de rook.
- Se verifico la posicion de las torres en test_board.
- Se verifico la posicion de los caballos en test_board.
- Se verifico la posicion de los reyes en test_board. 
----------------------------------------------------

# [1.1.12] 01-09-2024
### Agregado 

- Se agrego el movimiento de la torre ascendente.
- Se agrego el movimiento de la torre descendente.
- Se agrego un test del movimiento de la torre.
- Se arreglaron varias cosas.
- Se soluciono algunos problemas de importacion.
- Se agrego un str en PIECE.
- Se agrego carpeta PAWN. 
- Se agrego set_piece en BOARD.
----------------------------------------------------
# [1.1.11] 27-08-2024
### Agregado 

- Se agrego el test de KING con el setUp.
- Se agrego el str en HORSE
- Se agrego el str en KING
- Se agrego el str en ROOK
- Se agrego el metodo valid_move_king para los movimientos del rey.
- Se borro el metodo del movimiento de la torre para mejorlo y porque daba problemas.
----------------------------------------------------
# [1.1.10] 24-08-2024
### Agregado 

- Se agrego el test de HORSE en la posicon esquina.
- Se agrego el test de HORSE en la posicion borde.
- Se agrego el test de HORSE en la poscion borde pero no en una esquina.
----------------------------------------------------

# [1.1.9] 23-08-2024
### Agregado 

- Se implementó la lógica para calcular los movimientos válidos de un caballo. 
- El método genera una lista de posibles movimientos en forma de "L".
- Se agregó una verificación para asegurar que los movimientos estén dentro de los límite(8x8).
- Los movimientos válidos se agregan a la lista moves y se devuelven al final del método.
- Se agrego un test que verifica los movimientos desde una posicion. 
----------------------------------------------------
# [1.1.8] 22-08-2024
### Agregado 

- Se modifico el moviento de ROOK.
- Se creo el test de ROOk.
- Se hiceron algunas configuraciones.
- Se cambiaron algunas funciones. 
----------------------------------------------------

# [1.1.7] 21-08-2024
### Agregado 

- Se cambio el moviento de ROOK.
- La funcion valid_rook se encarga de los moviemintos horizontales y verticales de la torre.

----------------------------------------------------
# [1.1.6] 20-08-2024
### Agregado 

- Se creo en BOARD las posiciones de los caballos.
- Se verifico las posiciones de los caballos.
- Se verifico las posiciones de las reinas.
- Se creo las posiciones del rey.
- Se creo un archivo KNIGHT.
- Se creo las posiciones del los alfiles.
- Se creo el archivo BISHOP. 
----------------------------------------------------

# [1.1.5] 18-08-2024
### Agregado 

- Se creo el metodo is_clear_path en el archivo QUEEN que asegura que una pieza puede moverse de un punto a otro sin que haya otras piezas bloqueando el camino. 
----------------------------------------------------

# [1.1.4] 17-08-2024
### Agregado 

- Se agrego el movimiento vertical de la torre.
- Se agrego el movimiento horizontal de la torre.
- Se agrego en el archivo BOARD las posiciones de las reinas.
----------------------------------------------------

# [1.1.3] 16-08-2024
### Agregado 

- Se agregó un constructor __init__ para la clase que representa a la reina.
- Se añadió el método valid_move_queen para validar los movimientos de la reina
- Se verifica si la reina se mueve horizontalmente dentro de la misma fila 
- Se verifica si la reina se mueve verticalmente dentro de la misma columa.
- Se añadió una validación para movimientos diagonales.
----------------------------------------------------

# [1.1.2] 15-08-2024
### Agregado 

- Se agrego el test_board.py para asegurarnos de que el tablero (Board) se crea bien.
- Confirmamos que el tablero tiene 8x8 posiciones.
- Verificamos que las torres negras esten en la posicion correcta: en las esquinas superiores.
- Verificamos que las torres blancas esten en la posicion correcta: en las esquinas inferiores.
- Se agrego la pieza reina.
- La interfaz del usuario CLI. 
----------------------------------------------------

# [1.1.1] 14-08-2024
### Agregado 

- Una carpeta GAME con los archivos BOARD y CHESS.
- Una carpeta PIECE con el archivo ROOK.
 
