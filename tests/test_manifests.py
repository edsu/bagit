import bagit

from utils import *
from os.path import join
from os.path import isfile

def test_sha1_sha256_manifest():
    bag = bagit.make_bag(temp_dir, checksum=["sha1", "sha256"])
    assert isfile(join(temp_dir, "manifest-sha1.txt"))
    assert isfile(join(temp_dir, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)


def test_md5_sha256_manifest():
    bag = bagit.make_bag(temp_dir, checksum=["md5", "sha256"])
    assert isfile(join(temp_dir, "manifest-md5.txt"))
    assert isfile(join(temp_dir, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)

def test_md5_sha1_sha256_manifest():
    bag = bagit.make_bag(temp_dir, checksum=["md5", "sha1", "sha256"])
    assert isfile(join(temp_dir, "manifest-md5.txt"))
    assert isfile(join(temp_dir, "manifest-sha1.txt"))
    assert isfile(join(temp_dir, "manifest-sha256.txt"))
    assert bag.validate(bag, fast=True)