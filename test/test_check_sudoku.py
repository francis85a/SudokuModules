import pytest
from src.check_sudoku import check_sudoku
import casosTest.casos_test_sudoku as casosTest

@pytest.mark.comprobar_sudoku
@pytest.mark.parametrize(
    "sudoku, esperado", 
    [
        (casosTest.sudoku_correcto, True),
        (casosTest.no_cuadrado2, False),
        (casosTest.numero_no_presente, False),
        (casosTest.numero_repetido_columna, False),
        (casosTest.numero_repetido_fila_columna, False),
        (casosTest.sudoku_letras, False),
        (casosTest.numeros_decimales, False),
        (casosTest.numero_fuera_del_rango, False),
        (casosTest.lista_vacia, False),
        (casosTest.sudoku_una_fila_columna, True),
        (casosTest.sudoku_correcto2, True)
    ],  
)
def test_check_sudoku(sudoku, esperado):
    assert check_sudoku(sudoku) == esperado