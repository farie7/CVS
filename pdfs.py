import pdfkit
from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # name = "Farai"
    html = render_template('base.html')
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response


if __name__ == "__main__":
    app.run(debug=True)
