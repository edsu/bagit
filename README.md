# bagit

This is a work in progress to create a bagit-python v2. This README serves as a
design sketch for the way in which the new command line utility and library can
be used.

## Install

    % pip install bagit

## Command Line

### Creating a Bag

Convert the current working directory into a bag:

    % cd /my/awesome/data
    % bagit init

Convert a given directory into a bag:

    % bagit init /my/awesome/data

Use a directory as a source for creating a bag somewhere at another location.
Unlike the previous two commands the original data will be unmodified.

    % bagit init /my/awesome/data /vol/megastorage/my-awesome-data



