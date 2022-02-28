from shutil import copyfile

import os


def do_copy(file_path, config):
    src = '{project_path}{file_path}'.format(
        project_path=config.origin_project_path, file_path=file_path).replace('{sign}', config.origin_package_sign)
    dst = '{project_path}{file_path}'.format(
        project_path=config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_sign)
    mkdir(dst)
    copyfile(src, dst)
    print('文件 {} 复制到 {} 成功！'.format(src, dst))


def mkdir(path):
    # 判断是否存在文件夹如果不存在则创建文件夹
    if not os.path.exists(path):
        print('文件 {} 不存在！'.format(path))
        dir = path[0:path.rindex('/')]
        # makedirs 创建文件时如果路径不存在会创建这个路径
        if not os.path.exists(dir):
            os.makedirs(dir)
            print('文件夹 {} 创建成功！'.format(dir))


def replace_package(file_path, config):
    if '{sign}' not in file_path and file_path.endswith('.xml') == False:
        return
    file_path = '{project_path}{file_path}'.format(
        project_path=config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_sign)
    # read input file
    fin = open(file_path, encoding='UTF-8')
    # read file contents to string
    data = fin.read()
    print('{} 文件内容包名替换成功！'.format(file_path))
    # replace all occurrences of the required string
    data = data.replace('com.jiujie.{}'.format(
        config.origin_package_sign), 'com.jiujie.{}'.format(config.target_package_sign))
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open(file_path, "w", encoding='UTF-8')
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()
