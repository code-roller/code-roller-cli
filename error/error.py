from clint.textui import colored as TextColor
import os as os

class ThrowError():
    def __init__(self, error_message, error_recomendation=None):
        self.error_message = str(error_message)
        self.recomendation = error_recomendation

        self.error_from_dir = os.getcwd()

        self.throw_error_message(self.error_message)

    def throw_error_message(self, error_message):
        """
        Print each message in the message array
        """
        error_statement_list = list([
            "An Error occured",
            f"{error_message}",
            f"try : {self.recomendation}"
        ])

        for message_index, message in enumerate(error_statement_list):
            if message_index == (len(error_statement_list) - 1):
                if message is not None:
                    print(TextColor.cyan(message))
                continue

            print(TextColor.red(message))