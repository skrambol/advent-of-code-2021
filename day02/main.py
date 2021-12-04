from . import PartOne, PartTwo

if __name__ == "__main__":
    input = []

    with open("day02/input.txt") as file:
        for line in file.read().splitlines():
            (direction, units) = line.split(" ")
            input.append((direction, int(units)))

    # part one
    position = (0, 0)
    for move in input:
        position = PartOne.move_coordinates(position, move)

    print(PartOne.get_final_position(position))

    # part two
    position1 = (0, 0, 0)
    for move in input:
        position1 = PartTwo.move_coordinates(position1, move)

    print(PartTwo.get_final_position(position1))
