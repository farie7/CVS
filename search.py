from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request, redirect, url_for

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

UZ_engine = create_engine('postgresql://postgres:B17s"fric"@localhost/UZ')
nust_engine = create_engine('postgresql://postgres:B17s"fric"@localhost/nust')
msu_engine = create_engine('postgresql://postgres:B17s"fric"@localhost/msu')


if form.university.data == "uz":
    SessionUZ = sessionmaker(bind=UZ_engine)
    session = SessionUZ()
else if form.university.data == "msu":
    SessionMSU = sessionmaker(bind=msu_engine)
    session = SessionMSU()

else if form.university.data == "nust":
    SessionNust = sessionmaker(bind=nust_engine)
    session = SessionNust()
else:
    print("Please select a valid university !!")

Base = declarative_base()


app = Flask(__name__)

# db = SQLAlchemy(app)

class Students(Base):
    RegNum = Column(Integer, primary_key=True)
    Name = Column(String(80), unique=True)
    Surname = Column(String(80), unique=True)
    Programme = Column(String(80), unique=True)
    DOB = Column(String(80), unique=True)
    Address = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    GraduationYear = Column(String(120), unique=True)

    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname
        self.RegNum = RegNum
        self.Programme = Programme
        self.DOB = DOB
        self.Address = Address
        self. email = email
        self.GraduationYear = GraduationYear


    def __repr__(self):
        return '<Name %r' %self.Name



@app.route('/detail-list/')
def details():
    myStudent = Students.query.all()
    return render_template('student_details_list.html', myStudent=myStudent)

@app.route('/details-capture/', methods = ['POST'])
def capture():
    student = Students(request.form['RegNum'], request.form['Name'],
    request.form['Surname'], request.form['Programme'],
    request.form['DOB'], request.form['Address'], request.form['email'],
    request.form['GraduationYear'])


    SessionUZ.add(student)
    SessionUZ.commit()
    return redirect(url_for("details"))

if __name__ == "__main__":
    app.run(debug=True)
