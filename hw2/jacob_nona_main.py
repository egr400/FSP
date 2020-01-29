"""Sphere class"""
from jacob_nona_sphere import CreateSphere as sphere


def main():
    """main function printing methods """
    print_red()
    print_list()


def print_red():
    """Prints red variable instantiated from imported Sphere class"""
    red = sphere(1.7, 0.25)
    print(dir(red))
    print(red.surface_area, red.density, red.volume)


def print_list():
    """Prints contents of localized list """
    x_list = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    for i in x_list:
        print(*i, sep=" & ")


main()
