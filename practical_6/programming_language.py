class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a formatted string of objects"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.language, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Check for dynamically typed language."""
        return self.typing == "Dynamic"

