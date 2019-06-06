import os
from utils import *

from bagit import Bag
from os.path import join, isdir, isfile

info = {"Bagging-Date": "1970-01-01", "Contact-Email": "ehs@pobox.com"}
bag = Bag.create_bag(TEMP_DATA, bag_info=info, checksums=["md5"])

def test_structure():
    assert isdir(join(TEMP_DATA, "data"))

def test_bagit_txt():
    bagit_txt_file = join(TEMP_DATA, "bagit.txt")
    assert isfile(bagit_txt_file)
    bagit_txt = slurp_text_file(bagit_txt_file)
    assert "BagIt-Version: 0.97" in bagit_txt
    assert "Tag-File-Character-Encoding: UTF-8" in bagit_txt

def test_manifest():
    manifest_file = join(TEMP_DATA, "manifest-md5.txt")
    assert isfile(manifest_file)
    manifest = slurp_text_file(manifest_file).splitlines()
    assert "8e2af7a0143c7b8f4de0b3fc90f27354  data/README" in manifest
    assert "9a2b89e9940fea6ac3a0cc71b0a933a0  data/loc/2478433644_2839c5e8b8_o_d.jpg" in manifest
    assert "6172e980c2767c12135e3b9d246af5a3  data/loc/3314493806_6f1db86d66_o_d.jpg" in manifest
    assert "38a84cd1c41de793a0bccff6f3ec8ad0  data/si/2584174182_ffd5c24905_b_d.jpg" in manifest
    assert "5580eaa31ad1549739de12df819e9af8  data/si/4011399822_65987a4806_b_d.jpg" in manifest

def test_bag_info():
    bag_info_file = join(TEMP_DATA, "bag-info.txt")
    assert isfile(bag_info_file)
    bag_info = slurp_text_file(bag_info_file).splitlines()
    assert "Contact-Email: ehs@pobox.com" in bag_info
    assert "Bagging-Date: 1970-01-01" in bag_info
    assert "Payload-Oxum: 991765.5" in bag_info
    assert "Bag-Software-Agent: bagit.py v1.5.4 <https://github.com/LibraryOfCongress/bagit-python>" in bag_info

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
    assert bag.validate(bag, fast=