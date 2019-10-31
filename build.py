from pybuilder.core import use_plugin
from pybuilder.core import init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = "publish"

# Project version
with open("version.txt") as version_file:
	version = version_file.read().strip()

@init
def initialize(project, logger):	
	# Do not break build even though coverage is not passed
	project.set_property('coverage_break_build', False)
