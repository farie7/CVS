from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request, redirect, url_for
from flask import render_template
from flask import make_response
import pdfkit

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #name = "Farai"
    html = render_template('test.html')
    pdf  = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response




if __name__ == "__main__":
    app.run(debug=True)
