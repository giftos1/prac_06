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

    def get_age(self):
        """Get age of guitar from the current year 2020"""
        age_of_guitar = 2020 - self.year
        return age_of_guitar

    def is_vintage(self):
        """Check if a guitar is vintage based on its age"""
        return self.get_age() >= 50
