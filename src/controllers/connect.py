import flask

connect = flask.Blueprint('connect', __name__, template_folder="views")

@connect.route('/connect', methods = ['GET'])
def getConnect():
	return flask.render_template("connect.html")