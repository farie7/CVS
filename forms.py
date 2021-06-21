
from wtforms import StringField, Form, validators, SelectField, PasswordField
from wtforms.fields.html5 import EmailField


class VerificationForm(Form):
    institution = SelectField(u'Institution ',
                              choices=[('hit', 'Harare Institute of Technology'), ('uz', 'University of Zimbabwe'),
                                       ('nust', 'National University of Science and Technology')]
                              , validators=[validators.InputRequired()])
    # reg_number = StringField(label="Student Registration Number", validators=[validators.InputRequired()])
    email = EmailField(label="Student Email", validators=[validators.InputRequired(), validators.Email()])

    password = PasswordField(u'Enter Password (Email) ', [
        validators.DataRequired(),
    ])
