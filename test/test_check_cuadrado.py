import pytest
from src.check_cuadrado import check_cuadrado
import casosTest.casos_test_sudoku as casosTest



@pytest.mark.es_cuadrado
@pytest.mark.parametrize(
    "sudoku, esperado",
    [
        (casosTest.lista_vacia, False),
        (casosTest.sudoku_correcto, True),
        (casosTest.sudoku_correcto2, True),
        (casosTest.numero_repetido_columna, True),
        (casosTest.numero_repetido_fila_columna, True),
        (casosTest.numero_no_presente, True),
        (casosTest.numero_fuera_del_rango, True),
        (casosTest.sudoku_letras, True),
        (casosTest.numeros_decimales, True),
        (casosTest.no_cuadrado, False),
        (casosTest.no_cuadrado2, False),
        (casosTest.sudoku_una_fila_columna, True),
    ],
)
def test_check_cuadrado(sudoku, esperado):
    assert check_cuadrado(sudoku) == esperado