from flask import Flask, render_template
#from .models import  StudentDetails



app  = Flask(__name__)


@app.route('/detail-list/')
def index():
    return render_template ("student_details_list.html")


@app.route('/detail-capture/')
def index1():
    return render_template ("student_details_capture.html")

if __name__ == "__main__":
    app.run(debug=True)
