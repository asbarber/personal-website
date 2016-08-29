import flask

passions = flask.Blueprint('passions', __name__, template_folder="views")

@passions.route('/passions', methods = ['GET'])
def getPassions():
	return flask.render_template("passions.html")