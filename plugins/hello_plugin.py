
from plugin_base import PluginBase

class HelloPlugin(PluginBase):
    name = "hello"

    def run(self):
        print("Hello from the HelloPlugin!")