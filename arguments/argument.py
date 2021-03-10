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
        assert isinstance(self.arguments, list), "Expected a list"

        self.arguments = arguments
        self.length = len(self.arguments)

        self.parse_arguments()

    def parse_arguments(self):
        if self.length == 0:
            if self.find_code_roller_path() == None:
                pass

    def find_code_roller_path(self):
        IDENTIFIER = "CODE-ROLLER"

        if os.getenv(IDENTIFIER):
            return os.getenv(IDENTIFIER)

        return None
