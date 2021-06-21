from models import Student
from flask import request, redirect, url_for, render_template

from search import app


@app.route('/detail-list/')
def details():
    myStudent = Student.query.all()
    return render_template('student_details_list.html', myStudent=myStudent)


@app.route('/details-capture/', methods=['POST'])
def capture():
    student = Student(request.form['RegNum'], request.form['Name'],
                      request.form['Surname'], request.form['Programme'],
                      request.form['DOB'], request.form['Address'], request.form['email'],
                      request.form['GraduationYear'])

    # SessionUZ.add(student)
    # SessionUZ.commit()
    return redirect(url_for("details"))

