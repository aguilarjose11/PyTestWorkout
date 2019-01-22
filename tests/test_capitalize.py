import pytest


# method to be tested.
def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument.')
    return x.capitalize()


# tests if the capitalization works
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


# test whether the code will raise an exception
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)


# same as above.
def test_raises_exception_on_non_object_arguments():
    with pytest.raises(TypeError):
        capital_case([1, "24"])
