
def init(config):
    config.origin_package_sign = 'official'
    config.target_package_sign = 'demo'
    config.origin_project_path = 'D:/sizai/git/{sign}/{sign}-'.format(sign = config.origin_package_sign)
    config.target_project_path = 'D:/sizai/git/{sign}-vue/{sign}-'.format(sign = config.target_package_sign)
    return config
