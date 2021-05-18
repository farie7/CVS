import argparse
import os
import sqlite3

import pdfkit
from flask import Flask

parser = argparse.ArgumentParser(prog="init_db", usage="%(prog)s  [options]")
parser.add_argument("-i", "--init", help='Initialize database')
parser.add_argument("-d", "--database", help='Enter university database.')
parser.add_argument("-r", "--reg_number", help='Enter student reg number. ')

args = parser.parse_args()

app = Flask(__name__)


def initialise_db():
    uz = sqlite3.connect('uz.db')  # You can create a new database by changing the name within the quotes
    nust = sqlite3.connect('nust.db')
    hit = sqlite3.connect('hit.db')

    statement = '''
                 CREATE TABLE STUDENT(
            ID INT PRIMARY KEY     NOT NULL,
            FIRST_NAME           TEXT    NOT NULL,
            LAST_NAME           TEXT    NOT NULL,
          
            REG_NUMBER        CHAR(50),
            YEAR_OF_GRADUATION  INT
         );
         '''
    for cursor in [uz, nust, hit]:
        cursor.execute(statement)
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION)
    VALUES (1, 'Tinotenda', 'Ruzane', 'UZ01', 2020);'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION)
    VALUES (1, 'Kudakwashe', 'Kuzvindiwana', 'NUST02', 2020);'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION)
    VALUES (1, 'Komborerai', 'Chikweshe', 'H140283B', 2020);'''

    )
    for conn in [hit, uz, nust]:
        conn.commit()
        conn.close()


def delete_databases():
    for d in ['hit.db', 'nust.db', 'uz.db']:
        if os.path.exists(d):
            os.remove(d)
        else:
            print("The database %s do not exist. " % (d))


def reinitialise_db():
    delete_databases()
    initialise_db()


def query_student(database: str, reg_number: str):
    print(database, reg_number)
    statement = '''SELECT * FROM STUDENT WHERE REG_NUMBER=:reg_number '''
    conn = None
    if database:
        conn = sqlite3.connect('%s.db' % database)
        cursor = conn.cursor()
        result = cursor.execute(statement, {"reg_number": reg_number})
        student = {}
        for row in result:
            student['first_name'] = row[1]
            student['last_name'] = row[2]
            student['reg_number'] = row[3]
            student['year'] = row[4]
        print_certificate(student)

        conn.close()


def print_certificate(student):
    statement = "This is to verify that %s %s , registration number %s graduated at our university" \
                "in %s" % (student['first_name'], student['last_name'], student['reg_number'], student['year'])
    output = student['reg_number'] + '.pdf'
    pdf = pdfkit.from_string(statement, output)
    return pdf


if args.init == "I":
    print("Initialization database")
    initialise_db()
elif args.init == "D":
    delete_databases()
elif args.init == "R":
    reinitialise_db()
elif args.database and args.reg_number:
    query_student(args.database, args.reg_number)
elif args.init not in ['R', 'I', 'D']:
    print('Invalid option selected')
else:
    print("no option entered")
