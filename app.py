from flask import Flask
from config import prod_config, dev_config
import sys
import src.controllers as controllers


# Start application
# -----------------------------------------------------------------------------
is_dev_run = __name__ == "__main__"
config = dev_config if is_dev_run else prod_config
app = Flask(__name__, template_folder=config["template_folder"])

blueprints = [controllers.home, controllers.passions, controllers.portfolio]
for blueprint in blueprints:
	app.register_blueprint(blueprint)
# -----------------------------------------------------------------------------


# __main__
# -----------------------------------------------------------------------------
if is_dev_run:
	app.run(host=config['host'], port=config['port'], debug=config['debug'])
# -----------------------------------------------------------------------------

# TODO
# home.html - fix links to AVE and Course Scheduler
# home.html - GSI
# home.html - read content and update
