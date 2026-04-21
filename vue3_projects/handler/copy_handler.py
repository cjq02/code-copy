#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Created on 2021/07/12
@author: cjq
"""

from data.file_list import get_file_path_list
from utils.copy_utils import CopyTransaction, do_copy, do_replace

class Config:
    def __init__(self):
        self.target_project_path = ''
        self.origin_project_path = ''
        self.target_package_sign = ''
        self.origin_package_sign = ''
        self.target_package_path = ''
        self.origin_package_path = ''

def execute(config):
    transaction = CopyTransaction()
    try:
        for file_path in get_file_path_list():
            do_copy(file_path, config, transaction=transaction)
            do_replace(file_path, config)
    except Exception:
        transaction.rollback()
        print('生成出现异常，已还原已修改的文件。')
        raise
    else:
        transaction.commit()
