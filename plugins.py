import importlib.machinery, os, os.path, re, inspect

# will load modules with the name of the calling file
# calling file name: example.py
# will then load: example_one.py, example_two.py, etc
def simple_load():
	return [x['plugin'] for x in load_withnames(stackback = 2)]

def load_withnames(stackback = 1):
	# retrieve the file name of the calling module
	# note this has to match the number of calls back from host
	name = inspect.getmodule(inspect.stack()[stackback][0]).__file__;

	# the base name of this module
	basename = lambda x: os.path.splitext(os.path.split(x)[1])[0]
	basefile = basename(name)

	# the pattern to match for plugin files
	pattern = re.compile(basefile + '_.*\.py$')

	# retrieve the list of matching files
	files = [(x, os.path.join(os.path.dirname(os.path.realpath(name)), x)) for x in 
		os.listdir(os.path.dirname(os.path.realpath(name))) if pattern.match(x)]

	# load the files and send them back
	return [ {
		'name': basename(x[1])[len(basefile) + 1:],
		'plugin': importlib.machinery.SourceFileLoader('plugin_' + x[0], x[1]).load_module('plugin_' + x[0])
		} for x in files]

def load_bykeys():
	return { x['name']: x['plugin'] for x in load_withnames(stackback = 2) };