#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Created on 2021/10/12
@author: cjq

"""

import handler.copy_handler as copy_handler
from handler.copy_handler import Config

def main():
    config = Config()
    config.origin_package_sign = 'behavior'
    config.target_package_sign = 'integration'
    config.origin_project_path = 'D:/sizai/git/{sign}/{sign}-'.format(sign = config.origin_package_sign)
    config.target_project_path = 'D:/sizai/git/{sign}/{sign}-'.format(sign = config.target_package_sign)

    copy_handler.handle(config)


if __name__ == '__main__':
    main()
