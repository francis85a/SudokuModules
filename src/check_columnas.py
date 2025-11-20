def check_columnas(sudoku):

    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    numero_filas = len(sudoku)
    
    index_fila_actual = 0
    
    for fila in sudoku:

        for numero in fila:
            index_fila_siguiente = index_fila_actual + 1

            while index_fila_siguiente < numero_filas:

                try:
                    posicion_numero_fila_siguiente = sudoku[index_fila_siguiente].index(numero)

                except ValueError:
                    return False
                
                else:
                    if posicion_numero_fila_siguiente == fila.index(numero):
                        return False
                    else:
                        index_fila_siguiente += 1

        index_fila_actual += 1

    return True
