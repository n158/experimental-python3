# -*- coding: UTF-8 -*-
# https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python

import binascii


def read_in_chunks(file_object, chunk_size=1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1Kb."
    :param file_object: Required file 
    :type file_object: <class '_io.BufferedReader'> 
    :param chunk_size: length of a chunk in bytes 
    :type chunk_size: int 
    :return: Chunk in octetstring format
    :rtype: str  
    """""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield binascii.hexlify(data).decode()


if __name__ == '__main__':
    filename = r'./99 bottles.py'
    print("Reading file:", filename)
    with open(filename, 'rb') as f:
        f.seek(0)
        for piece in read_in_chunks(f, 80):
            print(piece)
