# tests/test_calculator.py


from calculator import add


def test_add():
    """Test that add() returns the correct sum."""
    result = add(2, 3)
    assert result == 5  # This will FAIL because add() returns 2 - 3 = -1
