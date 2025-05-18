import os
import importlib.util

class Editor:
    def __init__(self):
        self.plugins = {}
        self.text = ""
        self.load_plugins()

    def load_plugins(self, plugins_dir="plugins"):
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]
                file_path = os.path.join(plugins_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for item in dir(module):
                    obj = getattr(module, item)
                    if isinstance(obj, type):
                        # Only register subclasses of PluginBase (but not PluginBase itself)
                        try:
                            from plugin_base import PluginBase
                            if issubclass(obj, PluginBase) and obj is not PluginBase:
                                plugin_instance = obj(self)
                                self.plugins[plugin_instance.name] = plugin_instance
                        except Exception as e:
                            print(f"Error loading plugin {filename}: {e}")

    def run_plugin(self, plugin_name):
        plugin = self.plugins.get(plugin_name)
        if plugin:
            plugin.run()
        else:
            print(f"No plugin found with name: {plugin_name}")

if __name__ == "__main__":
    editor = Editor()
    print("Available plugins:", list(editor.plugins.keys()))
    # Example usage: run the "hello" plugin
    editor.run_plugin("hello")