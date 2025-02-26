class AnsiCodes:
    RESET = "\033[0m"

    STYLES = {
        "bold": "\033[1m",
        "fade": "\033[2m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "blink_slow": "\033[5m",
        "blink_fast": "\033[6m",
        "reverse": "\033[7m",
        "hidden": "\033[8m",
        "concealed": "\033[9m",
        "frame": "\033[51m",
        "overline": "\033[53m",
    }

    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "gray": "\033[90m",
    }

    BACKGROUNDS = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
    }
