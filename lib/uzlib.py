import zlib, io

decompress = zlib.decompress

class DecompIO(io.BytesIO):
    def __init__(self, stream, wbits=0):
        data = stream.read()
        data = zlib.decompress(data, wbits)
        return super().__init__(data)
