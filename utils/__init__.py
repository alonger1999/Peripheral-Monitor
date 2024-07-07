from datetime import datetime as dt

from colorama import Fore

from config import REGION, TIMEZONE, LOGGING_DATETIME_FORMATS


class Logger:

    DATETIME_FORMAT = LOGGING_DATETIME_FORMATS[REGION] if REGION in LOGGING_DATETIME_FORMATS else LOGGING_DATETIME_FORMATS['default']

    @staticmethod
    def success(message, level=0):

        now = dt.now(TIMEZONE)

        indent = '\t' * level

        print(Fore.GREEN + f"{indent}[{now.strftime(Logger.DATETIME_FORMAT)}] {message}" + Fore.RESET)

    @staticmethod
    def info(message, level=0):

        now = dt.now(TIMEZONE)

        indent = '\t' * level

        print(Fore.CYAN + f"{indent}[{now.strftime(Logger.DATETIME_FORMAT)}] {message}" + Fore.RESET)

    @staticmethod
    def warning(message, level=0):

        now = dt.now(TIMEZONE)

        indent = '\t' * level

        print(Fore.YELLOW + f"{indent}[{now.strftime(Logger.DATETIME_FORMAT)}] {message}" + Fore.RESET)

    @staticmethod
    def error(message, level=0):

        now = dt.now(TIMEZONE)

        indent = '\t' * level

        print(Fore.RED + f"{indent}[{now.strftime(Logger.DATETIME_FORMAT)}] {message}" + Fore.RESET)
