from shutil import copyfile, copytree, rmtree

import os

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

def do_copy(file_path, config):
    src = '{project_path}{file_path}'.format(
        project_path=config.origin_project_path, file_path=file_path).replace('{sign}', config.origin_package_path)
    dst = '{project_path}{file_path}'.format(
        project_path=config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_path)
    if os.path.isdir(src):
        if os.path.isdir(dst):
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
    suffixes = ('.js', '.jsx', '.ts', '.vue', '.java', '.xml')
    backend_suffixes = ('.java', '.xml')
    if file_path.endswith(suffixes) == False:
        print('不符合替换规则的文件：{}'.format(file_path))
        return
    
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    # replace all occurrences of the required string
    origin_package_name = 'com.jiujie.{}'.format(config.origin_package_sign)
    target_package_name = 'com.jiujie.{}'.format(config.target_package_sign)
    content = content.replace(origin_package_name.encode(), target_package_name.encode())
    if file_path.endswith(backend_suffixes) == False:
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    print('{} 文件内容关键词替换成功 -- {} to {}'.format(file_path, origin_package_name, target_package_name))
    # open the input file in write mode
    fin = open(file_path, "wb")
    # overrite the input file with the resulting data
    fin.write(content)
    # close the file
    fin.close()

def do_replace(file_path, config):
    dst = '{project_path}{file_path}'.format(
        project_path = config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_path)
    if os.path.isdir(dst):
        for dirpath, dirnames, filenames in os.walk(dst):
            for filename in filenames:
                replace_keyword(os.path.join(dirpath, filename), config)
    else:
        replace_keyword(dst, config)
