from main import check_fermat_theorem
import pytest



def test_fermat_theorem():
    assert check_fermat_theorem(2)


@pytest.mark.parametrize(
    "value, error_type",
    [('2', TypeError)]
)
def test_check_fermat_theorem(value, error_type):
    with pytest.raises(error_type):
        check_fermat_theorem(value)
