from app import calculate_grade

def test_distinction():
    assert calculate_grade(80) == "Distinction"

def test_fail():
    assert calculate_grade(30) == "Fail"