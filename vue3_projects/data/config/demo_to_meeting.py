
def init(config):
    config.origin_project_name = 'demo'
    config.target_project_name = 'meeting'
    config.origin_package_sign = 'demo'
    config.target_package_sign = 'meeting'
    config.origin_project_path = 'D:/sizai/git/{sign}-vue/{sign}-'.format(sign = config.origin_package_sign)
    config.target_project_path = 'D:/sizai/git/{sign}/{sign}-'.format(sign = config.target_package_sign)
    return config
