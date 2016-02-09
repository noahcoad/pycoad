import sys
import plugins

def test_load():
	expected = ["I'm so happy bobby!", "Sad person bobby :("]
	msgs = [x.run('bobby') for x in plugins.simple_load()]
	print(msgs);
	assert(msgs == expected)

if __name__ == "__main__":
	mod = sys.modules[__name__]
	[getattr(mod, x)() for x in dir(mod) if x.startswith('test_')]