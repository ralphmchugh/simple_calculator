import pytest # pytest is a testing framework
import src.calculator.calculator as calc

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(5,25, id="5^2"),
    ],

)
def test_squareNums(input, expected):
    """Testing the squareNums function"""
    assert calc.squareNums(input) == expected



def test_triNums():
    """Testing the triNums function"""
    










