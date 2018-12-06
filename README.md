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

    % bagit commit bag-info.txt
    % bagit commit data/rickroll.mp3

