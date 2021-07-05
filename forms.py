from flask_login import current_user
from wtforms import StringField, Form, validators, SelectField, PasswordField
from wtforms.fields.html5 import EmailField


class ApplicationConsentForm(Form):
    institution = SelectField(u'Institution ',
                              choices=[('hit', 'Harare Institute of Technology'), ('uz', 'University of Zimbabwe'),
                                       ('nust', 'National University of Science and Technology')]
                              , validators=[validators.InputRequired()])
    # reg_number = StringField(label="Student Registration Number", validators=[validators.InputRequired()])
    student_email = EmailField(label="Enter student's email address",
                               validators=[validators.InputRequired(), validators.Email()])
    user_email = EmailField(label="Email Address", validators=[validators.InputRequired(), validators.Email()])
    password = PasswordField(u'Password ', [
        validators.DataRequired(),
    ])
