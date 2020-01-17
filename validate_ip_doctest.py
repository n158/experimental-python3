# https://codereview.stackexchange.com/questions/216311/validate-ip4-address
import doctest


def validate_ip(ip):
    """
    Checks if the ip address is valid
    args:
        ip (str): The IP address
    ret:
        A boolean: True for a a valid IP

    >>> validate_ip('08.0.0.0')
    False

    >>> validate_ip('192.169.0.1')
    True

    >>> validate_ip('0.0.0.0')
    True

    >>> validate_ip('192.168.123.456')
    False

    >>> validate_ip('oooh.0.0.1')
    False
    """
    ranges = ip.split('.')
    return len(ranges) == 4 and all(
        r.isdigit() and  # Check for digits
        int(r) in range(0, 256) and  # Check in range of 0-255
        (r[0] != "0" or len(r) == 1)  # Check for leading zero's
        for r in ranges
    )


if __name__ == '__main__':
    help(validate_ip)
    doctest.testmod(verbose=True)
