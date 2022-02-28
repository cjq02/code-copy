#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Created on 2021/07/12
@author: cjq
"""

from shutil import copyfile

ORIGIN_PACKAGE_SIGN = 'bigdata'
TARGET_PACKAGE_SIGN = 'behavior'
ORIGIN_PROJECT_PATH = 'D:/sizai/git/policy-big-data/{sign}-'.format(sign = ORIGIN_PACKAGE_SIGN)
TARGET_PROJECT_PATH = 'D:/sizai/git/behavior/{sign}-'.format(sign = TARGET_PACKAGE_SIGN)

FILE_PATH_LIST = [
    'api/src/main/java/com/jiujie/{sign}/sys/service/ICodeService.java',
    'api/src/main/java/com/jiujie/{sign}/sys/vo/CodeVOExt.java',
    'api/src/main/java/com/jiujie/{sign}/application/vo/EnumVO.java',
    'api/src/main/java/com/jiujie/{sign}/sys/enumerate/CodeModifyStatusEnum.java',
    'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/CodeMapper.xml',
    'service/src/main/java/com/jiujie/{sign}/sys/service/CodeService.java',
    'web/src/main/java/com/jiujie/{sign}/sys/web/CodeController.java',
    'web/src/main/resources/static/template/code_js.ftl',
    'web/src/main/resources/static/template/code_json.ftl',
    'web/src/main/resources/static/template/enum_js.ftl',
    'web/src/main/resources/static/template/enum_class.ftl',
    'vue/src/views/sys/code/codePage.js',
    'vue/src/views/sys/code/index.vue',
    'vue/src/views/sys/code/components/CodeForm/codeForm.js',
    'vue/src/views/sys/code/components/CodeForm/index.vue',
    'vue/src/views/sys/code/components/CompareForm/compareForm.js',
    'vue/src/views/sys/code/components/CompareForm/index.vue',
    'vue/src/views/sys/code/components/GenerateEnumDialog/index.vue',
    'vue/src/views/sys/code/components/ButtonEnumPackage/index.vue',
    'vue/src/views/sys/code/components/ButtonEnumPackage/index.scss',
]

def main():
    for file_path in FILE_PATH_LIST:
        do_copy(file_path)
        replace_package(file_path)
    

def do_copy(file_path):
    src = '{project_path}{file_path}'.format(project_path = ORIGIN_PROJECT_PATH, file_path = file_path).replace('{sign}', ORIGIN_PACKAGE_SIGN)
    dst = '{project_path}{file_path}'.format(project_path = TARGET_PROJECT_PATH, file_path = file_path).replace('{sign}', TARGET_PACKAGE_SIGN)
    copyfile(src, dst)
    print('文件 {} 复制到 {} 成功！'.format(src, dst))


def replace_package(file_path):
    if '{sign}' not in file_path:
        return
    file_path = '{project_path}{file_path}'.format(project_path = TARGET_PROJECT_PATH, file_path = file_path).replace('{sign}', TARGET_PACKAGE_SIGN)
    #read input file
    fin = open(file_path, encoding='UTF-8')
    #read file contents to string
    data = fin.read()
    print(data)
    #replace all occurrences of the required string
    data = data.replace('com.jiujie.{}'.format(ORIGIN_PACKAGE_SIGN), 'com.jiujie.{}'.format(TARGET_PACKAGE_SIGN))
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
