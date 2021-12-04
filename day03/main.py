from typing import List
from . import PartOne, PartTwo

if __name__ == "__main__":
    with open("day03/input.txt") as file:
        input: List[str] = [line for line in file.read().splitlines()]
        gamma_rate: str = PartOne.get_rate(input, "gamma")
        epsilon_rate: str = PartOne.get_rate(input, "epsilon") # bit inverse is a faster solution
        power_consumption: int = PartOne.get_power_consumption(gamma_rate, epsilon_rate)

        print(power_consumption)

        oxygen_rating: str = PartTwo.get_rate(input, "oxygen")
        co2_rating: str = PartTwo.get_rate(input, "co2")
        life_support: int = PartTwo.get_life_support_rating(oxygen_rating, co2_rating)

        print(life_support)
