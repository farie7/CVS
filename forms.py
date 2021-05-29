from wtforms import StringField, Form, validators, SelectField


class VerificationForm(Form):
    reg_number = StringField(label="Student Registration Number", validators=[validators.InputRequired()])
    institution = SelectField(label="Institution",
                              choices=[('hit', 'Harare Institute of Technology'), ('uz', 'University of Zimbabwe'),
                                       ('nust', 'National University of Science and Technology')]
                              , validators=[validators.InputRequired()])
