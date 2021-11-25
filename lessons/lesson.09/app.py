from flask import Flask, url_for
from flask_migrate import Migrate

from models import db
from views.products import products_app


app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=(
        "postgresql+psycopg2://shop:password@localhost:5432/shop"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

app.register_blueprint(products_app, url_prefix="/products")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/")
def index_view():
    return "Hello world!!!"


@app.route("/info/")
def info_view():
    return {
        "routes": {
            "url_for('hello_user')": url_for("hello_user"),
            "url_for('hello_user', username='OTUS')": url_for(
                "hello_user", username="OTUS"),
        }
    }


@app.route("/hello/")
@app.route("/hello/<username>/")
def hello_user(username="Wold"):
    return f"Hello {username}!"


@app.route("/items/<int:item_id>/")
def get_item_by_id(item_id):
    return {"item": item_id}


# filters

@app.template_filter("datetimeformat")
def datetime_format(value, dt_format="%d.%m.%Y %H:%M"):
    return value.strftime(dt_format)
