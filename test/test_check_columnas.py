import pytest
from src.check_columnas import check_columnas
import casosTest.casos_test_sudoku as casosTest

@pytest.mark.son_columnas_validas
@pytest.mark.parametrize(
    "sudoku, esperado",
    [
        (casosTest.sudoku_correcto, True),
        (casosTest.numero_repetido_columna, False),
        (casosTest.numero_repetido_fila_columna, False),
    ],
)
def test_check_columnas(sudoku, esperado):
    assert check_columnas(sudoku) == esperado