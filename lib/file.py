from os.path import dirname, join, exists

MAIN_DIRECTORY = dirname(dirname(__file__))


def get_full_path(*path):
    full_path = join(MAIN_DIRECTORY, *path)
    if exists(full_path):
        return full_path
    else:
        raise Exception(f'Path not found: {full_path}')
