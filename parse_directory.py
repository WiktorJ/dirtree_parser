import os


def is_ignored(dir, ignore_directories, replacement):
    for ignore_dir in ignore_directories:
        if dir.startswith(replacement + ignore_dir):
            return True
    return False


def parse(dir, ignore_directories=None, replacement=""):
    if not dir.endswith('/'):
        dir += '/'
    if not replacement.endswith('/'):
        replacement += '/'
    if ignore_directories is None:
        ignore_directories = []
    print('\dirtree{%')
    for root, dirs, files in os.walk(dir):
        root = root.replace(dir, replacement)
        if not is_ignored(root, ignore_directories, replacement):
            dir_list = list(filter(lambda x: len(x) != 0, root.split('/')))
            dir_depth = len(dir_list)
            dir_to_write = (dir_list[len(dir_list) - 1] + '.').replace('_', "\_")
            print('.' + str(dir_depth), dir_to_write)
            for file in files:
                file_to_write = (file + '.').replace('_', '\-')
                print('.' + str(dir_depth + 1), file_to_write)
    print('}')


parse("/home/wiktor/Studies/Inż/accsoft-web-components-tvc", ignore_directories=['.git', '.idea'],
      replacement='tvc-client')
