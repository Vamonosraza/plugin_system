class PluginBase:
    name = "base"

    def __init__(self, editor):
        self.editor = editor

    def run(self):
        raise NotImplementedError("Plugin must implement the run() method.")