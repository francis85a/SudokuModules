import pytest
from src.check_numeros_validos import check_numeros_validos
import casosTest.casos_test_sudoku as casosTest

@pytest.mark.son_numeros_validos
@pytest.mark.parametrize(
    "sudoku, esperado",
    [
        (casosTest.sudoku_correcto, True),
        (casosTest.sudoku_letras, False),
        (casosTest.numeros_decimales, False),
        (casosTest.numero_fuera_del_rango, False),
        (casosTest.no_cuadrado, False),
    ],

)
def test_check_numeros_validos(sudoku, esperado):
    assert check_numeros_validos(sudoku) == esperado