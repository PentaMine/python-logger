from datetime import datetime
from colorama import Fore

logLevel = True
colorLevelText = False
quitWhenLogFatal = True

warnColor = Fore.YELLOW
infoColor = Fore.RESET
debugColor = Fore.WHITE
errorColor = Fore.RED
fatalColor = Fore.RED


class CustomLogLevel:
    def __init__(self, name, isFatal: bool = False, color: str = Fore.RESET):
        self.name = name
        self.isFatal = isFatal
        self.color = color

    def log(self, message):
        log(message, self.color, self.name)
        if self.isFatal:
            quit()


def log(message: str, color: str = Fore.RESET, level: str = "DEBUG", end: str = "\n"):
    current_time = datetime.now()
    if logLevel:
        print(f"[{current_time.strftime('%X')}] {color if colorLevelText else ''}[{level}]", color + str(message), end=end + Fore.RESET)
    else:
        print(f"[{current_time.strftime('%X')}]", color + str(message), end=end + Fore.RESET)


def log_warning(message: str):
    log(message, warnColor, "WARN")


def log_info(message: str):
    log(message, infoColor, "INFO")


def log_debug(message: str):
    log(message, debugColor, "DEBUG")


def log_error(message: str):
    log(message, errorColor, "ERROR")


def log_fatal(message: str):
    log(message, fatalColor, "FATAL")
    if quitWhenLogFatal:
        quit()
