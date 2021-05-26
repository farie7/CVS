# from flask import Flask
# from sqlalchemy.orm import sessionmaker
#
# from databases import engine_uz, engine_cut, engine_hit
# from models import Student
#
# app = Flask(__name__)
#
# def create_app():
#
#     app = Flask(__name__)
#
#     app.config['SECRET_KEY'] = 'secret-key-goes-here'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     db.init_app(app)
#
#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)
#
#     from models import User
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))
#
#     # blueprint for auth routes in our app
#     from auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)
#
#     # blueprint for non-auth parts of app
#     from main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     return app
# # class Institution(Base):
# #     __tablename__ = 'institutions'
# #     id = Column(Integer, primary_key=True, autoincrement=False)
# #     name = Column(String, nullable=False)
# #     students = relationship('Student', backref='institution', lazy=True)
# #
#
#
# def query_students(institution: str, reg_number=None, by_reg_number=False):
#     """
#
#     :param reg_number:
#     :param institution:
#     :param by_reg_number:
#     """
#     if by_reg_number is True and reg_number is not None:
#         try:
#             session = None
#             if institution == "uz":
#                 Session = sessionmaker(bind=engine_uz)
#                 session = Session()
#
#             elif institution == "cut":
#                 Session = sessionmaker(bind=engine_cut)
#                 session = Session()
#
#             elif institution == "hit":
#
#                 Session = sessionmaker(bind=engine_hit)
#                 session = Session()
#             else:
#                 print("Please select a valid university !!")
#             result = session.query(Student).filter_by(reg_number=reg_number).all()
#             print(result)
#         except Exception as error:
#             print("Error: ", error)
#     else:
#         try:
#             session = None
#             if institution == "uz":
#                 Session = sessionmaker(bind=engine_uz)
#                 session = Session()
#
#             elif institution == "cut":
#                 Session = sessionmaker(bind=engine_cut)
#                 session = Session()
#
#             elif institution == "hit":
#
#                 Session = sessionmaker(bind=engine_hit)
#                 session = Session()
#             else:
#                 print("Please select a valid university !!")
#             result = session.query(Student).all()
#             print(result)
#         except Exception as error:
#             print("Error: ", error)
#
#
# query_students('hit', reg_number='H200345H', by_reg_number=True)
# if __name__ == "__main__":
#     app.run(debug=True)
