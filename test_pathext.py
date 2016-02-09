# run with py.test

import sys
import pathext

# path = '/System/Library/OpenSSL'

# def test_files():
# 	cases = ((None, False, ['/System/Library/OpenSSL/openssl.cnf']), 
# 		("\.cnf$", False, ['/System/Library/OpenSSL/openssl.cnf']),
# 		(None, False, ['openssl.cnf']),
# 		("\.exe$", False, []))
# 	for idx, case in enumerate(cases):
# 		actual = pathext.files(path, case[0], case[1])
# 		print("expect: %s\nactual: %s\n" % (case[2], actual))
# 		assert(actual == case[2])

# def test_dirs():
# 	dirs = pathext.dirs(path)
# 	expected = ['/System/Library/OpenSSL/certs', '/System/Library/OpenSSL/misc', '/System/Library/OpenSSL/private']
# 	print(dirs)
# 	assert(dirs == expected)

def test_noext():
	cases = (('test.py', 'test'), ('/vol/test.pt', 'test'))
	for case in cases:
		actual = pathext.noext(case[0])
		print("input:  %s\nexpect: %s\nactual: %s\n" % (case[0], case[1], actual))
		assert(actual == case[1])

if __name__ == "__main__":
	mod = sys.modules[__name__]
	[getattr(mod, x)() for x in dir(mod) if x.startswith('test_')]