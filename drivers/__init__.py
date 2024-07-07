import os

from abc import ABC, abstractmethod

from drivers.factory.posix import CPUFactory, RAMFactory, DriveFactory


class Driver(ABC):

    @abstractmethod
    def get_data(self) -> dict:
        pass


class CPU(Driver):

    FACTORIES = {
        'posix': CPUFactory
    }

    def __init__(self, load_monitor_interval: int = 1, temperature_accuracy: int = 3) -> None:
        self.__factory = CPU.FACTORIES[os.name.lower()](load_monitor_interval=load_monitor_interval, temperature_accuracy=temperature_accuracy)

    def get_data(self) -> dict:

        try:

            load = self.__factory.get_load()
            temperature = self.__factory.get_temperature()

            return {

                'load': {
                    'raw': load,
                    'unit': "%",
                    'formatted': f"{load}%"
                },

                'temperature': {
                    'raw': temperature,
                    'unit': "°C",
                    'formatted': f"{temperature} °C"
                }

            }
        
        except Exception:
            return None


class RAM(Driver):

    FACTORIES = {
        'posix': RAMFactory
    }

    def __init__(self) -> None:
        self.__factory = RAM.FACTORIES[os.name.lower()]()

    def get_data(self) -> dict:

        try:

            total = self.__factory.get_total()
            used = self.__factory.get_used()
            free = self.__factory.get_free()
            percent = self.__factory.get_percent()

            return {

                'total': {
                    'raw': total,
                    'unit': "Bytes",
                    'formatted': f"{total} Bytes"
                },

                'used': {
                    'raw': used,
                    'unit': "Bytes",
                    'formatted': f"{used} Bytes"
                },

                'free': {
                    'raw': free,
                    'unit': "Bytes",
                    'formatted': f"{free} Bytes"
                },

                'percent': {
                    'raw': percent,
                    'unit': "%",
                    'formatted': f"{percent}%"
                }

            }
        
        except Exception:
            return None


class Drive(Driver):

    FACTORIES = {
        'posix': DriveFactory
    }

    def __init__(self, path: str) -> None:
        self.__factory = Drive.FACTORIES[os.name.lower()](path=path)

    def get_data(self) -> dict:

        try:

            model = self.__factory.get_model()
            temperature = self.__factory.get_temperature()
            temperatures = self.__factory.get_temperatures()
            total = self.__factory.get_total()

            return {

                'model': model,

                'temperature': {
                    'raw': temperature,
                    'unit': "°C",
                    'formatted': f"{temperature} °C"
                },

                'temperatures': {
                    'raw': temperatures,
                    'unit': "°C"
                },

                'total': {
                    'raw': total,
                    'unit': "Bytes",
                    'formatted': f"{total} Bytes"
                }

            }
        
        except Exception:
            return None
