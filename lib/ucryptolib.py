import pyaes
# not exist on esp32 port
# MODE_ECB = 1
# MODE_CBC = 2
# MODE_CTR = 6

class aes():
    def __init__(self, key, mode, IV=None):
        if mode == 2 and IV == None:
            raise Exception("you must provide IV when using counter mode.")
        if mode == 1:
            self.__aes = pyaes.AESModeOfOperationECB(key)
        elif mode == 2:
            self.__aes = pyaes.AESModeOfOperationCBC(key, iv = IV)
        elif mode == 6:
            if IV == None:
                self.__aes = pyaes.AESModeOfOperationCTR(key)
            else:
                counter = pyaes.Counter(initial_value = IV)
                self.__aes = pyaes.AESModeOfOperationCTR(key, counter = counter)
        else:
            raise Exception("ValueError: mode")
    
    def encrypt(self, in_buf, out_buf=None):
        out = self.__aes.encrypt(in_buf)
        if out_buf != None:
            out_buf[:len(out)] = out
        else:
            return bytes(out)
    
    def decrypt(self, in_buf, out_buf=None):
        out = self.__aes.decrypt(in_buf)
        if out_buf != None:
            out_buf[:len(out)] = out
        else:
            return bytes(out)
