import os

from datetime import datetime as dt

from monitors import Monitor

from config.custom import TIMEZONE, DRIVE_PING_DATETIME_FORMAT


class CPUMonitor(Monitor):
    pass


class RAMMonitor(Monitor):
    pass


class DriveMonitor(Monitor):
    
    def pre_check(self) -> None:

        now = dt.now(TIMEZONE)
        
        ping_folder = self.kwargs['ping_folder']

        with open(os.path.join(ping_folder, "ping"), 'w') as ping_file:
            ping_file.write(f"{now.strftime(DRIVE_PING_DATETIME_FORMAT)}\n")
