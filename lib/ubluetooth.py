FLAG_READ = 2
FLAG_WRITE_NO_RESPONSE = 4
FLAG_WRITE = 8
FLAG_NOTIFY = 16
FLAG_INDICATE = 32

class UUID():
    def __init__(self, uuid):
        pass

class BLE():
    # Configuration
    def active(self, act=None):
        if act == None:
            return True
    def config(self, param=None, *argv, **kws):
        if param != None:
            return param
    # Event Handling
    def irq(self, handler):
        pass
    # Broadcaster Role (Advertiser)
    def gap_advertise(self, interval_us, adv_data=None, *, resp_data=None, connectable=True):
        pass
    # Observer Role (Scanner)
    def gap_scan(self, duration_ms, interval_us=1280000, window_us=11250, active=False):
        pass
    # Central Role
    def gap_connect(self, addr_type, addr, scan_duration_ms=2000):
        pass
    # Central & Peripheral Roles
    def gap_disconnect(self, conn_handle):
        pass
    # GATT Server
    def gatts_register_services(self, services_definition):
        id = 0
        services_id = []
        for service in services_definition:
            s_uuid, characters = service
            characters_id = []
            for character in characters:
                characters_id.append(id)
                id += 1
                if len(character) >= 3:
                    descriptors = character[2]
                    for descriptor in descriptors:
                        characters_id.append(id)
                        id += 1
            services_id.append(tuple(characters_id))
        return tuple(services_id)
    def gatts_read(self, value_handle):
        return b''
    def gatts_write(self, value_handle, data):
        pass
    def gatts_notify(self, conn_handle, value_handle, data=None):
        pass
    def gatts_indicate(self, conn_handle, value_handle):
        pass
    def gatts_set_buffer(self, value_handle, len, append=False):
        pass
    # GATT Client
    def gattc_discover_services(self, conn_handle, uuid=None):
        pass
    def gattc_discover_characteristics(self, conn_handle, start_handle, end_handle, uuid=None):
        pass
    def gattc_discover_descriptors(self, conn_handle, start_handle, end_handle):
        pass
    def gattc_read(self, conn_handle, value_handle):
        pass
    def gattc_write(self, conn_handle, value_handle, data, mode=0):
        pass
    def gattc_exchange_mtu(self, conn_handle):
        pass

