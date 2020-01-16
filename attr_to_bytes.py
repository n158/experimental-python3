import itertools

def attr_to_bytes(attr):
    """
    Convert octetstring to bytes.
    :param attr: Given octetstring (without spaces and any other delimiters)
    :type attr: str
    :return: Converted bytes
    :rtype: bytes
    """
    
    attr = str(attr)
    result = bytearray(len(attr) // 2)
    windows = [iter(attr)] * 2
    for i, word in enumerate(itertools.zip_longest(fillvalue=None, *windows)):
        result[i] = int(''.join(word), 16)
    return bytes(result)
    
    
