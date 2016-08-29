import flask

portfolio = flask.Blueprint('portfolio', __name__, template_folder="views")

@portfolio.route('/portfolio', methods = ['GET'])
def getPortfolio():
	return flask.render_template("portfolio.html")