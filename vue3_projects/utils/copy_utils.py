from shutil import copyfile, copytree, rmtree

import os
import tempfile

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


class CopyTransaction:
    def __init__(self):
        self._backup_dir = tempfile.mkdtemp(prefix='copy_rollback_')
        self._snapshots = {}
        self._created_dirs = []

    def snapshot(self, path):
        normalized_path = os.path.normpath(path)
        if normalized_path in self._snapshots:
            return

        if os.path.exists(normalized_path):
            backup_name = str(len(self._snapshots))
            backup_path = os.path.join(self._backup_dir, backup_name)
            if os.path.isdir(normalized_path):
                copytree(normalized_path, backup_path)
                path_type = 'dir'
            else:
                backup_parent = os.path.dirname(backup_path)
                if backup_parent and not os.path.exists(backup_parent):
                    os.makedirs(backup_parent, exist_ok=True)
                copyfile(normalized_path, backup_path)
                path_type = 'file'
            self._snapshots[normalized_path] = {
                'exists': True,
                'type': path_type,
                'backup_path': backup_path
            }
            return

        self._snapshots[normalized_path] = {
            'exists': False,
            'type': None,
            'backup_path': None
        }

    def record_created_dir(self, path):
        normalized_path = os.path.normpath(path)
        if normalized_path not in self._created_dirs:
            self._created_dirs.append(normalized_path)

    def rollback(self):
        for path, snapshot in reversed(list(self._snapshots.items())):
            if os.path.isdir(path):
                rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)

            if not snapshot['exists']:
                continue

            parent_dir = os.path.dirname(path)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir, exist_ok=True)

            if snapshot['type'] == 'dir':
                copytree(snapshot['backup_path'], path)
            else:
                copyfile(snapshot['backup_path'], path)

        for created_dir in reversed(self._created_dirs):
            if os.path.isdir(created_dir) and not os.listdir(created_dir):
                os.rmdir(created_dir)

        if os.path.isdir(self._backup_dir):
            rmtree(self._backup_dir)

    def commit(self):
        if os.path.isdir(self._backup_dir):
            rmtree(self._backup_dir)


def do_copy(file_path, config, transaction=None):
    src = '{project_path}{file_path}'.format(
        project_path=config.origin_project_path, file_path=file_path).replace('{sign}', config.origin_package_path)
    dst = '{project_path}{file_path}'.format(
        project_path=config.target_project_path, file_path=file_path).replace('{sign}', config.target_package_path)
    if transaction is not None:
        transaction.snapshot(dst)
    if os.path.isdir(src):
        if os.path.isdir(dst):
            rmtree(dst)
        mkdir(dst, transaction=transaction)
        copytree(src, dst, dirs_exist_ok=True)
    else:
        dst_dir = os.path.dirname(dst)
        if dst_dir and not os.path.exists(dst_dir):
            os.makedirs(dst_dir, exist_ok=True)
            if transaction is not None:
                transaction.record_created_dir(dst_dir)
            print('文件夹 {} 创建成功！'.format(dst_dir))
        copyfile(src, dst)
    print('文件 {} 复制到 {} 成功！'.format(src, dst))


def mkdir(path, transaction=None):
    # 判断是否存在文件夹如果不存在则创建文件夹
    if not os.path.exists(path):
        print('文件 {} 不存在！'.format(path))
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            if transaction is not None:
                transaction.record_created_dir(dir_path)
            print('文件夹 {} 创建成功！'.format(dir_path))


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
