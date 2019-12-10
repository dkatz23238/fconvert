def test_1():
    from fconvert.functions import convert_farenheit_to_cel
    val = convert_farenheit_to_cel(120)
    assert val == 48.89