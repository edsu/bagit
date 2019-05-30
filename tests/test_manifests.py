from bagit import Manifest

from utils import *

def test_md5():
    m = Manifest(TEMP_DATA, "md5")
    assert m.algorithm == "md5"
    assert m["loc/2478433644_2839c5e8b8_o_d.jpg"] == "9a2b89e9940fea6ac3a0cc71b0a933a0"
    assert m["README"] == "8e2af7a0143c7b8f4de0b3fc90f27354"
    assert m["loc/3314493806_6f1db86d66_o_d.jpg"] == "6172e980c2767c12135e3b9d246af5a3"
    assert m["si/2584174182_ffd5c24905_b_d.jpg"] == "38a84cd1c41de793a0bccff6f3ec8ad0"
    assert m["si/4011399822_65987a4806_b_d.jpg"] == "5580eaa31ad1549739de12df819e9af8"