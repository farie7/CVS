from flask_login import current_user
from wtforms import StringField, Form, validators, SelectField, PasswordField, RadioField
from wtforms.fields.html5 import EmailField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired


class ApplicationConsentForm(Form):
    institution = SelectField(u'Institution ',
                              choices=[('hit', 'Harare Institute of Technology'), ('uz', 'University of Zimbabwe'),
                                       ('nust', 'National University of Science and Technology')]
                              , validators=[validators.InputRequired()])
    reg_number = StringField(label="Enter Student University ID", validators=[validators.InputRequired()])
    student_email = EmailField(label="Enter student's email address (Required)",
                               validators=[validators.InputRequired(), validators.Email()])
    user_email = EmailField(label="Email Address", validators=[validators.InputRequired(), validators.Email()])
    password = PasswordField(u'Password ', [
        validators.DataRequired(),
    ])


class PaymentVerificationRequestForm(Form):
    choices = [("certificate", "Certificate"), ("transcript", "Transcript")]
    choices_payee = [("student", "Student"), ("organisation", "Organisation")]
    request_type = RadioField(label="Verification Request", choices=choices)
    payee = RadioField(label="Payment ", choices=choices_payee)


class RequestVerificationForm(Form):
    choices = [('hit', 'Harare Institute of Technology'),
               ('uz', 'University of Zimbabwe'), ('nust', 'National University of Science and Technology')]

    institution = StringField("Select Institution", validators=[DataRequired()], id='institution', _name="institution")


class StudentVerificationForm(Form):
    reg_number = StringField(label="Enter Student University ID", validators=[validators.InputRequired()])
    student_email = EmailField(label="Enter student's email address (Required)",
                               validators=[validators.InputRequired(), validators.Email()])
    form = PaymentVerificationRequestForm()
    # user_email = EmailField(label="Email Address", validators=[validators.InputRequired(), validators.Email()])
    #
    # password = PasswordField(u'Password ', [
    #     validators.DataRequired(),
    # ])


class VerificationForm(Form):
    choices = [('hit', 'Harare Institute of Technology'),
               ('uz', 'University of Zimbabwe'), ('nust', 'National University of Science and Technology')]

    institution = StringField("Select Institution", validators=[DataRequired()], id='institution', _name="institution")
