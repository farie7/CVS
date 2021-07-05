import sqlite3

from app import app
from models import Student


def verify_student(reg_number: str, institution: str):
    """

    :param reg_number:
    :param institution:
    """

    conn = sqlite3.connect('%s.db' % institution)
    statement = '''SELECT * FROM STUDENT WHERE REG_NUMBER=:reg_number '''
    cursor = conn.cursor()
    student = Student()
    try:
        result = cursor.execute(statement, {"reg_number": reg_number})
        print('result: ', type(result), )

        for row in result:
            if row[1] is None:
                return None
            else:
                print(row[1],
                      row[2],
                      row[3],
                      row[4],
                      row[5], row[6])
                student.name = row[1]
                student.surname = row[2]
                student.reg_number = row[3]
                student.graduation_year = row[6]
                student.programme = row[5]
                student.degree_class = row[4]

    except Exception as e:
        app.logger.error(e)
    finally:
        conn.close()
    return student
