from flask import Flask, jsonify

app = Flask(__name__)

def calculate_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"

@app.route("/")
def home():
    students = {
        "Anushka": 82,
        "Rahul": 55,
        "Priya": 33
    }

    result = {name: calculate_grade(marks) for name, marks in students.items()}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
