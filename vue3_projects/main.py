#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 命令：python .\main.py origin target   

"""

Created on 2022/01/26
@author: cjq

"""

import importlib
import sys
import handler.copy_handler as copy_handler
from handler.copy_handler import Config

def main():
    origin = importlib.import_module('data.config.{}'.format(sys.argv[1]))
    target = importlib.import_module('data.config.{}'.format(sys.argv[2]))

    config = Config()
    config.origin_package_sign = origin.PACKAGE_SIGN
    config.target_package_sign = target.PACKAGE_SIGN
    config.origin_package_path = getattr(origin, 'PACKAGE_PATH', origin.PACKAGE_SIGN)
    config.target_package_path = getattr(target, 'PACKAGE_PATH', target.PACKAGE_SIGN)
    config.origin_project_path = origin.PROJECT_PATH
    config.target_project_path = target.PROJECT_PATH

    copy_handler.execute(config)


if __name__ == '__main__':
    main()
