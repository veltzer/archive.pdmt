'''
Show the config of Pdmt
'''


class Operation:
    def __init__(self):
        super().__init__(
            'hello',
            'print hello on the screen',
        )

    def run(self):
        pdmt.config.show()
