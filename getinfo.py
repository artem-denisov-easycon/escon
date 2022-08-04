import os
import sys

class DeviceInfo():
    def __init__(self, name):
        """Inicializace tridy pomoci jmena

        Args:
            name (str): _jmeno zarizeni
        """        
        self.name = name
    
    def get_memory_info(self):
        """Ziskat informaci ohledne pameti 
        """        
        file = open('/proc/meminfo', 'r')
        print(file.read())
        file.close()

    def get_cpu_info(self):
        """Ziskat informaci ohledne cpu 
        """
        file = open('/proc/cpuinfo', 'r')
        print(file.read())
        file.close()

    def get_pid(self, filename):
        """Ziskat PID beziciho procesu a zapsat do souboru

        Args:
            filename (str): cilovy soubor
        """
        pid = str(os.getpid())
        print("PID: "+pid)
        file = open(filename, 'w+')
        file.write(pid)
        file.close()

def main():
    device = DeviceInfo("testdev")
    device.get_memory_info()
    device.get_cpu_info()
    if not os.path.exists('/opt'):
        os.makedirs('/opt')
    filename='/opt/'+device.name+'.pid'
    device.get_pid(filename)

if __name__ == "__main__":
    main()
