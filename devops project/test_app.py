from app import calculate_grade

def test_distinction():
    assert calculate_grade(80) == "Distinction"

def test_first_class():
    assert calculate_grade(65) == "First Class"

def test_pass():
    assert calculate_grade(50) == "Pass"

def test_fail():
    assert calculate_grade(30) == "Fail"
