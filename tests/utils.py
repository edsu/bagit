import bagit

from shutil import copytree, rmtree
from os.path import dirname, isdir, join

base_dir = dirname(__file__)
test_data = join(base_dir, "data")
test_temp = join(base_dir, "temp")

# avoid changing bag-info.txt fixities
bagit.VERSION = "1.5.4"

def setup_module():
    if isdir(test_temp):
        rmtree(test_temp)
    copytree(test_data, test_temp)

def teardown_module():
    if isdir(test_temp):
        pass #rmtree(test_temp)

def slurp_text_file(filename):
    with open(filename) as f:
        return f.read()