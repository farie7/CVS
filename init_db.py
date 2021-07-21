import argparse
import os
import sqlite3

import pdfkit

import setup_app
from models import Request

parser = argparse.ArgumentParser(prog="init_db", usage="%(prog)s  [options]")
parser.add_argument("-i", "--init", help='Initialize database')
parser.add_argument("-d", "--database", help='Enter university database.')
parser.add_argument("-r", "--reg_number", help='Enter student reg number. ')

args = parser.parse_args()

class DatabaseException(Exception):
    __cause__ = "File not Found"
def initialise_db():
    try:
        uz = sqlite3.connect('dev_test/uz.db')  # You can create a new database by changing the name within the quotes
        nust = sqlite3.connect('dev_test/nust.db')
        hit = sqlite3.connect('dev_test/hit.db')
    except DatabaseException:
        raise DatabaseException("File not found")
    statement_1 = '''
                 CREATE TABLE REQUESTS(
            ID INT PRIMARY KEY     , 
            REG_NUMBER      TEXT   ,
           CREATED_AT date 
         );
         '''

    statement_1 = '''
                 CREATE TABLE REQUESTS(
            ID INT PRIMARY KEY     , 
            REG_NUMBER      TEXT   ,
           CREATED_AT date 
         );
         '''

    statement = '''
                 CREATE TABLE STUDENT(
            REC_ID INTEGER PRIMARY KEY     UNIQUE      , 
            FIRST_NAME           TEXT    NOT NULL,
            LAST_NAME           TEXT    NOT NULL,
            REG_NUMBER      TEXT   ,
            DEGREE_CLASS TEXT ,
            PROGRAMME TEXT, 
            YEAR_OF_GRADUATION INT
         );
         '''
    for cursor in [uz, nust, hit]:
        cursor.execute(statement)

    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ('001', 'Tinotenda', 'Ruzane', 'UZ01', 2011, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ('002', 'John', 'Rusambo', 'UZ03', 2011, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '003','Terrence', 'Zhou', 'UZ04', 2011, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '004','Lisa', 'Mutasa', 'UZ05', 2002, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '005','Charlene', 'Muzenda', 'UZ06', 2002, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '006','Peter', 'Chibwe', 'UZ07', 2016, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '007','Leo', 'Messo', 'UZ08', 2016, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '008','Tony', 'Montana', 'UZ09', 2012, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '009','Tinashe', 'Muskwe', 'UZ10', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )

    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '010','Richard', 'Taderera', 'UZ11', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )

    uz.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '011','Richard', 'Taderera', 'UZ11', 2020, 'MSC Cyber Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '001','Kudakwashe', 'Kuzvindiwana', 'NUST02', 2020, 'BSC Honours Degree in Computer Science','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '002','Njabulo', 'Ndlovhu', 'NUST01', 2007, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '003','Sibusiso', 'Vilakazi', 'NUST03', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '004','Nhlamulo', 'Muzi', 'NUST04', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '005','Scelo', 'Mxolisi', 'NUST05', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ('006', 'Michelle', 'Chimwanda', 'NUST06', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '007','Nigel', 'Muza', 'NUST07', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '008','Michael', 'Kapini', 'NUST08', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '009','Jessica', 'Magadlela', 'NUST09', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    nust.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '010','Cyril', 'Xulu', 'NUST10', 2020, 'Bsc Honours Degree in Information Security','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '001','Komborerai', 'Chikweshe', 'H140283B', 2020, 'BTech Honours Degree in Software Engineering','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '002','Cain', 'Murambi', 'H160183D', 2020, 'BTech Honours Degree in Software Engineering','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '003','Shingi', 'Kamwendo', 'H160283B', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '004','Omry', 'Marebera', 'H160532D', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '005','Yolanda', 'Chibaya', 'H160841Y', 2020, 'BTech Honours Degree in Computer Science','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '006','Nigel', 'Chonzi', 'H1604423C', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '007','Xander', 'Cage', 'H150295E', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '008','Ronald', 'Chigumbu', 'H150643r', 2020, 'BTech Honours Degree in Information Technology','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '009','Ian', 'Mugabe', 'H160419I', 2020, 'BTech Honours Degree in Information Security','2.1');'''

    )
    hit.execute(
        '''INSERT INTO STUDENT (ID,FIRST_NAME,LAST_NAME,REG_NUMBER,YEAR_OF_GRADUATION, PROGRAMME, DEGREE_CLASS)
    VALUES ( '010','Anesu', 'Jari', 'H150834EB', 2020, 'BTech Honours Degree in Information Security','2.1');'''

    )
    for conn in [hit, uz, nust]:
        conn.commit()
        conn.close()


def delete_databases():
    for d in ['hit.db', 'nust.db', 'uz.db']:
        database = "dev_test/%s" % d
        if os.path.exists("%s" % database):
            os.remove(database)
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
