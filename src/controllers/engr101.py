import flask
from flask import request
from config import db
from private import private_config

engr101 = flask.Blueprint('engr101', __name__, template_folder="views")

@engr101.route('/engr101', methods = ['GET'])
def getEngr101():
	url = db.get('engr101').get('url')
	return flask.render_template("engr101/engr101.html", url=url)


@engr101.route('/engr101/admin', methods = ['GET'])
def getEngr101Admin():
	return flask.render_template("engr101/admin.html")	

@engr101.route('/engr101/admin', methods = ['POST'])
def postEngr101Admin():
	username = request.form.get('username')
	password = request.form.get('password')
	url = request.form.get('url')

	# Authenticate and update DB
	isAuthenticated = username == private_config.get('engr101').get('admin_username') and \
					  password == private_config.get('engr101').get('admin_password')
	print username, password, url, isAuthenticated					  
	if isAuthenticated:
		db['engr101']['url'] = url

	return getEngr101Admin()

@engr101.route('/engr101/review', methods= ['GET'])
def getEngr101Review():
	return flask.render_template("engr101/review.html")

