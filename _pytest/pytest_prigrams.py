# File: test_calculation.py
def add(a, b):
    return a + b

# Test function
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# =============================================================================

# File: test_fixtures.py
import pytest

# Fixture to provide a sample list
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

# Test function that uses the fixture
def test_list_length(sample_list):
    assert len(sample_list) == 5

# Another test using the fixture
def test_list_content(sample_list):
    assert 3 in sample_list
    assert 6 not in sample_list

# =============================================================================

# File: test_exceptions.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test function for exception
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# Test function for normal division
def test_divide():
    assert divide(10, 2) == 5
    assert divide(8, 4) == 2


