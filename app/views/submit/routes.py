from flask import Blueprint, render_template

submit_blueprint = Blueprint('submit', __name__)


@submit_blueprint.route('/submit')
def index():
    return render_template('submit.html')