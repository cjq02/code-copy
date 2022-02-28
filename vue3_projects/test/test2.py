import importlib
import sys
sys.path.append("..")

module_name = 'data.config.{}'.format(sys.argv[1])
config = importlib.import_module(module_name)

print('config {}'.format(config.main().target_project_path))