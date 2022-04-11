import main


def test_sum():
    output = main.sum(1, 2)
    assert output == 3

def test_multiply():
    assert main.multiply(1, 2) == 2
    assert main.multiply(0, 6) == 0
