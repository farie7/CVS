from itsdangerous import URLSafeTimedSerializer

import setup_app


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(setup_app.create_app().config['SECRET_KEY'])
    return serializer.dumps(email, salt=setup_app.create_app().config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(setup_app.create_app().config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=setup_app.create_app().config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email
