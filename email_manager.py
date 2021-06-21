<<<<<<< HEAD
from threading import Thread

from flask import flash
from flask_login import current_user
from flask_mail import Mail, Message

import app


# Asynchronously send email without blocking the other processes from operating
def async_send_mail(_app, msg, mail):
    with _app.app_context():
        try:
            mail.send(msg)
            return True
        except:
            return False


# send email to student
def send_email(recipient: str, password: str, template):
    # email configuration
    # configuration of mail
    _app = app.create_app()
    _app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    _app.config['MAIL_PORT'] = 465
    _app.config['MAIL_USE_TLS'] = False  # TLS is a protocol that encrypts and delivers mail securely
    _app.config[
        'MAIL_USE_SSL'] = True  # The Secure Sockets Layer (SSL) provides encryption for TCP/IP connections as they
    # transit the Internet and local networks between a client and a server.
    _app.config['MAIL_USERNAME'] = current_user.email
    _app.config['MAIL_PASSWORD'] = password
    mail = Mail(_app)
    msg = Message('Application for Consent', sender=_app.config['MAIL_USERNAME'], recipients=[recipient], html=template)

    thr = Thread(target=async_send_mail, args=[_app, msg, mail])  # Thread to run async send mail, provides
    # concurrency within a process.
    try:
        thr.start()
    except:
        return 'Error'
    return thr
=======
from threading import Thread

from flask_login import current_user
from flask_mail import Mail, Message

import app


# Asynchronously send email without blocking the other processes from operating
def async_send_mail(_app, msg, mail):
    with _app.app_context():
        mail.send(msg)


# send email to student
def send_email(recipient: str, password: str, template):
    # email configuration
    # configuration of mail
    _app = app.create_app()
    _app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    _app.config['MAIL_PORT'] = 465
    _app.config['MAIL_USE_TLS'] = False  # TLS is a protocol that encrypts and delivers mail securely
    _app.config[
        'MAIL_USE_SSL'] = True  # The Secure Sockets Layer (SSL) provides encryption for TCP/IP connections as they
    # transit the Internet and local networks between a client and a server.
    _app.config['MAIL_USERNAME'] = current_user.email
    _app.config['MAIL_PASSWORD'] = password
    mail = Mail(_app)
    msg = Message('Application for Consent', sender=_app.config['MAIL_USERNAME'], recipients=[recipient], html=template)

    thr = Thread(target=async_send_mail, args=[_app, msg, mail]) # Thread to run async send mail, provides
    # concurrency within a process.
    try:
        thr.start()
    except:
        return 'Error'
    return thr
>>>>>>> d63d48656716b47d598db2be1044e24f73a0d2ed
