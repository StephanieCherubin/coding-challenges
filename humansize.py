SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    # required argument have to go first in parentheses
    # size is required
    # a_kilobyte_is_1024_bytes is not required because it is already set as true

    # You can document a Python function/class by giving it a documentation string (docstring for short) after every definition of a function or class.
    # You can also add it to the docstring by using self.__doc___
    # In Python, everything is a dictionary.
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    # if a_kilobyte_is_1024_bytes:
    #     multiple = 1024
    # else: 
    #     multiple = 2000

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple: #size = size / multiple
            #
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))

