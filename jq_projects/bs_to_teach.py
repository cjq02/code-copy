#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Created on 2021/07/12
@author: cjq
"""

from shutil import copyfile

ORIGIN_PROJECT_NAME = 'bookstore'
TARGET_PROJECT_NAME = 'teach'
ORIGIN_PACKAGE_SIGN = 'book'
TARGET_PACKAGE_SIGN = 'teach'
ORIGIN_PROJECT_PATH = 'D:/sizai/git/bookstore/{sign}-'.format(sign = ORIGIN_PROJECT_NAME)
TARGET_PROJECT_PATH = 'D:/sizai/git/teach-plat/{sign}-'.format(sign = TARGET_PROJECT_NAME)
ORIGIN_SYS_DIR = 'sys'
TARGET_SYS_DIR = 'sys'

FILE_PATH_LIST = [
    'api/src/main/java/com/jiujie/{sign}/application/annotation/EnumCodeInfo.java',
    'api/src/main/java/com/jiujie/{sign}/{sys}/service/ICodeService.java',
    'api/src/main/java/com/jiujie/{sign}/{sys}/vo/CodeVOExt.java',
    'api/src/main/java/com/jiujie/{sign}/common/vo/EnumVO.java',
    'api/src/main/java/com/jiujie/{sign}/{sys}/enumerate/CodeModifyStatusEnum.java',
    'service/src/main/resources/com/jiujie/{sign}/{sys}/sqlmapper/CodeMapper.xml',
    'service/src/main/java/com/jiujie/{sign}/{sys}/service/CodeService.java',
    'web/src/main/java/com/jiujie/{sign}/{sys}/web/CodeController.java',
    'web/src/main/java/com/jiujie/{sign}/utils/FreeMarkerUtils.java',
    'web/src/main/resources/static/template/code_js.ftl',
    'web/src/main/resources/static/template/code_json.ftl',
    'web/src/main/resources/static/template/enum_js.ftl',
    'web/src/main/resources/static/template/enum_class.ftl',
    'web/src/main/resources/static/assets/js/{sys}/codePage.js',
    'web/src/main/resources/static/assets/js/{sys}/codeForm.js',
    'web/src/main/resources/static/assets/js/{sys}/codeGroupPage.js',
    'web/src/main/resources/static/assets/js/{sys}/codeCompareForm.js',
    'web/src/main/resources/static/assets/js/{sys}/codeToEnumConfig.js',
    'web/src/main/resources/views/{sys}/codePage.jsp',
    'web/src/main/resources/views/{sys}/codeForm.jsp',
    'web/src/main/resources/views/{sys}/codeGroupPage.jsp',
    'web/src/main/resources/views/{sys}/codeCompareForm.jsp',
    'web/src/main/resources/views/{sys}/codeToEnumConfig.jsp',
    'web/src/main/resources/static/assets/js/application/base/common.base.js',
    'web/src/main/resources/static/assets/js/application/base/form.base.js',
    'web/src/main/resources/static/assets/js/application/base/page.base.js',
    'web/src/main/resources/views/application/_template_field.jsp'
]

def main():
    for file_path in FILE_PATH_LIST:
        do_copy(file_path)
        replace_package(file_path)
    

def do_copy(file_path):
    src = '{project_path}{file_path}'.format(project_path = ORIGIN_PROJECT_PATH, file_path = file_path).replace('{sign}', ORIGIN_PACKAGE_SIGN).replace('{sys}', ORIGIN_SYS_DIR)
    dst = '{project_path}{file_path}'.format(project_path = TARGET_PROJECT_PATH, file_path = file_path).replace('{sign}', TARGET_PACKAGE_SIGN).replace('{sys}', TARGET_SYS_DIR)
    copyfile(src, dst)
    print('文件 {} 复制到 {} 成功！'.format(src, dst))


def replace_package(file_path):
    if '{sign}' not in file_path:
        return
    file_path = '{project_path}{file_path}'.format(project_path = TARGET_PROJECT_PATH, file_path = file_path).replace('{sign}', TARGET_PACKAGE_SIGN).replace('{sys}', TARGET_SYS_DIR)
    #read input file
    fin = open(file_path, encoding='UTF-8')
    #read file contents to string
    data = fin.read()
    print(data)
    #replace all occurrences of the required string
    data = data.replace('com.jiujie.{}'.format(ORIGIN_PACKAGE_SIGN), 'com.jiujie.{}'.format(TARGET_PACKAGE_SIGN))
    data = data.replace('com.jiujie.{package_sign}.{sys}'.format(package_sign = TARGET_PACKAGE_SIGN, sys = ORIGIN_SYS_DIR), 'com.jiujie.{package_sign}.{sys}'.format(package_sign = TARGET_PACKAGE_SIGN, sys = TARGET_SYS_DIR))
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_path, "w", encoding='UTF-8')
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()



if __name__ == '__main__':
    main()
