import hashlib

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
    assert files == ['README']

def test_listdir_subdir():
    storage = FileSystemStorage(TEMP_DATA)
    dirs, files = storage.listdir("loc")
    assert dirs == []
    assert files == [
        '2478433644_2839c5e8b8_o_d.jpg',
        '3314493806_6f1db86d66_o_d.jpg'
    ]

def test_md5():
    storage = FileSystemStorage(TEMP_DATA)
    assert storage.md5('loc/2478433644_2839c5e8b8_o_d.jpg') == '9a2b89e9940fea6ac3a0cc71b0a933a0'

def test_hexdigest():
    storage = FileSystemStorage(TEMP_DATA)
    h = storage.hexdigest('loc/2478433644_2839c5e8b8_o_d.jpg', [hashlib.md5, hashlib.sha256])
    assert h[0] == '9a2b89e9940fea6ac3a0cc71b0a933a0'
    assert h[1] == 'b6df8058fa818acfd91759edffa27e473f2308d5a6fca1e07a79189b95879953'