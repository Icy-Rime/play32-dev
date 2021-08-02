import select as cpy_select
import selectors

POLLIN = 1
POLLOUT = 4
POLLERR = 8
POLLHUP = 16
select = cpy_select.select

def poll():
    return Poll()

class Poll():
    def __init__(self):
        self.__selector = selectors.DefaultSelector()

    def register(self, obj, eventmask=POLLIN|POLLOUT):
        if obj in self.__selector.get_map():
            self.unregister(obj)
        mask = 0
        if eventmask & POLLIN != 0:
            mask |= selectors.EVENT_READ
        if eventmask & POLLOUT != 0:
            mask |= selectors.EVENT_WRITE
        pass
    def unregister(self, obj):
        self.__selector.unregister(obj)
        pass
    def modify(self, obj, eventmask):
        self.unregister(obj)
        self.register(obj, eventmask)
        pass
    def poll(self, timeout=-1):
        if timeout == -1:
            events = self.__selector.select()
        else:
            events = self.__selector.select(float(timeout / 1000))
        lst = []
        for key, s_mask in events:
            obj = key.data
            mask = 0
            if s_mask & selectors.EVENT_READ != 0:
                mask |= POLLIN
            if s_mask & selectors.EVENT_WRITE != 0:
                mask |= POLLOUT
            lst.append((obj, mask))
        return []
    def ipoll(self, timeout=-1, flags=0):
        for obj, mask in self.poll(timeout):
            if flags == 1:
                self.modify(obj, 0)
            yield (obj, mask)