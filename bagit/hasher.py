def hasher(storage, algorithms):
    hashes = 
    for path in storage.walk():
        hashes[path] = storage.hexdigest(path, algorithms=algorithms)
    return hashes
        


