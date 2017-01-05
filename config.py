prod_config = {
	"template_folder": "/var/www/app/src/views"
}

dev_config = {
	"template_folder": "src/views",
	"host": "0.0.0.0",
	"debug": True,
	"port": 3000	
}

config = None

db = {
	'engr101': {
		'url': '#'
	}
}

app_config = {
	'command_school': {
		'db_update' : False,
		'db_fname' : 'db/apps/command_school/programs.p',
		'db_problems_path' : 'db/apps/command_school/',
		'db_problems' : [
			'1-1-voter-eligibility',
			'1-2-basic-calculator',
			'1-3-temperature-converter',
			'1-4-circle-math',
			'1-5-shortest-program',
			'1-6-cylinder-volume',
			'1-7-dice-roll-simulator'
		]
	}
}
