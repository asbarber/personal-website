# -----------------------------------------------------------------------------
class User():
	def __init__(self, username, problemsCompleted=[]):
		self.username = username
		self.problemsCompleted = problemsCompleted

	def hasCompleted(self, problemId):
		return problemId in self.problemsCompleted

	def markCompleted(self, problemId):
		if not problemId in self.problemsCompleted:
			self.problemsCompleted.append(problemId)
# -----------------------------------------------------------------------------