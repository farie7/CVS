import datetime
import os
import sqlite3
from threading import Thread

from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask import send_file
from flask_login import login_required, current_user
from flask_mail import Message, Mail
from sqlalchemy import desc, asc

import app
from create_pdf import print_document
from email_manager import send_email
from forms import VerificationForm
# from init_db import query_student
from models import Student, Request, RequestStatus
from token_generator import confirm_token, generate_confirmation_token

main = Blueprint('main', __name__)

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


ROWS_PER_PAGE = 10


@main.route('/requests')
@login_required
def requests():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    request_data = RequestStatus.query.filter_by(user_id=current_user.id).order_by(
        desc(RequestStatus.time_created)).paginate(
        page=page,
        per_page=ROWS_PER_PAGE)

    return render_template('requests.html', data=request_data)


@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = VerificationForm(request.form)
    global institute
    req = RequestStatus()
    req.user_id = current_user.id

    if request.method == 'POST' and form.validate():
        institute = universities[form.institution.data]
        # Generate token for confirmation url using recipient's email
        token = generate_confirmation_token(form.email.data)
        # Urls for confirm and reject responses
        confirm_url = url_for('main.handle_consent_approved', token=token, _external=True)
        reject_url = url_for('main.handle_consent_approved', token=token, _external=True)
        message = "%s is seeking your approval of consent to verify your certificate from %s." % (
            current_user.company, institute)

        # create html page with message body and html links
        html = render_template('student_consent_request.html', confirm_url=confirm_url, reject_url=reject_url,
                               message=message)

        try:
            send_email(recipient=form.email.data, password=form.password.data, template=html)
            req.token_id = token
            req.status = "PENDING"
            if hasattr(req, 'student'):
                setattr(req,
                'student',form.email.data)
            app.db.session.add(req)
            app.db.session.commit()
            flash('You have successfully sent your request has been sent', 'success')

        except Exception as e:
            flash(e.__str__(), "danger")

    #     # search student in database
    #     reg_number = form.reg_number.data
    #     institution = form.institution.data
    #     student = verify_student(reg_number, institution)
    #     req = Request()
    #     req.user_id = current_user.get_id()
    #     if not isinstance(student, Student):
    #         file = 'N/A'
    #         req.student_id = reg_number
    #         req.file = file
    #         req.verified = False
    #     else:
    #         verified = True
    #         file = student.reg_number + ".pdf"
    #         req.file = file
    #         req.verified = True
    #         req.student_id = student.reg_number
    #         print_document(student, institution)
    #     req.institution_name = universities[institution]
    #     req.time_created = datetime.datetime.now().strftime("%H:%M:%S")
    #     app.db.session.add(req)
    #
    #     app.db.session.commit()
    #
    #     return render_template('home.html', form=form, verified=verified, file=file)

    return render_template('home.html', name=current_user.name, form=form, verified=None)


@main.route('/download/<path:filename>')
def download(filename):
    # Download file
    path = os.path.join(app.create_app().config['STUDENTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)


@main.route('/confirm/<token>')
@login_required
def handle_consent_approved(token):
    req = RequestStatus.query.filter_by(token_id=token).first()
    # req.status = "CONFIRMED"
    setattr(req, 'status', 'CONFIRMED')
    setattr(req, 'time_created', datetime.datetime.now().strftime("%H:%M:%S"))

    app.db.session.add(req), app.db.session.commit()
    return render_template('consent_approved.html', institute=institute)


@main.route('/decline/<token>')
@login_required
def handle_consent_reject(token):
    # query consent request by token
    req = RequestStatus.query.filter_by(token_id=token).first()
    setattr(req, 'status', 'REJECTED')
    setattr(req, 'time_created', datetime.datetime.now().strftime("%H:%M:%S"))
    app.db.session.add(req)
    app.db.session.commit()
    return render_template('consent_rejected.html', institute=institute)


if __name__ == '__main__':
    app = app.create_app()
    app.app_context().push()
    app.run(debug=True)
