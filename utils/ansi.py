class ANSI:
    """
    ANSI string formatting class
    """

    @staticmethod
    def format_ansi(string: str, style: str) -> str:
        """
        Format a string with an ansi style.
        :param string: The string to format.
        :param style: The style to apply. Use ANSI properties from this class.
        """
        return style + string + ANSI.RESET()
    
    @staticmethod
    def ESCAPE():
        return "\u001b["

    @staticmethod
    def RESET():
        return ANSI.ESCAPE() + "0m"

    @staticmethod
    def BOLD():
        return ANSI.ESCAPE() + "1m"

    @staticmethod
    def DIM():
        return ANSI.ESCAPE() + "2m"

    @staticmethod
    def ITALIC():
        return ANSI.ESCAPE() + "3m"

    @staticmethod
    def UNDERLINE():
        return ANSI.ESCAPE() + "4m"

    @staticmethod
    def BLINK():
        return ANSI.ESCAPE() + "5m"

    @staticmethod
    def REVERSE():
        return ANSI.ESCAPE() + "7m"

    @staticmethod
    def HIDDEN():
        return ANSI.ESCAPE() + "8m"

    @staticmethod
    def STRIKETHROUGH():
        return ANSI.ESCAPE() + "9m"

    @staticmethod
    def GRAY():
        return ANSI.ESCAPE() + "30m"

    @staticmethod
    def RED():
        return ANSI.ESCAPE() + "31m"

    @staticmethod
    def GREEN():
        return ANSI.ESCAPE() + "32m"

    @staticmethod
    def YELLOW():
        return ANSI.ESCAPE() + "33m"

    @staticmethod
    def BLUE():
        return ANSI.ESCAPE() + "34m"

    @staticmethod
    def PINK():
        return ANSI.ESCAPE() + "35m"

    @staticmethod
    def CYAN():
        return ANSI.ESCAPE() + "36m"

    @staticmethod
    def WHITE():
        return ANSI.ESCAPE() + "37m"

    @staticmethod
    def BG_FIREFLY_DARK_BLUE():
        return ANSI.ESCAPE() + "40m"

    @staticmethod
    def BG_ORANGE():
        return ANSI.ESCAPE() + "41m"

    @staticmethod
    def BG_MARBLE_BLUE():
        return ANSI.ESCAPE() + "42m"

    @staticmethod
    def BG_GREYISH_TURQUOISE():
        return ANSI.ESCAPE() + "43m"

    @staticmethod
    def BG_GRAY():
        return ANSI.ESCAPE() + "44m"

    @staticmethod
    def BG_INDIGO():
        return ANSI.ESCAPE() + "45m"

    @staticmethod
    def BG_LIGHT_GRAY():
        return ANSI.ESCAPE() + "46m"

    @staticmethod
    def BG_WHITE():
        return ANSI.ESCAPE() + "47m"