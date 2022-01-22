from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
skills = dict()

def add_skill(pattern):
    def wrapper(func):
        skills[pattern] = func
        return func
    return wrapper

__all__ = [
    basename(f)[:-3]
    for f in modules
    if isfile(f) and not f.endswith('__init__.py')
]