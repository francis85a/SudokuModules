def check_filas(sudoku):
    
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    for fila in sudoku:
        diccionario_valores = {}
        for numero in fila:

            if numero in diccionario_valores:
                diccionario_valores[numero] += 1
            else:
                diccionario_valores[numero] = 1

            if diccionario_valores[numero] > 1:
                return False
    return True
