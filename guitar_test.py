from practical_6.guitar import Guitar


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2013, 2000)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 7,
                                                      other_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other_guitar.name,
                                                         False,
                                                         other_guitar.is_vintage()))


run_tests()
