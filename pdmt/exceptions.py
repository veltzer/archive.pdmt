"""
Exceptions to be used in pdmt
"""

import enum
import sys
import pdmt.utils.printer


class Codes(enum.Enum):
    """ exit codes to be used by the exceptions """
    commandLineInputProblem = 1


class CommandLineInputException(Exception):
    def __init__(self, msgs):
        super().__init__()
        self.msgs = msgs

    def print(self):
        for msg in self.msgs:
            pdmt.utils.printer.print_msg(msg)

    def print_and_exit(self):
        self.print()
        sys.exit(Codes.commandLineInputProblem.value)
