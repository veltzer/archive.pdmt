class Operation:
    """
    A simple hello world operation (prints hello world on the screen)
    """
    def __init__(self):
        super().__init__(
            'hello',
            'print hello on the screen',
        )

    def run(self):
        print('Hello, World!\n', self.name)
