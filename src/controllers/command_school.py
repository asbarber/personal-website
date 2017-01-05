# -----------------------------------------------------------------------------
import flask
from flask import request

from private import private_config
from src.apps.command_school import programs
from src.apps.command_school import users
from src.apps.command_school.programs import PROBLEM_DB as db
# -----------------------------------------------------------------------------


# Config
# -----------------------------------------------------------------------------
command_school = flask.Blueprint('command_school', __name__, template_folder='views')
# -----------------------------------------------------------------------------


# All Problems
# -----------------------------------------------------------------------------
@command_school.route('/cs/problems', methods = ['GET'])
def getAllProblems():
	problems = db.getOrderedProblems()
	user = users.User('asbarber', [])

	return flask.render_template('command_school/problems.html', problems=problems, user=user)
# -----------------------------------------------------------------------------


# Individual Problem
# -----------------------------------------------------------------------------
@command_school.route('/cs/problem', methods = ['GET'])
def getProblem():
	problemId = request.args.get('id')
	problem = db.getProblem(problemId)
	d = {
		'problem' : problem,
		'instruction': db.getInstruction(problem.instructionId).text,
		'samples': [db.getSampleCase(sampleId).text for sampleId in problem.sampleIds],
		'starterCode': db.getStarterCode(problem.starterCodeId).code,
		'solution': db.getSolution(problem.solutionId).code
	}
	print d
	return flask.render_template('command_school/problem.html', **d)


def getSequentialProblem(currProblemId, isForward):
	if isForward:
		newProblemId = db.getNextProblemId(currProblemId)
	else:
		newProblemId = db.getPrevProblemId(currProblemId)

	if not newProblemId:
		return flask.redirect(flask.url_for('.getAllProblems'))
	
	return flask.redirect(flask.url_for('.getProblem', id=newProblemId))


@command_school.route('/cs/problem/next', methods = ['GET'])
def getNextProblem():
	return getSequentialProblem(request.args.get('id'), isForward=True)


@command_school.route('/cs/problem/prev', methods = ['GET'])
def getPrevProblem():
	return getSequentialProblem(request.args.get('id'), isForward=False)


@command_school.route('/cs/submitCode', methods = ['GET'])
def postSubmitCode():
	sourceCode = request.args.get('code')

	with open('tmp.cpp', 'w') as cpp_file:
		cpp_file.write(sourceCode)

	# compileResults = programs.Compiler.compile('tmp.cpp', 'tmp.out')
	# runResults = programs.Executor.execute('tmp.out')

	# d = {
	# 	'compileResults': compileResults[2],
	# 	'executeResults': runResults[1]
	# }

	print d
	return flask.jsonify(**d)
# -----------------------------------------------------------------------------

