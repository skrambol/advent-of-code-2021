from typing import List, Union


def get_depth_change(depths: List[int]) -> List[Union[None, int]]:
    """
    returns a list of bool that contains the change from the previous depth
        None -> used for the first entry
        True -> current is greater than previous
        False -> current is less than or equal than previous

    depths: list of depth changes
    """
    changes = [None]

    for i in range(1, len(depths)):
        changes.append(depths[i] > depths[i-1])

    return changes


def count_depth_change(changes: List, is_increasing=True) -> int:
    """
    returns a number of positive/negative/zero values depending on the given value
        True -> default; counts positive relative change
        False -> counts zero/negative relative change

    changes: list of relative depth changes
    value: bool; True will check for relative increase; Flase for decrease or no change
    """
    # counts the number of `value` in the list
    return sum(v for v in changes if v is is_increasing)


def get_measurement_window(depths: List[int], window: int = 3) -> List:
    """
    returns a list of int that contains the sum of the next `window` elements from `depths`

    depths: list of int; depth changes
    window: int; number of elements to sum
    """
    max_index = len(depths)
    array = []

    for i in range(0, max_index):
        if i+window > max_index:
            break

        else:
            measurement_window = sum(depths[i:i+window])
            array.append(measurement_window)

    return array
