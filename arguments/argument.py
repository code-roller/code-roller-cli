import sys as sys
import os as os

"""
If a person has to set any command
he has to set a env to
name code-roller

else, we just take them 
to the setup
"""

class CodeRollerParser(object):
    def __init__(self, arguments=sys.argv[1:]):
        assert isinstance(arguments, list), "Expected a list"

        self.arguments = arguments
        self.length = len(self.arguments)

        self.directory = str(os.getcwd())

        self.parse_arguments()

    def parse_arguments(self):
        if self.find_code_roller_path() is not None:
            self.directory = self.find_code_roller_path()

        if self.length == 0:
            pass
        elif self.length == 2:
            pass
        else:
            pass

    def find_code_roller_path(self):
        IDENTIFIER = "CODE-ROLLER"

        if os.getenv(IDENTIFIER):
            return os.getenv(IDENTIFIER)

        return None
