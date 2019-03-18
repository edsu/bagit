import os
import bagit

from utils import setup_module, teardown_module, TEMP_DATA

def test_ok():
    assert bagit.VERSION == "1.5.4"

def test_create_dir():
    assert os.path.isdir(TEMP_DATA)
