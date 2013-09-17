from flask import Blueprint

from .views import Feedback


def create_blueprint(blueprint_name, conf):
    feedback_blueprint = Blueprint(blueprint_name, __name__, **conf)

    feedback_blueprint.add_url_rule('/', view_func=Feedback.as_view('feedback'))

    return feedback_blueprint
