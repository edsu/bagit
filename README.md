# bagit

This is a work in progress to create a bagit-python v2. This README serves as a
design sketch for the way in which the new command line utility and library can
be used.

## Install

    % pip install bagit

## Command Line

### Create

Convert the current working directory into a bag:

    % cd /my/awesome/data
    % bagit init

Convert a given directory into a bag:

    % bagit init /my/awesome/data

Use a source directory to create a bag at another location. Unlike the previous
two commands this will copy the files and not modify the source directory:

    % bagit init /my/awesome/data /vol/megastorage/my-awesome-data

### Validate

Validate the bag that is present in your current working directory. You can be
down inside of it.

    % bagit validate 

Validate a bag at a given location:

    % bagit validate /my/awesome/data

### Update

You may find yourself modifying bag metadata or payload files and want to update
the manifest files with the latest checksums:

    % bagit add bag-info.txt
    % bagit add data/rickroll.mp3
    % bagit commit

## API

### Bag

The *Bag* class can be used directly in your own code to open a bag and operate on it. For example, in order to create a new *Bag* instance and verify it you can:

```python
from bagit import Bag

bag = Bag("/my/awesome/data")
print(bag.validate())
```

Similarly if you need to create a bag you can use the *create_bag* function:

```python
from bagit import create_bag

bag = create_bag("/my/awesome/data")
```

Add a file to a bag, if it's relative to the bag payload:

```python
bag.add_file("video.mp4")
```

## Storage

In addition to interacting to Bags on the filesystem you can also store bags in alteratne storage containers.

### Zip

```python
bag = Bag("my-awesome-bag.zip")
print(bag.validate())
```

### S3

```python
bag = Bag("s3://my-awesome-bag")
print(bag.validate())
```

### Bag Events

If you need to override the way that Bags are processed you can subclass *bagit.Bag*:

TBD.
