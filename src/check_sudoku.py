import sys
sys.path.append('src')

from check_cuadrado import check_cuadrado
from check_numeros_validos import check_numeros_validos
from check_filas import check_filas
from check_columnas import check_columnas

def check_sudoku(sudoku):

    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    return check_cuadrado(sudoku) and check_numeros_validos(sudoku) and check_filas(sudoku) and check_columnas(sudoku)
