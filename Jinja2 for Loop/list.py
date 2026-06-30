from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    students=[
        'usama','ali','jaan','bahi','khang'
    ]
    return render_template('index1.html', students=students)

app.run(debug=True)