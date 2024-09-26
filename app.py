from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from data.db import db
from models.country_model import Country
from models.city_model import City
from models.location_model import Location
from models.type_model import Type
from models.indusrty_model import Industry
from models.target_model import Target
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/second_war_solution3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///second_war_solution.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


@app.route('/')
def wellcome():
    country = Country(name='USA')
    db.session.add(country)
    db.session.commit()
    countries_to_return = Country.query.all()
    if countries_to_return is None:
        return 'none'
    #if countries_to_return is not None:
    print (str(countries_to_return[0]))
        #return jsonify(countries_to_return)
    return 'wellcome to second war solution!'


if __name__ == '__main__':
    app.run(debug=True)




