import os
import sqlite3

import pdfkit
from flask import Flask, request, send_file
from flask import render_template

from forms import VerificationForm

# from init_db import query_student

app = Flask(__name__)
# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'verified_students')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = VerificationForm(request.form)
    verified = False
    if request.method == 'POST':

        if form.validate():
            # search student in database
            reg_number = form.reg_number.data
            institution = form.institution.data

            student = verify_student(reg_number, institution)
            if not student:
                return render_template('home.html', form=form, verified=verified, file=None)
            generate_pdf(student)
            file = student['reg_number'] + ".pdf"
            verified = True
            return render_template('home.html', form=form, verified=verified, file=file)

    return render_template('home.html', form=form, verified=None)


def generate_pdf(student):
    """

    :param student:
    :return:
    """

    output = os.path.join(uploads_dir, student['reg_number'] + '.pdf')
    html = render_template('verification_result.html', student=student)
    pdfkit.from_string(html, output)


def verify_student(reg_number, institution):
    """

    :param reg_number:
    :param institution:
    """
    if institution:
        conn = sqlite3.connect('%s.db' % institution)
        statement = '''SELECT * FROM STUDENT WHERE REG_NUMBER=:reg_number '''
        cursor = conn.cursor()
        result = cursor.execute(statement, {"reg_number": reg_number})
        student = {}
        for row in result:
            student['first_name'] = row[1]
            student['last_name'] = row[2]
            student['reg_number'] = row[3]
            student['year'] = row[4]
        conn.close()

        return student


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    """

    :return:
    """
    form = VerificationForm(request.form)
    verified = False
    if request.method == 'POST':

        if form.validate():
            # search student in database
            reg_number = form.reg_number.data
            institution = form.institution.data

            student = verify_student(reg_number, institution)
            if not student:
                return render_template('home.html', form=form, verified=verified, file=None)
            generate_pdf(student)
            file = student['reg_number'] + ".pdf"
            verified=True
            return render_template('home.html', form=form, verified=verified, file=file)

    return render_template('home.html', form=form, verified=None)


@app.route('/download/<path:filename>')
def download(filename):
    # Download file
    path = os.path.join(uploads_dir, filename)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)