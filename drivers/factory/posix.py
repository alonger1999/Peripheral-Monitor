import re
import psutil
import subprocess

from pySMART import Device


class CPUFactory:

    def __init__(self, load_monitor_interval: int = 1, temperature_accuracy: int = 3) -> None:

        self.__load_monitor_interval = load_monitor_interval
        self.__temperature_accuracy = temperature_accuracy
    
    def get_load(self) -> float:
        return psutil.cpu_percent(interval=self.__load_monitor_interval)

    def get_temperature(self) -> float:
        return round(float(re.search(r'\d+\.\d+', subprocess.check_output("vcgencmd measure_temp", shell=True, text=True)).group()), self.__temperature_accuracy)


class RAMFactory:

    def get_total(self) -> int:
        return psutil.virtual_memory().total
    
    def get_used(self) -> int:
        return psutil.virtual_memory().used
    
    def get_free(self) -> int:
        return psutil.virtual_memory().free
    
    def get_percent(self) -> float:
        return psutil.virtual_memory().percent


class DriveFactory:

    def __init__(self, path: str) -> None:
        self.__device = Device(path)

    def update(self) -> None:
        self.__device.update()

    def get_model(self) -> str:
        return self.__device.model

    def get_temperature(self) -> float:
        return self.__device.temperature
    
    def get_temperatures(self) -> dict:
        return self.__device.temperatures
    
    def get_total(self) -> int:
        return self.__device.size
