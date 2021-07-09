import datetime
import logging
import os
from logging.config import dictConfig

from flask import Blueprint, render_template, request, flash, url_for, Flask, Response, jsonify, redirect, g
from flask import send_file
from flask_login import login_required, current_user
from sqlalchemy import desc

import setup_app
from dev_test.databases import save, get_institution_details
from email_manager import send_email
from forms import ApplicationConsentForm, RequestVerificationForm, StudentVerificationForm, UniversitySelectionForm, \
    PaymentVerificationRequestForm
# from init_db import query_student
from models import RequestStatus, Message, Student
from verification import verify_student
from token_generator import generate_confirmation_token, confirm_token

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s %(levelname)s %(name)s %(threadName)s: %(message)s')

universities = {
    'hit': 'Harare Institute of Technology',
    'uz': 'University of Zimbabwe',
    'nust': 'National University of Science and Technology'
}

app = setup_app.create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


ROWS_PER_PAGE = 10


@app.route('/requests')
@login_required
def requests():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    request_data = RequestStatus.query.filter_by(user_id=current_user.id).order_by(
        desc(RequestStatus.time_created)).paginate(
        page=page,
        per_page=ROWS_PER_PAGE)

    return render_template('requests.html', data=request_data)


@app.route('/student-verification')
def student_verification():
    # instantiate student verification form

    if request.method == "POST":
        payment_form = StudentVerificationForm(request.form)
        # return render_template('verification-page.html',form=form)
    else:
        form = StudentVerificationForm()
        return render_template('verification-page.html', form=form)


@app.route('/messages')
@login_required
def messages():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    data = Message.query.filter_by(user_id=current_user.id).order_by(
        desc(Message.date_created)).paginate(
        page=page,
        per_page=ROWS_PER_PAGE)

    return render_template('messages.html', data=data)


@app.route('/select-university', methods=["POST", "GET"])
@login_required
def select_university():
    if request.method == "POST":
        form = UniversitySelectionForm(request.form)
        assert form.institution.data.lower() in universities.keys(), "Unavailable"
        g.institution = universities[form.institution.data.lower()]
        g.university = form.institution.data
        app.logger.debug("Value of g.university is {}".format(g.institution))
        return render_template('verification-page.html', form=StudentVerificationForm())
    else:
        form = UniversitySelectionForm()

    return render_template('request_verification.html', form=form)


@app.route('/year-of-oldest-record/<institution>', methods=['GET'])
def get_institution(institution: str):
    """
    @desc: Get institution data institution
    @param: institution
    @return: JSON response year of the oldest record in @institution


    """
    year_of_oldest_record: int = 0
    if request.method == 'GET':
        form = RequestVerificationForm(request.form)
        try:
            year_of_oldest_record, number_of_students = get_institution_details(institution)
            app.logger.debug(
                " year_of_oldest_record, number_of_students : {}, {}".format(year_of_oldest_record, number_of_students))
            json_data = [{"institution": universities[institution]},
                         {"year_of_oldest_record": year_of_oldest_record}
                , {"number_of_students": number_of_students}]
            return jsonify(json_data)
        except Exception as e:
            app.logger.error("Error :\n {}".format(e))
            return jsonify({"message": "Student is not found."})


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = ApplicationConsentForm(request.form)
    return render_template('home.html', form=form)


@app.route('/verify-student-exists', methods=['GET'])
def handle_verify_student_exists():
    if request.method == 'GET':
        reg_number = request.args.get('reg_number')
        institution = request.args.get('institution')

        app.logger.debug("{}: {}".format(reg_number, institution))

        try:

            student = verify_student(reg_number, institution)
            # use if else
            if isinstance(student, Student):
                message = "We can confirm the student with ID {} has been found in the {}" \
                    .format(reg_number, universities[institution])
            else:
                message = "Student  {} not found at {}" \
                    .format(reg_number, universities[institution])
            return jsonify(message)
        except Exception as e:
            app.logger.error(e)


# @login_required
# @app.route('/')

@app.route('/send_email', methods=['POST'])
@login_required
def handle_send_email():
    form = ApplicationConsentForm(request.form)
    global institute
    req = RequestStatus()
    req.user_id = current_user.id
    app.logger.debug(request.method)
    if request.method == 'POST' and form.validate():
        institute = universities[form.institution.data]
        # Generate token for confirmation url using recipient's email
        token = generate_confirmation_token(form.student_email.data)
        # Urls for confirm and reject responses
        confirm_url = url_for('handle_consent_approved', token=token, _external=True)
        reject_url = url_for('handle_consent_rejected', token=token, _external=True)
        message = "%s is seeking your approval of consent to verify your certificate from %s." % (
            current_user.company, institute)

        # create html page with message body and html links
        html = render_template('student_consent_request.html', confirm_url=confirm_url, reject_url=reject_url,
                               message=message)

        try:
            send_email(recipient=form.student_email.data, password=form.password.data, template=html)
            req.token_id = token
            req.status = "PENDING"
            if hasattr(req, 'student'):
                setattr(req, 'student', form.student_email.data)
            save(req)
            flash('Your have successfully sent your request.', 'success')
            app.logger.info("Message successfully sent")

        except Exception as e:
            app.logger.error(e)
            flash('Your email has not been sent. Please try again.', 'danger')
    else:
        app.logger.warn("form not valid or request method == %s ") % request.method

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
    return redirect('home')


@app.route('/download/<path:filename>')
def download(filename):
    # Download file
    path = os.path.join(app.create_app().config['STUDENTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)


@app.route('/confirm/<token>')
def handle_consent_approved(token: str):
    try:
        email = confirm_token(token)
        app.logger.debug('Token: {} , email: {}'.format(token, email))

    except Exception as e:
        app.logger.error('Exception in handle consent {}'.format(e))

    req = RequestStatus.query.filter_by(token_id=token).first()

    # req.status = "CONFIRMED"
    if req:
        req.status = 'CONFIRMED'
        req.time_created = datetime.datetime.now().strftime("%H:%M:%S")
        obj = Message()
        obj.user_id = current_user.id
        student = req.student
        message = "{} has approved your request to verify their certificate.".format(student)
        obj.message = message
        obj.time_created = datetime.datetime.now().strftime("%H:%M:%S")
        from dev_test.databases import save
        save(req)
        save(obj)

        return render_template('consent_approved.html')
    return render_template('error_page.html')


@app.route('/decline/<token>')
def handle_consent_rejected(token: str):
    # query consent request by token
    req = RequestStatus.query.filter_by(token_id=token).first()
    if req:
        setattr(req, 'status', 'REJECTED')
        setattr(req, 'time_created', datetime.datetime.now().strftime("%H:%M:%S"))
        from dev_test.databases import save
        save(req)
    return render_template('consent_rejected.html', institute=institute)


if __name__ == '__main__':
    main = setup_app.create_app()
    main.app_context().push()
    app.run(debug=True, host="0.0.0.0")
