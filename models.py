<<<<<<< HEAD
from datetime import datetime, time

from flask_login import UserMixin, current_user
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
    def get_number_of_messages(self):
        return Message.query.filter_by(user_id=current_user.id).count()


class Request(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=False)
    student_id = db.Column(String, nullable=False)
    institution_name = db.Column(String, nullable=True)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=False)
    verified = db.Column(Boolean(), default=False)
    file = db.Column(String)


class RequestStatus(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=True)
    student = db.Column(String, nullable=True, unique=True)
    token_id = db.Column(String, nullable=False, unique=True)
    # confirmed = db.Column(Boolean, default=False)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=True)
    status = db.Column(String, default='init', nullable=True)


class Message(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=True)

    message = db.Column(String, nullable=True)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=True)
=======

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
    institution_name = db.Column(String, nullable=True)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=False)
    verified = db.Column(Boolean(), default=False)
    file = db.Column(String)


class RequestStatus(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=True)
    student = db.Column(String, nullable=True, unique=True)
    token_id = db.Column(String, nullable=False, unique=True)
    # confirmed = db.Column(Boolean, default=False)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=True)
    status = db.Column(String, default='init', nullable=True)
>>>>>>> d63d48656716b47d598db2be1044e24f73a0d2ed
