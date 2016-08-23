'''
Exceptions to be used in pdmt
'''

import enum # for Enum
import sys # for exit
import pdmt.utils.printer # for print_msg

''' exit codes to be used by the exceptions '''
class Codes(enum.Enum):
    commandLineInputProblem=1

class CommandLineInputException(Exception):
    def __init__(self, msgs):
        super().__init__()
        self.msgs=msgs
    def print(self):
        for msg in self.msgs:
            pdmt.utils.printer.print_msg(msg)
    def print_and_exit(self):
        self.print()
        sys.exit(Codes.commandLineInputProblem.value)
