import flask

home = flask.Blueprint('home', __name__, template_folder="views")

@home.route('/', methods = ['GET'])
@home.route('/home', methods = ['GET'])
def getHome():
	return flask.render_template("home.html")



