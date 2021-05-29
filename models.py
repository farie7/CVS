from datetime import datetime, time

from flask_login import UserMixin
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from app import db

Base = declarative_base()


class Student(Base):
    """
    Student model
    """
    __tablename__ = "students"
    reg_number = Column(String, primary_key=True, unique=True)
    name = Column(String(80), unique=True)
    surname = Column(String(80), unique=True)
    programme = Column(String(80))
    # dob = Column(String(80), unique=True)
    degree_class = Column(String(80))
    graduation_year = Column(Integer())

    @property
    def full_name(self):
        return "%s %s" % (self.name, self.surname)

    def __repr__(self):
        return '<Name %r' % self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password1 = db.Column(db.String(100))
    password2 = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    company = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    # requests = relationship('Request', backref='user', lazy=True)


class Request(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=False)
    student_id = db.Column(String, nullable=False)
    institution_name=db.Column(String,nullable=False)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=False)
    verified = db.Column(Boolean(), default=False)
    file = db.Column(String)
