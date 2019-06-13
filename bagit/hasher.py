class Hasher:
    
    def __init__(self, algos=["md5"]):
        self.algos = algos
        
    def hash(self, storage):
        hashes = {}
        for path in storage.walk():
            hashes[path] = self.storage.hexdigest(path, algos)
        return hashes