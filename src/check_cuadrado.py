import sys
sys.path.append('src')
def check_cuadrado(sudoku):
    CERO = 0
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"
    numero_fila = len(sudoku)
    numero_columna = len(sudoku[0])

    for fila in sudoku:
        if len(fila) != numero_columna:
            return False
    
        
    if (numero_fila * numero_columna) == CERO:
        return False
    
    return numero_fila == numero_columna
