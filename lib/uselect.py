import select as cpy_select

POLLIN = 1
POLLOUT = 4
POLLERR = 8
POLLHUP = 16
select = cpy_select.select

class Poll():
    def register(self, obj, eventmask=0):
        pass
    def unregister(self, obj):
        pass
    def modify(self, obj, eventmask):
        pass
    def poll(self, timeout=-1):
        return []
    def ipoll(self, timeout=-1, flags=0):
        return iter([])