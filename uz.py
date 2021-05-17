from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:B17s"fric"@localhost/UZ'
app.config['SQLALCHEMY_BINDS'] = {'NUST': 'postgresql://postgres:B17s"fric"@localhost/nust',
                                  'MSU': 'postgresql://postgres:B17s"fric"@localhost/msu'}
db = SQLAlchemy(app)


class Students(db.Model):
    RegNum = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    Surname = db.Column(db.String(80), unique=True)
    Programme = db.Column(db.String(80), unique=True)
    DOB = db.Column(db.String(80), unique=True)
    Address = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    GraduationYear = db.Column(db.String(120), unique=True)

    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname

    def __repr__(self):
        return '<Name %r' % self.Name


class Students(db.Model):
    __bind_key__ = 'MSU'
    RegNum = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    Surname = db.Column(db.String(80), unique=True)
    Programme = db.Column(db.String(80), unique=True)
    DOB = db.Column(db.String(80), unique=True)
    Address = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    GraduationYear = db.Column(db.String(120), unique=True)

    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname

    def __repr__(self):
        return '<Name %r' % self.Name


class Students(db.Model):
    __bind_key__ = 'NUST'
    RegNum = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    Surname = db.Column(db.String(80), unique=True)
    Programme = db.Column(db.String(80), unique=True)
    DOB = db.Column(db.String(80), unique=True)
    Address = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    GraduationYear = db.Column(db.String(120), unique=True)

    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname

    def __repr__(self):
        return '<Name %r' % self.Name


@app.route('/detail-list/')
def details():
    myStudent = Students.query.all()
    return render_template('student_details_list.html', myStudent=myStudent)


@app.route('/details-capture/', methods=['POST'])
def capture():
    student = Students(request.form['RegNum'], request.form['Name'],
                       request.form['Surname'], request.form['Programme'],
                       request.form['DOB'], request.form['Address'], request.form['email'],
                       request.form['GraduationYear'])
    db.session.add(student)
    db.session.commit()
    return redirect(url_for("details"))


if __name__ == "__main__":
    app.run(debug=True)
