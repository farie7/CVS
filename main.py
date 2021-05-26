import os
import sqlite3

from flask import Blueprint, render_template, request
from flask import send_file
from flask_login import login_required, current_user

import app
from create_pdf import print_document
from forms import VerificationForm
# from init_db import query_student
from models import Student, Request

main = Blueprint('main', __name__)

# app = app.create_app()
universities = {
    'hit': 'Harare Institute of Technology',
    'uz': 'University of Zimbabwe',
    'nust': 'National University of Science and Technology'
}

app.db.create_all()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


ROWS_PER_PAGE = 5


@main.route('/requests')
@login_required
def requests():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    # system_db = sqlite3.connect('system.db');

    request_data = Request.query.all()
    return render_template('requests.html', data=request_data)


@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = VerificationForm(request.form)
    verified = False
    if request.method == 'POST':
        if form.validate():
            # search student in database
            reg_number = form.reg_number.data
            institution = form.institution.data
            student = verify_student(reg_number, institution)
            req = Request()

            if not isinstance(student, Student):
                req.verified = False
                req.student_id = reg_number
                req.user_id = current_user.get_id()
                app.db.session.add(req)
                app.db.session.commit()
                return render_template('home.html', form=form, verified=verified, file=None)
            else:

                req.verified = True
                req.student_id = student.reg_number
                req.user_id = current_user.get_id()
                app.db.session.add(req)
                app.db.session.commit()

                print('request: ', req.student_id)
                print_document(student)
                file = student.reg_number + ".pdf"
                verified = True
            return render_template('home.html', form=form, verified=verified, file=file)

    return render_template('home.html', name=current_user.name, form=form, verified=None)


def verify_student(reg_number: str, institution: str):
    """

    :param reg_number:
    :param institution:
    """

    conn = sqlite3.connect('%s.db' % institution)
    statement = '''SELECT * FROM STUDENT WHERE REG_NUMBER=:reg_number '''
    cursor = conn.cursor()
    result = cursor.execute(statement, {"reg_number": reg_number})
    print('result: ', type(result), )
    student = Student()

    for row in result:
        if row[1] is None:
            return None
        else:
            student.name = row[1]
            student.surname = row[2]
            student.reg_number = row[3]
            student.graduation_year = row[4]

        conn.close()

        return student


@main.route('/download/<path:filename>')
def download(filename):
    # Download file
    path = os.path.join(app.config['STUDENTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)
