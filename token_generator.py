from itsdangerous import URLSafeTimedSerializer

import app


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.create_app().config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.create_app().config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=7200):
    serializer = URLSafeTimedSerializer(app.create_app().config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.create_app().config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email
