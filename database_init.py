from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/UZ"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class StudentDetails(db.Model):
    __tablename__ = 'Student Details'

    RegNum = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String())
    Surname = db.Column(db.String())
    Program = db.Column(db.String())
    Email = db.Column(db.String())
    DOB = db.Column(db.String())
    GraduationYear = db.Colstrinumn(db.String())
    Address = db.Column(db.String())
    Photo = db.Column(db.String())
