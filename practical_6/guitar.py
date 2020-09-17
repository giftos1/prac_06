class Guitar:
    """Guitar class for storing information of a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """self variables for storing details of a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string format for a guitar object"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)


