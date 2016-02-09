# run with py.test

import sys
import plugins

def test_simple_load():
	expected = ["I'm so happy bobby!", "Sad person bobby :("]
	msgs = [x.run('bobby') for x in plugins.simple_load()]
	print("msgs: %s" % msgs);
	assert(msgs == expected)

def test_load_bykeys():
	expected = {'happy': "I'm so happy bobby!", 'sad': "Sad person bobby :("}
	plugs = plugins.load_bykeys()
	msgs = {x: plugs[x].run('bobby') for x in plugs.keys()}
	print("msgs: %s" % msgs);
	assert(msgs == expected)

if __name__ == "__main__":
	mod = sys.modules[__name__]
	[getattr(mod, x)() for x in dir(mod) if x.startswith('test_')]