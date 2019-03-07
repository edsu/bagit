import bagit

from utils import setup_module, teardown_module

def test_ok():
    assert bagit.VERSION == "1.5.4"
