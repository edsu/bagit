import bagit

from shutil import copytree, rmtree
from os.path import dirname, isdir, join

BASE_DIR = dirname(__file__)
TEST_DATA = join(BASE_DIR, "data")
TEMP_DATA = join(BASE_DIR, "temp")

# avoid changing bag-info.txt fixities
bagit.VERSION = "1.5.4"

def setup_module():
    if isdir(TEMP_DATA):
        rmtree(TEMP_DATA)
    copytree(TEST_DATA, TEMP_DATA)

def teardown_module():
    if isdir(TEMP_DATA):
        rmtree(TEMP_DATA)

def slurp_text_file(filename):
    with open(filename) as f:
        return f.read()