import shutil

def copy_file(src, dst_list):
    try:
        # 遍历目标路径列表
        for dst in dst_list:
            # 使用 shutil.copy() 函数复制文件
            shutil.copy(src, dst)
            print(f"文件已成功从 {src} 复制到 {dst}")
    except FileNotFoundError:
        print(f"源文件 {src} 不存在")
    except PermissionError:
        print(f"没有权限复制文件到某些目标路径")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")

source_project = "D:\sizai\git\mlh-base\mlh-base-vue"

destination_projects = [
    "D:\sizai\git\wms\wms-vue",
    "D:\sizai\git\mlh-sale\mlh-sale-vue",
    "D:\sizai\git\mlh-sale\mlh-sale-shop-vue",
    "D:\sizai\git\mlh-purchase\mlh-purchase-vue",
    "D:\sizai\git\mlh-production\mlh-production-vue",
    "D:\sizai\git\supplychain\supplychain-vue",
]

file_paths = [
    "src\layout\components\SystemSwitch\SystemSwitch.vue"
]

for destination_project in destination_projects:
    destination_files = []
    for file_path in file_paths:
        destination_files.append(destination_project + "\\" + file_path)
        source_file = source_project + "\\" + file_path
        copy_file(source_file, destination_files)

