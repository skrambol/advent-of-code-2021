def file_to_int_array(filename):
    """
    returns an array containing int from filename

    filename: string for the filename relative to the root directory
    """
    with open(filename) as file:
        return [int(num) for num in file.read().splitlines()]
