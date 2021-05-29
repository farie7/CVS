import argparse
import os
import sqlite3

import pdfkit

import app
from models import Request

parser = argparse.ArgumentParser(prog="init_db", usage="%(prog)s  [options]")
parser.add_argument("-i", "--init", help='Initialize database')
parser.add_argument("-d", "--database", help='Enter university database.')
parser.add_argument("-r", "--reg_number", help='Enter student reg number. ')

args = parser.parse_args()


def initialise_db():
    uz = sqlite3.connect('uz.db')  # You can create a new database by changing the name within the quotes
    nust = sqlite3.connect('nust.db')
    hit = sqlite3.connect('hit.db')

    statement_1 = '''
                 CREATE TABLE REQUESTS(
            ID INT PRIMARY KEY     , 
            REG_NUMBER      TEXT UNIQUE  ,
           CREATED_AT date 
         );
         '''

    statement = '''
                 CREATE TABLE STUDENT(
            ID INT PRIMARY KEY     , 
            FIRST_NAME           TEXT    NOT NULL,
            LAST_NAME           TEXT    NOT NULL,
            REG_NUMBER      TEXT UNIQUE  ,
            DEGREE_CLASS TEXT ,
            PROGRAMME TEXT, 
            YEAR_OF_GRADUATION INT
         );
         '''
    for cursor in [uz, nust, hit]:
        cursor.execute(statement)
    # system.execute(statement_1)
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Tinotenda', 'Ruzane', 'UZ01', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'John', 'Rusambo', 'UZ03', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Terrence', 'Zhou', 'UZ04', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Lisa', 'Mutasa', 'UZ05', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Charlene', 'Muzenda', 'UZ06', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Peter', 'Chibwe', 'UZ07', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Leo', 'Messo', 'UZ08', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Tony', 'Montana', 'UZ09', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Tinashe', 'Muskwe', 'UZ10', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )

    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Kudakwashe', 'Kuzvindiwana', 'NUST02', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Njabulo', 'Ndlovhu', 'NUST01', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Sibusiso', 'Vilakazi', 'NUST03', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Nhlamulo', 'Muzi', 'NUST04', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Scelo', 'Mxolisi', 'NUST05', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Michelle', 'Chimwanda', 'NUST06', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Nigel', 'Muza', 'NUST07', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Michael', 'Kapini', 'NUST08', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Jessica', 'Magadlela', 'NUST09', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Cyril', 'Xulu', 'NUST10', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Komborerai', 'Chikweshe', 'H140283B', 2020, 'BTech Honours Degree in Software Engineering','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Cain', 'Murambi', 'H160183D', 2020, 'BTech Honours Degree in Software Engineering','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Shingi', 'Kamwendo', 'H160283B', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Omry', 'Marebera', 'H160532D', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Yolanda', 'Chibaya', 'H160841Y', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Nigel', 'Chonzi', 'H1604423C', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Xander', 'Cage', 'H150295E', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Ronald', 'Chigumbu', 'H150643r', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Ian', 'Mugabe', 'H160419I', 2020, 'BTech Honours Degree in Information Security','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( 'Anesu', 'Jari', 'H150834EB', 2020, 'BTech Honours Degree in Information Security','2.1');'''

    )
    for conn in [hit, uz, nust]:
        conn.commit()
        conn.close()


def delete_databases():
    for d in ['hit.db', 'nust.db', 'uz.db']:
        if os.path.exists(d):
            os.remove(d)
            print("Databases deleted.")
        else:
            print("The database %s do not exist. " % (d))


def reinitialise_db():
    delete_databases()
    initialise_db()
    print("Reinitialisation complete.")


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
    """

    :param student:
    :return:
    """
    statement = "This is to verify that %s %s , registration number %s graduated at our university" \
                " in %s" % (student['first_name'], student['last_name'], student['reg_number'], student['year'])
    output = student['reg_number'] + '.pdf'
    pdf = pdfkit.from_string(statement, output)
    return pdf


if args.init == "I":
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
