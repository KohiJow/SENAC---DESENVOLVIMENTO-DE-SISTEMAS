from flask import Flask

from db import db

from routes.eletronicos_routes import eletronicos_routes
#daqui pra baixo entendi porra nenhuma tenho q estuda cacete
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eletronicos.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(eletronicos_routes)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
