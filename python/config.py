import yaml

DEFAULT_PATH = "../resources/"
CONFIG_FILE = "config.yml"


class Config:

    def __init__(self):
        with open(DEFAULT_PATH + CONFIG_FILE, 'r') as file:
            self.conf = yaml.safe_load(file)

    def config(self, path: str) -> str:
        path_list = path.split('.')
        depth = self.conf[path_list.pop(0)]
        for p in path_list:
            depth = depth[p]
        return depth
