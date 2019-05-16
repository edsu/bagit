import io
import os
import hashlib

from os.path import join, exists


class Storage:
    """
    A base storage class, providing an interface and functionality for 
    other storage systems to inherit or override.
    """

    @classmethod
    def new_from_location(klass, location):
        # TODO: extend for .zip, s3, etc
        return FileSystemStorage(location)

    def __repr__(self):
        raise NotImplementedError("subclasses of Storage must provide __repr__() method")

    def exists(self, name):
        """
        Return True if the specified file exists or False if it does not.
        """
        raise NotImplementedError("subclasses of Storage must provide an exists() method")

    def open(self, name, mode='rb'):
        """
        Retrieve the specified file from storage.
        """
        raise NotImplementedError("subclasses of Storage must provide an open() method.")

    def save(self, name, content, max_length=None):
        """
        Save new content to the file specified by name. The content should
        be a proper File object or any Python file-like object, ready
        to be read from the beginning.
        """
        return NotImplementedError("subclasses of Storage must provide a save method.")

    def uri(self, name):
        """
        Return a URI for the given file.
        """
        return NotImplementedError("subclasses of Storage must provide a uri() method.")

    def delete(self, name):
        """
        Delete the file.
        """
        raise NotImplementedError("subclasses of Storage must provide a delete() method.")

    def listdir(self, path):
        """
        List the contents of the specified path. Return a 2-tuple of lists:
        the first item being directories, the second item being files.
        """
        raise NotImplementedError("subclasses of Storage must provide a listdir() method.")

    def size(self, name):
        raise NotImplementedError("subclasses of Storage must provide a size() method.")

    def md5(self, name):
        return self.hexdigest(name, [hashlib.md5])[0]

    def sha256(self, name):
        return self.hexdigest(name, [hashlib.sha256])[0]
 
    def hexdigest(self, name, algos, buffer_size=io.DEFAULT_BUFFER_SIZE):
        hashers = [a() for a in algos]
        fh = self.open(name, 'rb')
        while True:
            data = fh.read(buffer_size)
            if not data:
                break
            for hasher in hashers:
                hasher.update(data)
        return [h.hexdigest() for h in hashers]


class FileSystemStorage(Storage):

    def __init__(self, location=None):
        self.location = location

    def __repr__(self):
        return self.location

    def path(self, name):
        return join(self.location, name)

    def exists(self, name):
        return exists(self.path(name))

    def open(self, name, mode='r'):
        return open(self.path(name), mode)

    def save(self, name, content):
        # TODO
        pass

    def listdir(self, name=''):
        dirs, files = [], []
        path = self.path(name)
        for entry in os.scandir(path):
            if entry.is_dir():
                dirs.append(entry.name)
            else:
                files.append(entry.name)
        return dirs, files