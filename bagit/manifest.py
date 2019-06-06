class Manifest:

    def __init__(self, path, algorithm="md5"):
        """
        Create a Manifest instance by passing in the directory path
        where the files reside and the fixity algorithm to use.
        """
        self.path = path
        self.algorithm = algorithm
        self.fixities = {}

    def __getitem__(self, path):
        """
        Return the fixity for a given file in the manifest.
        """
        if key in self.files:
            return self.files[key]
        else:
            raise MissingManifestFile(path)

    def generate(self):
        pass


class MissingFile(Exception):
    pass