from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_uz = create_engine('postgresql://postgres:postgres@localhost/university_of_zimbabwe')
engine_hit = create_engine('postgresql://postgres:postgres@localhost/harare_institute')
engine_cut = create_engine('postgresql://postgres:postgres@localhost/chinhoyi_institute')

Base = declarative_base()

app = Flask(__name__)


# DATABASES = {
#     'hit': 'postgresql://postgres:postgres@localhost/university_of_zimbabwe',
#     'cut': 'postgresql://postgres:postgres@localhost/chinhoyi_institute',
#     'uz': 'postgresql://postgres:postgres@localhost/university_of_zimbabwe'
# }


# db = SQLAlchemy(app)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(String, unique=True)
    name = Column(String(80), unique=True)
    surname = Column(String(80), unique=True)
    programme = Column(String(80))
    dob = Column(String(80), unique=True)
    address = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    graduation_year = Column(String(120))

    # institution_id = Column(Integer, ForeignKey('institution.id'),
    #                         nullable=False)

    def __init__(self, reg_number, name, surname, programme, dob, address, email, graduation_year) -> None:
        self.graduation_year = graduation_year
        self.email = email
        self.address = address
        self.dob = dob
        self.programme = programme
        self.surname = surname
        self.name = name
        self.reg_number = reg_number

    @property
    def full_name(self):
        return self.name + "" + self.surname

    def __repr__(self):
        return '<Name %r' % self.name


# class Institution(Base):
#     __tablename__ = 'institutions'
#     id = Column(Integer, primary_key=True, autoincrement=False)
#     name = Column(String, nullable=False)
#     students = relationship('Student', backref='institution', lazy=True)
#

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


def query_student_by_institution(database: str, reg_number: str) -> None:
    """
    :param reg_number:
    Student registration number that uniquely identifies the institution's students
    :param database:
    The student database
    """
    try:
        session = None
        if database == "uz":
            Session = sessionmaker(bind=engine_uz)
            session = Session()

        elif database == "cut":
            Session = sessionmaker(bind=engine_cut)
            session = Session()

        elif database == "hit":

            Session = sessionmaker(bind=engine_hit)
            session = Session()
        else:
            print("Please select a valid university !!")
        result = session.query(Student).filter_by(reg_number=reg_number).all()
        print(result)
    except Exception as error:
        print("Error: ", error)


for engine in [engine_cut, engine_uz, engine_hit]:
    Base.metadata.create_all(bind=engine, checkfirst=True)


def query_students_by_institution(institution: str) -> [Student]:
    """

    :param institution:
    The institution enrolled at by students
    """
    try:
        session = None
        if institution == "uz":
            Session = sessionmaker(bind=engine_uz)
            session = Session()

        elif institution == "cut":
            Session = sessionmaker(bind=engine_cut)
            session = Session()

        elif institution == "hit":

            Session = sessionmaker(bind=engine_hit)
            session = Session()
        else:
            print("Please select a valid university !!")
        result = session.query(Student).all()
        print(result)
    except Exception as error:
        print("Error: ", error)


for engine in [engine_cut, engine_uz, engine_hit]:
    Base.metadata.create_all(bind=engine, checkfirst=True)


def seed_databases():
    """

    """
    print("seeding......")
    Session_Hit = sessionmaker(bind=engine_hit)
    session1 = Session_Hit()
    Session_UZ = sessionmaker(bind=engine_uz)
    session2 = Session_UZ()
    Session_CUT = sessionmaker(bind=engine_cut)
    session3 = Session_CUT()

    # Adding students
    try:

        session1.add_all(
            [Student(reg_number="H200345H",
                     name="Ian", surname="Gore",
                     programme="CS", dob="10-02-1996",
                     address="5 Hill Road, Avondale, Harare",
                     email="igore@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="H200456T",
                     name="Chipo", surname="Urombo",
                     programme="IT", dob="12-08-1996",
                     address="99 Hill Road, Avondale, Harare",
                     email="curombo@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="H200456V",
                     name="Busani", surname="Ndlovhu",
                     programme="SE", dob="14-06-1995",
                     address="234 Hill Road, Greencroft, Harare",
                     email="bndlovhu@gmail.com",
                     graduation_year="2020"
                     )

             ]

        )
        session2.add_all(
            [Student(reg_number="UZSTUD01",
                     name="Chiedza", surname="Mupariwa",
                     programme="CS", dob="28-04-1990",
                     address="7 Hill Avenue, Hatfield, Harare",
                     email="cmupariwa@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="UZSTUD03",
                     name="John", surname="Doe",
                     programme="CS", dob="8-08-1996",
                     address="7 Seke Road, Harare",
                     email="jdoe@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="UZSTUD04",
                     name="Rudo", surname="Musa",
                     programme="CS", dob="7-06-1995",
                     address="87 Hill Road, Avondale, Harare",
                     email="rmusa@gmail.com",
                     graduation_year="2020"
                     )

             ]

        )
        session3.add_all(
            [Student(reg_number="CUTSTUD01",
                     name="Kevin", surname="Jones",
                     programme="CS", dob="18-01-1996",
                     address="45 Hill Road, Avondale, Harare",
                     email="kjones@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="CUTSTUD03",
                     name="Sam", surname="Chipo",
                     programme="IS", dob="19-08-1997",
                     address="89 Hill Road, Avondale, Harare",
                     email="jdoe@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="CUTSTUD04",
                     name="Michelle", surname="Musa",
                     programme="IT", dob="23-06-1997",
                     address="7 Hill Road, Avondale, Harare",
                     email="mmusa@gmail.com",
                     graduation_year="2020"
                     )

             ]

        )

        for session in [session1, session2, session3]:
            session.commit()

    except Exception as e:
        print("There was a problem with session: ", e)
    finally:
        for session in [session1, session2, session3]:
            session.close()


for e in [engine_cut, engine_uz, engine_hit]:
    Base.metadata.drop_all(bind=e)
for e in [engine_cut, engine_uz, engine_hit]:
    Base.metadata.create_all(bind=e)
seed_databases()
query_student_by_institution('hit', "H1470283B")

query_students_by_institution('cut')
if __name__ == "__main__":
    app.run(debug=True)
