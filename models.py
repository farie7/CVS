from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    """
    Student model
    """
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(String, unique=True)
    name = Column(String(80), unique=True)
    surname = Column(String(80), unique=True)
    institution = Column(String(80), nullable=False)
    programme = Column(String(80))
    dob = Column(String(80), unique=True)
    address = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    graduation_year = Column(String(120))

    # institution_id = Column(Integer, ForeignKey('institution.id'),
    #                         nullable=False)

    def __init__(self, reg_number, name, surname,institution, programme, dob, address,email, graduation_year) -> None:
        self.institution = institution
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
