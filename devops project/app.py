def calculate_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"

students = {
    "Anushka": 82,
    "Rahul": 55,
    "Priya": 33
}

for name, marks in students.items():
    print(f"{name}: {calculate_grade(marks)}")