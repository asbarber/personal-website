import flask

home = flask.Blueprint('home', __name__, template_folder="templates")

@home.route('/home', methods = ['GET'])
def getHome():
	return "Hello Home"