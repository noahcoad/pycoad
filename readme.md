Misc handy python utilities

run tests with py.test

# plugins
A very simple plugin loader

Uses the calling file and an underscore to locate plugins. <br>
hello.py will load hello\_world.py and hello\_scooby.py.

loader

    # file: hello.py
    import pycoad
    
    plugins = pycoad.plugins.simple_load()
    print([x.run("Bobby") for plugins])

first plugin

    # file: feeling_happy.py
    def run(name):
      return "Feeling alive today %s!" % name

second plugin

    # file: feeling_sad.py
    def run(name):
    	return "%s is feeling down =(" % name

