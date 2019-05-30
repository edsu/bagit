import .exceptions

class Manifest:

    def __init__(self, path, algorithm=["md5"]):
        """
        Create a Manifest instance by passing in the directory path
        where the files reside and the fixity algorithm(s) to use.
        """
        self.path = path
        self.algorithms = algorithms
        self.fixities = {}

    def __getitem__(self, path):
        """
        Return the fixity for a given file in the manifest.
        """
        if key in self.files:
            return self.files[key]
        else:
            raise exceptions.MissingManifestFile(path)

    def generate(self):
        pass
