from flask import Flask
import json
import getopt
import sys
import src.controllers as controllers

# Command line arguments
# -----------------------------------------------------------------------------
def print_usage():
	print 'app.py -c <configfile>'

def main(argv):
	try:
		argv = sys.argv[1:]
		opts, args = getopt.getopt(argv, "hc:", ["configfile="])
	except getopt.GetoptError:
		print_usage()
		sys.exit(2)

	configfile = None
	for opt, arg in opts:
		if opt == '-h':
			print_usage()
			sys.exit()
		elif opt in ("-c", "--configfile"):
			configfile = arg

	if configfile == None:
		print_usage()
		sys.exit(2)

	with open(configfile) as data_file:
		config = json.load(data_file)

	run(config)
# -----------------------------------------------------------------------------


# Start application
# -----------------------------------------------------------------------------
def run(config):
	app = Flask(__name__, template_folder=config["template_folder"])

	blueprints = [controllers.home]
	for blueprint in blueprints:
		app.register_blueprint(blueprint)

	app.run(host=config['host'], port=config['port'], debug=config['debug'])
# -----------------------------------------------------------------------------


# __main__
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	main(sys.argv[1:])
# -----------------------------------------------------------------------------
