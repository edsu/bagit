import bagit

from utils import *
from os.path import join
from os.path import isfile

def test_sha1_sha256_manifest():
    bag = bagit.make_bag(TEMP_DATA, checksums=["sha1", "sha256"])
    assert isfile(join(TEMP_DATA, "manifest-sha1.txt"))
    assert isfile(join(TEMP_DATA, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)


def test_md5_sha256_manifest():
    bag = bagit.make_bag(TEMP_DATA, checksums=["md5", "sha256"])
    assert isfile(join(TEMP_DATA, "manifest-md5.txt"))
    assert isfile(join(TEMP_DATA, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)

def test_md5_sha1_sha256_manifest():
    bag = bagit.make_bag(TEMP_DATA, checksums=["md5", "sha1", "sha256"])
    assert isfile(join(TEMP_DATA, "manifest-md5.txt"))
    assert isfile(join(TEMP_DATA, "manifest-sha1.txt"))
    assert isfile(join(TEMP_DATA, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)