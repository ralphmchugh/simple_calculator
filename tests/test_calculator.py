import pytest # pytest is a testing framework
import src.calculator.calculator as calc

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(5,25, id="5^2"),
        pytest.param(-5,25, id="-5^2"),
        pytest.param(0,0, id="0^2"),
    ],

)
def test_squareNums(input, expected):
    """Testing the squareNums function"""
    assert calc.squareNums(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(5,15, id="Trinum of 5"),
        pytest.param(6,21, id="Trinum of 6"),
        pytest.param(0,0, id="Trinum of 0"),
    ],
)
def test_triNums(input, expected):
    """Testing the triNums function"""
    assert calc.triNums(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(5,16, id="Lazy Caterer of 5"),
        pytest.param(10,56, id="Lazy Caterer of 10"),
        pytest.param(0,1, id="Lazy Caterer of 0")
    ],
)
def test_lazyCaterer(input, expected):
    """Testing the lazyCaterer function"""
    assert calc.lazyCaterer(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(5,65, id="Magic square of 5"),
        pytest.param(-5,-65, id="Magic square of -5"),
        pytest.param(0,0, id="Magic square of 0"),
    ],
)
def test_magicSquares(input, expected):
    """Testing the Magic Squares function"""
    assert calc.magicSquares(input) == expected



@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        pytest.param(3,4,5, id="Hypotenuse of a 3,4 triangle"),
        pytest.param(6,8,10, id="Hypotenuse of a 6,8 triangle"),
        pytest.param(0,0,0, id="Hypotenuse of a 0,0 triangle"),
    ],
)
def test_hypotenuseOfRightTriangle(input1, input2, expected):
    """Testing the Hypotenuse function"""
    assert calc.hypotenuseOfRightTriangle(input1, input2) == expected



@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(-5,5, id="Absolute value of -5"),
        pytest.param(5,5, id="Absolute value of 5"),
        pytest.param(-1.5,1.5, id="Absolute value of -1.5(float check)"),
    ],
)
def test_absoluteValue(input, expected):
    """Testing the absoluteValue function"""
    assert calc.absoluteValue(input) == expected




@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(8,256, id="2 to the power of 8"),
        pytest.param(16,65536, id="2 to the power of 16"),
        pytest.param(32,4294967296, id="2 to the power of 32")
       
    ],
)
def test_powerOfTwo(input, expected):
    """Testing the powerOfTwo function"""
    assert calc.powerOfTwo(input) == expected



