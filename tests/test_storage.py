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

def test_hasher():
    expected = {
        "loc/2478433644_2839c5e8b8_o_d.jpg": "9a2b89e9940fea6ac3a0cc71b0a933a0",
        "README":                            "8e2af7a0143c7b8f4de0b3fc90f27354",
        "loc/3314493806_6f1db86d66_o_d.jpg": "6172e980c2767c12135e3b9d246af5a3",
        "si/2584174182_ffd5c24905_b_d.jpg":  "38a84cd1c41de793a0bccff6f3ec8ad0",
        "si/4011399822_65987a4806_b_d.jpg":  "5580eaa31ad1549739de12df819e9af8"
    }

    storage = FileSystemStorage(TEMP_DATA)
    hashes = storage.hash([hashlib.md5])
    for path, checksums in hashes.items():
        assert path in expected
        assert checksums["md5"] == expected[path]