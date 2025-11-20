import pytest
from src.check_filas import check_filas
import casosTest.casos_test_sudoku as casosTest

@pytest.mark.son_filas_validas
@pytest.mark.parametrize(
    "sudoku, esperado", 
    [
        (casosTest.sudoku_correcto, True),
        (casosTest.numero_repetido_fila_columna, False),
        (casosTest.numero_fuera_del_rango, True),
        (casosTest.no_cuadrado2, True),
    ],

)
def test_check_filas(sudoku, esperado):
    assert check_filas(sudoku) == esperado