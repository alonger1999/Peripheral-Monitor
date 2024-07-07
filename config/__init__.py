from pytz import timezone

from drivers import CPU, RAM, Drive
from monitors.custom import CPUMonitor, RAMMonitor, DriveMonitor

from utils.custom import get_cpu_emergencies, get_ram_emergencies, get_drive_emergencies
from config.custom import CPU_CONFIG, DRIVE_CONFIG


TICK = 5  # Seconds

REGION = "Europe/Kiev"

TIMEZONE = timezone(REGION)

LOGGING_DATETIME_FORMATS = {
    'US/Pacific': "%m/%d/%Y %H:%M:%S",
    'default': "%Y-%m-%d %H:%M:%S"
}

CPU_DRIVER = CPU()
RAM_DRIVER = RAM()

MONITORS = [
    CPUMonitor("CPU Temperature", CPU_DRIVER, emergencies=get_cpu_emergencies("temperature"), **CPU_CONFIG['temperature']['parameters']),
    CPUMonitor("CPU Load", CPU_DRIVER, emergencies=get_cpu_emergencies("load"), **CPU_CONFIG['load']['parameters']),
    RAMMonitor("RAM Usage", RAM_DRIVER, emergencies=get_ram_emergencies("percent")),
    *[DriveMonitor(f"{drive['name']} Temperature", Drive(drive['path']), emergencies=get_drive_emergencies(), ping_folder=drive['ping_folder']) for drive in DRIVE_CONFIG]
]
