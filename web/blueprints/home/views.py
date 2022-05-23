from flask import render_template

from utility.mkblueprint import ProjectBlueprint

blueprint = ProjectBlueprint('/', __name__)


@blueprint.route(blueprint.url, methods=['GET', 'POST'])
def home():
    return render_template('home/home.html', title='Home')