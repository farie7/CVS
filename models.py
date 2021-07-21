from datetime import datetime, time

from flask_login import UserMixin
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from time import time
import json
from setup_app import db
Base = declarative_base()


class Student(Base):
    """
    Student model
    """
    __tablename__ = "students"
    id = db.Column(Integer, primary_key=True, unique=True)
    reg_number = db.Column(String, nullable=False)
    namez = db.Column(String(80), unique=True)
    surname = db.Column(String(80), unique=True)
    programme = db.Column(String(80))

    # dob = Column(String(80), unique=True)
    degree_class = db.Column(String(80))

    graduation_year = db.Column(Integer())

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
    last_request_view_time = db.Column(db.DateTime)
    # notifications = db.relationship('Notification', backref='user',
    #                                 lazy='dynamic')
    notification_received = db.relationship('RequestStatus', foreign_keys='RequestStatus.user_id',
                                            backref='notify', lazy='dynamic')

    def request_change(self):
        #     from sqlalchemy import text
        #
        #     sql = text("select status from request_status order by timestamp desc LIMIT 1;")
        #     result = db.engine.execute(sql)
        #     names = [row[0] for row in result]
        #     return len(names)
        last_read_time = self.last_request_view_time or datetime(1900, 1, 1)
        print("last read time :", last_read_time)
        print("timestamp : ", RequestStatus.timestamp)
        return RequestStatus.query.filter_by(notify=self).filter(
            RequestStatus.timestamp > last_read_time).count()

        # return len(RequestStatus.query.all())

    # def add_notification(self, name, data):
    #     self.notifications.filter_by(name=name).delete()
    #     n = Notification(name=name, payload_json=json.dumps(data), user=self)
    #     db.session.add(n)
    #     return n


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
    user_id = db.Column(String, db.ForeignKey('user.id'), nullable=True)
    student = db.Column(String, nullable=True, unique=True)
    token_id = db.Column(String, nullable=False, unique=True)
    # confirmed = db.Column(Boolean, default=False)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=True)
    status = db.Column(String, default='init', nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Message(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String, nullable=True)
    message = db.Column(String, nullable=True)
    date_created = db.Column(Date(), default=datetime.now())
    time_created = db.Column(String, nullable=True)

# class Notification(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     timestamp = db.Column(db.Float, index=True, default=time)
#     payload_json = db.Column(db.Text)

# def get_data(self):
#     return json.loads(str(self.payload_json))

# class Institution(Base):
#     __tablename__ = 'institutions'
#     id = db.Column(Integer, primary_key=True, autoincrement=False)
#     name = db.Column(String, nullable=False)
#     students = db.relationship('Student', backref='institution', lazy=True)
