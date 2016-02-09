# import coad.pathext; list(coad.pathext.files('~/Dropbox/code', subdir = True))
# file:///Users/noahcoad/stream/pydocs/python-3.3.2-docs-html/library/os.html#module-os
# path = '/System/Library/OpenSSL'; list(os.walk(path))

import os, os.path, re, itertools

walker = lambda path, i: itertools.chain.from_iterable([[os.path.join(x[0], b) for b in x[i]] for x in os.walk(path)])

def files(folder = '.', pattern = None, subdir = False):
	return search(2, folder, pattern, subdir)

def dirs(folder = '.', pattern = None, subdir = False):
	return search(1, folder, pattern, subdir)

def search(filedir, folder = '.', pattern = None, subdir = False):
	if isinstance(folder, str): folder = [folder];
	typecheck = lambda x: os.path.isdir(x) if filedir == 1 else lambda x: os.path.isfile(x)
	folder = [os.path.expanduser(os.path.expandvars(x)) for x in folder]
	if pattern: comp = re.compile(pattern);
	full = True
	if subdir:
		resultes = os.walk(path)
		# results = list(itertools.chain.from_iterable([walker(x, filedir) for x in filedir]))
	else:
		rawlist = os.listdir(path)
		results = [(path, [x for x in rawlist if os.path.isdir(x)], [x for x in rawlist if os.path.isfile(x)])]
		# results = list(itertools.chain.from_iterable([[os.path.join(f, x) if full else x for x in os.listdir(f) if typecheck(os.path.join(f, x)) and (not(pattern) or comp.search(x))] for f in folder]))
	return 

def noext(path):
	return os.path.splitext(os.path.split(path)[1])[0];