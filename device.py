class Disk:
    def __init__(self):
        pass

class Device:
    def __init__(self,name="default_name", disk=None, specs=None, os="BaseOs"):
        self.disk = disk
        self.name = name
        if specs == None :
            specs = {
                "RAM" : 4,
                "storage" : disk if disk else 32,
                "GPU tier" : 0,
                "wifi" : None,
                "bluetooth" : None
            }
    
    def info(self):
        pass
        
