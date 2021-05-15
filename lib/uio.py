import io

open = io.open
FileIO = io.FileIO
TextIOWrapper = io.TextIOWrapper
class StringIO(io.StringIO):
    def __init__(self, init_value):
        if type(init_value) == int:
            data = bytes(init_value).decode()
            super().__init__(data)
        else:
            super().__init__(init_value)
class BytesIO(io.BytesIO):
    def __init__(self, init_value):
        if type(init_value) == int:
            data = bytes(init_value)
            super().__init__(data)
        else:
            super().__init__(init_value)
