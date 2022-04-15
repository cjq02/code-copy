from shutil import copyfile, copytree, rmtree

import os


def do_copy(file_path, config):
    src = '{project_path}{file_path}'.format(
        project_path=config.origin_project_path, file_path=file_path).replace('{sign}', config.origin_package_sign)
    dst = '{project_path}{file_path}'.format(
        project_path=config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_sign)
    if os.path.isdir(src):
        rmtree(dst)
        mkdir(dst)
        copytree(src, dst,  dirs_exist_ok=True)
    else:
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


def replace_keyword(file_path, config):
    # if '{sign}' not in file_path and file_path.endswith('.xml') == False:
    #     return
    suffixes = ('.js', '.ts', '.vue', '.java', '.xml')
    if file_path.endswith(suffixes) == False:
        print('不符合替换规则的文件：{}'.format(file_path))
        return
    
    # read input file
    fin = open(file_path, encoding='UTF-8')
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    origin_package_name = 'com.jiujie.{}'.format(config.origin_package_sign)
    target_package_name = 'com.jiujie.{}'.format(config.target_package_sign)
    data = data.replace(origin_package_name, target_package_name)
    print('{} 文件内容关键词替换成功 -- {} to {}'.format(file_path, origin_package_name, target_package_name))
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open(file_path, "w", encoding='UTF-8')
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()

def do_replace(file_path, config):
    dst = '{project_path}{file_path}'.format(
        project_path = config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_sign)
    if os.path.isdir(dst):
        for dirpath, dirnames, filenames in os.walk(dst):
            for filename in filenames:
                replace_keyword(os.path.join(dirpath, filename), config)
    else:
        replace_keyword(dst, config)
