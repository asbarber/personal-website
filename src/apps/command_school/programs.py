import subprocess
import os
import json
import pickle
from config import app_config


# -----------------------------------------------------------------------------
class Shell():
	@staticmethod
	def results_call(args):
		p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		std_out, std_err = p.communicate()
		return p.returncode, std_out, std_err

	@staticmethod
	def compile(in_fname, out_fname):
		return Shell.results_call(
				[
					'g++',
					in_fname,
					'-o',
					out_fname
				]
		)

	@staticmethod
	def execute(compiled_fname):
		return Shell.results_call([
			os.path.join('./', compiled_fname)
		])
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
class Compiler():
	@staticmethod
	def compile(in_fname, out_fname):
		return Shell.compile(in_fname, out_fname)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
class Executor():
	@staticmethod
	def execute(compiled_fname):
		return Shell.execute(compiled_fname)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
class Instruction():
	def __init__(self, id, text):
		self.id = id
		self.text = text

class SampleCase():
	def __init__(self, id, text):
		self.id = id
		self.text = text

class TestCase():
	def __init__(self, id, input, exp_stdout, exp_stderr):
		self.id = id
		self.input = input
		self.exp_stdout = exp_stdout
		self.exp_stderr = exp_stderr

class StarterCode():
	def __init__(self, id, code):
		self.id = id
		self.code = code

class Solution():
	def __init__(self, id, code):
		self.id = id
		self.code = code

class Problem():
	def __init__(self, id, title, skills, icon, instructionId, sampleIds, testIds, starterCodeId, solutionId):
		self.id = id
		self.title = title
		self.skills = skills
		self.icon = icon
		self.instructionId = instructionId
		self.sampleIds = sampleIds
		self.testIds = testIds
		self.starterCodeId = starterCodeId
		self.solutionId = solutionId

class ProblemDB():
	def __init__(self, dbFname):
		with open(dbFname, 'rb') as dbFile:
			self.db = pickle.load(dbFile)

	def getObject(self, category, id):
		return self.db[category][id]

	def getProblem(self, problemId):
		return self.getObject('problems', problemId)

	def getSequentialProblemId(self, problemId, isForward):
		# Assumes problemId is a valid problem id
		currIndex = self.db['orderedProblemIds'].index(problemId)
		nextIndex = currIndex + 1 if isForward else currIndex - 1

		# Check in-bounds
		if nextIndex >= len(self.db['orderedProblemIds']) or nextIndex < 0:
			return None

		# Next id
		return self.db['orderedProblemIds'][nextIndex]

	def getNextProblemId(self, problemId):
		return self.getSequentialProblemId(problemId, isForward=True)

	def getPrevProblemId(self, problemId):
		return self.getSequentialProblemId(problemId, isForward=False)

	def getInstruction(self, instructionId):
		return self.getObject('instructions', instructionId)

	def getSampleCase(self, sampleId):
		return self.getObject('samples', sampleId)

	def getTestCase(self, testId):
		return self.getObject('tests', testId)

	def getStarterCode(self, starterCodeId):
		return self.getObject('starterCodes', starterCodeId)

	def getSolution(self, solutionId):
		return self.getObject('solutions', solutionId)
		
	def getProblems(self):
		return [self.getProblem(id) for id in self.db['problems'].keys()]

	def getOrderedProblems(self):
		return [self.getProblem(problemId) for problemId in self.db['orderedProblemIds']]
		
	def getProblemIdsAndTitles(self):
		return [(id, self.getProblem(id).title) for id in self.db['problems'].keys()]


	@staticmethod
	def createDB(dbFname, problemsPath, problems):
		all_problems = {}
		all_instructions = {}
		all_starters = {}
		all_samples = {}
		all_solutions = {}

		for problemId in problems:
			problemPath = problemsPath + problemId
			problemData = json.loads(open(problemPath + '/meta.json', 'r').read())

			# Instruction
			instrId = 'instruction-' + problemId
			instrText = open(problemPath + '/instruction.txt', 'r').read()
			instruction = Instruction(instrId, instrText)
			problemData['instructionId'] = instrId
			all_instructions[instrId] = instruction

			# Starter Code
			starterId = 'starter-' + problemId
			starterCode = open(problemPath + '/starter.cpp', 'r').read()
			starter = StarterCode(starterId, starterCode)
			problemData['starterCodeId'] = starterId
			all_starters[starterId] = starter

			# Solution
			solutionId = 'solution-' + problemId
			solutionCode = open(problemPath + '/solution.cpp', 'r').read()
			solution = Solution(solutionId, solutionCode)
			problemData['solutionId'] = solutionId
			all_solutions[solutionId] = solution

			# Sample Test Cases
			problemData['sampleIds'] = []
			for sampleFname in os.listdir(problemPath + '/samples'):
				sampleFname = os.path.join(problemPath + '/samples', sampleFname)
				sampleId = os.path.basename(sampleFname) + problemId
				sampleText = open(sampleFname, 'r').read()
				sample = SampleCase(sampleId, sampleText)
				problemData['sampleIds'].append(sampleId)
				all_samples[sampleId] = sample

			# Test Cases
			problemData['testIds'] = []

			# Problem
			problem = Problem(problemId, **problemData)
			all_problems[problemId] = problem

		all_orderings = sorted(all_problems.keys())
		all = {
			'orderedProblemIds' : all_orderings,
			'problems' : all_problems,
			'instructions' : all_instructions,
			'starterCodes' : all_starters,
			'samples' : all_samples,
			'solutions' : all_solutions
		}

		pickle.dump(all, open(dbFname, 'wb'))	
# -----------------------------------------------------------------------------


# SINGLETON
# -----------------------------------------------------------------------------
config = app_config['command_school']
if config['db_update'] or not os.path.exists(config['db_fname']):
	ProblemDB.createDB(config['db_fname'], config['db_problems_path'], config['db_problems'])
PROBLEM_DB = ProblemDB(config['db_fname'])
# -----------------------------------------------------------------------------

