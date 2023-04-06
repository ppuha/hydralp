import yaml

def get_config(path):
  with open(path) as f:
    return yaml.safe_load(f.read())
