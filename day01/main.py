from utils import file_to_int_array
from . import get_depth_change, count_depth_change, get_measurement_window

if __name__ == "__main__":
    input = file_to_int_array("day01/input.txt")

    clean_input = get_measurement_window(input)
    depths = get_depth_change(clean_input)
    count = count_depth_change(depths)

    print(count)
