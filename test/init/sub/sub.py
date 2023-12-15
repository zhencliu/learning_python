from . import Top

class Sub(Top):
    def __init__(self):
        super().__init__()
        print('Sub')
