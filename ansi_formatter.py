from ansi_codes import AnsiCodes


class AnsiFormatter:
    @staticmethod
    def color_text(text, color=None, background=None, style=None):
        parts = []
        if style in AnsiCodes.STYLES:
            parts.append(AnsiCodes.STYLES[style])
        if color in AnsiCodes.COLORS:
            parts.append(AnsiCodes.COLORS[color])
        if background in AnsiCodes.BACKGROUNDS:
            parts.append(AnsiCodes.BACKGROUNDS[background])

        return "".join(parts) + text + AnsiCodes.RESET

    @staticmethod
    def rgb_text(text, r, g, b):
        return f"\033[38;2;{r};{g};{b}m{text}{AnsiCodes.RESET}"

    @staticmethod
    def rgb_background(text, r, g, b):
        return f"\033[48;2;{r};{g};{b}m{text}{AnsiCodes.RESET}"
