#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Created on 2022/01/26
@author: cjq

"""

import importlib
import sys
import handler.copy_handler as copy_handler
from handler.copy_handler import Config

def main():
    module_name = 'data.config.{}'.format(sys.argv[1])
    config = importlib.import_module(module_name).init(Config)
    copy_handler.execute(config)


if __name__ == '__main__':
    main()
