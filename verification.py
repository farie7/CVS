import os
import sqlite3

from dev_test.databases import database_exists
from setup_app import create_app

from models import Student

app = create_app()


def non_nullable(func):
    """
    Assert that the database exists
    """

    def inner(arg, arg_1):
        institution_database = 'dev_test/%s.db' % arg_1

        assert os.path.exists(institution_database), app.logger.error(
            "{} does not exist.".format(institution_database))
        return func(arg, arg_1)
    return inner


@non_nullable
def verify_student(reg_number: str, institution: str) -> Student:
    """
    :param reg_number:
    :param institution:
    """
    institution_database = 'dev_test/%s.db' % institution

    conn = sqlite3.connect(institution_database)
    statement = '''SELECT * FROM STUDENT WHERE REG_NUMBER=:reg_number '''
    cursor = conn.cursor()
    student = Student()

    result = cursor.execute(statement, {"reg_number": reg_number})
    print('result: ', type(result), )

    for row in result:
        if row[1] is None:

            return None
        else:
            student.name = row[1]
            student.surname = row[2]
            student.reg_number = row[3]
            student.graduation_year = row[6]
            student.programme = row[5]
            student.degree_class = row[4]

        conn.close()

        return student
