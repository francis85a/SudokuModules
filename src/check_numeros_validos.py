def check_numeros_validos(sudoku):

    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    for fila in sudoku:
        for numero in fila:
            if numero not in range(1,len(sudoku)+1):
                return False
            if not isinstance(numero, int):
                return False
    return True
