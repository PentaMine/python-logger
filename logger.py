from datetime import datetime
from colorama import Fore

logLevel = True
colorLevelText = True
quitWhenLogFatal = True
colorText = False

warnColor = Fore.YELLOW
infoColor = Fore.RESET
debugColor = Fore.WHITE
errorColor = Fore.LIGHTRED_EX
fatalColor = Fore.RED


class CustomLogLevel:
    def __init__(self, name, color: str = Fore.RESET, isFatal: bool = False):
        self.name = name
        self.color = color
        self.isFatal = isFatal

    def log(self, message):
        log(message, self.color, self.name)
        if self.isFatal and quitWhenLogFatal:
            quit()


def log(message: str, color: str = Fore.RESET, level: str = "DEBUG", end: str = "\n"):
    current_time = datetime.now()
    if colorText:
        if logLevel:
            print(f"[{current_time.strftime('%X')}] {color if colorLevelText else Fore.RESET}[{level}]",
                  color + str(message), end=end + Fore.RESET)

        else:
            print(f"[{current_time.strftime('%X')}]", color + str(message), end=end + Fore.RESET)
    else:
        if logLevel:
            print(f"[{current_time.strftime('%X')}] [{level}]",
                  str(message), end=end)

        else:
            print(f"[{current_time.strftime('%X')}]", str(message), end=end)


def log_warning(message: str):
    log(message, warnColor, "WARN")


def log_info(message: str):
    log(message, infoColor, "INFO")


def log_debug(message: str):
    log(message, debugColor, "DEBUG")


def log_error(message: str):
    log(message, errorColor, "ERROR")


def log_fatal(message: str, exception=""):
    log(message, fatalColor, "FATAL")
    if quitWhenLogFatal:
        quit(exception)
