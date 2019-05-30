from os.path import abspath

from .storage import Storage

class Bag:
    """A class for BagIt bags."""

    @classmethod 
    def create_bag(klass, source, destination=None, bag_info={}, processes=1, checksums=None, encoding="utf-8"):
        """
        Create a bag in place, or at a given destination using a given directory of source data.
        """
        src = Storage.new_from_location(source)
        for path in src.listdir():
            src.move(path, )

        return Bag(str(src), create=True)

    def __init__(self, location, create=False):
        self.storage = Storage.new_from_location(location)