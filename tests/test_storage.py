from bagit.storage import FileSystemStorage
from utils import setup_module, teardown_module, TEMP_DATA

def test_exists():
    storage = FileSystemStorage(TEMP_DATA)
    assert storage.exists("README") == True
    assert storage.exists("README2") == False

def test_open():
    storage = FileSystemStorage(TEMP_DATA)
    f = storage.open("README")
    assert f.read(13) == "public domain"

def test_listdir():
    storage = FileSystemStorage(TEMP_DATA)
    dirs, files = storage.listdir()
    assert dirs == ['si', 'loc']
