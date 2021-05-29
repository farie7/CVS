import datetime
import os
import sqlite3

from flask import Blueprint, render_template, request
from flask import send_file
from flask_login import login_required, current_user
from sqlalchemy import desc, asc

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

    request_data = Request.query.filter_by(user_id=current_user.id).order_by(desc(Request.time_created)).paginate(
        page=page,
        per_page=ROWS_PER_PAGE)

    return render_template('requests.html', data=request_data)


@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = VerificationForm(request.form)

    if request.method == 'POST' and form.validate():
        verified = False
        if form.validate():
            # search student in database
            reg_number = form.reg_number.data
            institution = form.institution.data
            student = verify_student(reg_number, institution)
            req = Request()
            req.user_id = current_user.get_id()
            if not isinstance(student, Student):
                file = 'N/A'
                req.student_id = reg_number
                req.file = file
                req.verified = False
            else:
                verified = True
                file = student.reg_number + ".pdf"
                req.file = file
                req.verified = True
                req.student_id = student.reg_number
                print_document(student, institution)
            req.institution_name = universities[institution]
            req.time_created = datetime.datetime.now().strftime("%H:%M:%S")
            app.db.session.add(req)

            app.db.session.commit()

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

        conn.close()

        return student


@main.route('/download/<path:filename>')
def download(filename):
    # Download file
    path = os.path.join(app.create_app().config['STUDENTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app = app.create_app()
    app.app_context().push()
    app.run(debug=True)
