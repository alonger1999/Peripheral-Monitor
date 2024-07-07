import threading
import time as t

from jinja2 import Template

from utils import Logger
from config import TICK, MONITORS
from config.logging import MONITORS_STATUS_LOG_CONFIG, EMERGENCIES_STATUS_LOG_CONFIG


def check_monitor(monitor):

    monitor_check_status, emergency_run_statuses = monitor.check()

    MONITORS_STATUS_LOG_CONFIG[monitor_check_status]['function'](Template(MONITORS_STATUS_LOG_CONFIG[monitor_check_status]['message_template']).render(monitor=monitor), level=1)

    for emergency_name, emergency_run_status in emergency_run_statuses.items():
        EMERGENCIES_STATUS_LOG_CONFIG[emergency_run_status]['function'](Template(EMERGENCIES_STATUS_LOG_CONFIG[emergency_run_status]['message_template']).render(emergency=emergency_name), level=2)


def mainloop():

    number_of_monitors = len(MONITORS)

    Logger.info(f"Starting {number_of_monitors} monitors...")

    for monitor in MONITORS:
        threading.Thread(target=check_monitor, args=(monitor,)).start()

    Logger.info("All monitors have been started.")


if __name__ == '__main__':

    while True:
        mainloop()
        t.sleep(TICK)
