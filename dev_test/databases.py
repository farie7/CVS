import os
import sqlite3
import logging
from flask import flash
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setup_app import db
from models import Student, Base

engine_uz = create_engine('postgresql://postgres:postgres@localhost/university_of_zimbabwe')
engine_hit = create_engine('postgresql://postgres:postgres@localhost/harare_institute')
engine_cut = create_engine('postgresql://postgres:postgres@localhost/chinhoyi_institute')
DATABASES = {
    'hit': 'postgresql://postgres:postgres@localhost/university_of_zimbabwe',
    'cut': 'postgresql://postgres:postgres@localhost/chinhoyi_institute',
    'uz': 'postgresql://postgres:postgres@localhost/university_of_zimbabwe'
}


# Base = declarative_base()

def save(entity: db.Model):
    db.session.add(entity),
    db.session.commit()


def init():
    for e in [engine_cut, engine_uz, engine_hit]:
        Base.metadata.drop_all(bind=e)
        create_tables()


def create_tables():
    """
    Create tables in  databases
    """
    for e in [engine_cut, engine_uz, engine_hit]:
        Base.metadata.create_all(bind=e, checkfirst=True)
    seed_databases()


def seed_databases():
    """
    Populates databases with initial student data,
     for each respective university
    """
    print("Seeding......")
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
                     programme="CS", dob="10-02-1996", institution='hit',
                     address="5 Hill Road, Avondale, Harare",
                     email="igore@gmail.com",
                     graduation_year="2016"
                     ),
             Student(reg_number="H200456T",
                     name="Chipo", surname="Urombo",
                     programme="IT", dob="12-08-1996", institution='hit',
                     address="99 Hill Road, Avondale, Harare",
                     email="curombo@gmail.com",
                     graduation_year="2014"
                     ),
             Student(reg_number="H200456V",
                     name="Busani", surname="Ndlovhu", institution='hit',
                     programme="SE", dob="14-06-1995",
                     address="234 Hill Road, Greencroft, Harare",
                     email="bndlovhu@gmail.com",
                     graduation_year="2007"
                     )

             ]

        )
        session2.add_all(
            [Student(reg_number="UZSTUD01",
                     name="Chiedza", surname="Mupariwa", institution='uz',
                     programme="CS", dob="28-04-1990",
                     address="7 Hill Avenue, Hatfield, Harare",
                     email="cmupariwa@gmail.com",
                     graduation_year="2007"
                     ),
             Student(reg_number="UZSTUD03",
                     name="John", surname="Doe",
                     programme="CS", dob="8-08-1996", institution='uz',
                     address="7 Seke Road, Harare",
                     email="jdoe@gmail.com",
                     graduation_year="2011"
                     ),
             Student(reg_number="UZSTUD04",
                     name="Rudo", surname="Musa",
                     programme="CS", dob="7-06-1995",
                     address="87 Hill Road, Avondale, Harare",
                     email="rmusa@gmail.com", institution='uz',
                     graduation_year="2020"
                     )

             ]

        )
        session3.add_all(
            [Student(reg_number="CUTSTUD01",
                     name="Kevin", surname="Jones",
                     programme="CS", dob="18-01-1996", institution='cut',
                     address="45 Hill Road, Avondale, Harare",
                     email="kjones@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="CUTSTUD03",
                     name="Sam", surname="Chipo",
                     programme="IS", dob="19-08-1997", institution='cut',
                     address="89 Hill Road, Avondale, Harare",
                     email="jdoe@gmail.com",
                     graduation_year="2020"
                     ),
             Student(reg_number="CUTSTUD04",
                     name="Michelle", surname="Musa", institution='cut',
                     programme="IT", dob="23-06-1997",
                     address="7 Hill Road, Avondale, Harare",
                     email="mmusa@gmail.com",
                     graduation_year="2020"
                     )

             ]

        )

        for session in [session1, session2, session3]:
            session.commit()
        print('Databases Seeded.')
    except Exception as e:
        print("There was a problem with session: ", e)
    finally:
        for session in [session1, session2, session3]:
            session.close()


# flask_g global variable
# mem cache server

def database_exists(institution_database: str) -> bool:
    """
    Assert that the database exists
    """

    return os.path.exists('./%s' % institution_database)


def get_institution_details(institution: str):
    """
    @desc: Returns the number of students in selected institution and year of the oldest record
    @param: institution:the institution to search
    """
    try:
        institution_database = '%s.db' % institution

        assert database_exists(institution_database), "%s does not exist" % institution_database
        conn = sqlite3.connect(institution_database)
        statement = '''SELECT MIN(YEAR_OF_GRADUATION), COUNT(YEAR_OF_GRADUATION) FROM STUDENT;'''
        cursor = conn.cursor()
        result = cursor.execute(statement)
        oldest_record = 0
        number_of_students = 0
        for row in result:
            oldest_record += row[0]
            number_of_students += row[1]
        return oldest_record, number_of_students
    except Exception as e:
        logging.error(e)


# TOD
if __name__ == "__main__":
    init()
    create_tables()
