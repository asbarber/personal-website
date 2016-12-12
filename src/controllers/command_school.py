# -----------------------------------------------------------------------------
import flask
from flask import request
from config import db
from private import private_config
# -----------------------------------------------------------------------------


# Config
# -----------------------------------------------------------------------------
command_school = flask.Blueprint('command_school', __name__, template_folder='views')
# -----------------------------------------------------------------------------


# Request Routing
# -----------------------------------------------------------------------------
@command_school.route('/cs', methods = ['GET'])
def getCommandSchool():
	d = {
		'problem': 'Determine voter eligibility',
		'tests': 'Tests',
		'starterCode': '#include <iostream>\nusing namespace std;\n\nint main() {\n\n}'
	}

	return flask.render_template('command_school/home.html', **d)


@command_school.route('/cs/submitCode', methods = ['GET'])
def postSubmitCode():
	print request.args.get('code')

	d = {
		'compileStatus': False,
		'runResults': 'failed'
	};
	return flask.jsonify(**d)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def submitCode():
	return None

def compile():
	return None

def run():
	return None
# -----------------------------------------------------------------------------
