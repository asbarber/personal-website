import flask

cv = flask.Blueprint('cv', __name__, template_folder="views")

@cv.route('/cv', methods = ['GET'])
def getCV():
	return flask.render_template("cv.html")