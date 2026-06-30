from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    students = [
        {
            "name": "Usama",
            "age": 23,
            "department": "Computer Science"
        },
        {
            "name": "Ali",
            "age": 22,
            "department": "Software Engineering"
        },
        {
            "name": "Ahmed",
            "age": 24,
            "department": "Information Technology"
        }
    ]

    return render_template(
        "index2.html",
        students=students
    )

if __name__ == "__main__":
    app.run(debug=True)