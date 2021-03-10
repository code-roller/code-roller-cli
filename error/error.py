from clint.textui import colored as TextColor
import os as os

class ThrowError():
    def __init__(self, error_message, error_recomendation=None):
        self.error_message = str(error_message)
        self.recomendation = error_recomendation

        self.error_from_dir = os.getcwd()

        self.throw_error_message()

    def throw_error_message(self, error_message):
        error_statement_list = list([
            "An Error occured",
            f":{error_message}:",
            f"\ntry : {self.recomendation}"
        ])