class ANSI_Colorizer():
    def __init__(self):
        self.colors = {
            'black': 30,
            'red': 31,
            'green': 32,
            'yellow': 33,
            'blue': 34,
            'magenta': 35,
            'cyan': 36,
            'white': 37,
            'reset': 0
        }

    def colorize(self, text, color):
        return '\033[{}m{}\033[{}m'.format(self.colors[color], text, self.colors['reset'])

    def colorize_all(self, text):
        for color in self.colors:
            print(self.colorize(text, color))

    def get_color(self, color):
        return self.colors[color]

    def get_colors(self):
        return self.colors

    def get_color_names(self):
        return self.colors.keys()

    def get_color_codes(self):
        return self.colors.values()

    def print_colorized(self, text, color):
        print(self.colorize(text, color))

    def print_colorized_all(self, text):
        for color in self.colors:
            self.print_colorized(text, color)

    def print_colorized_all_with_names(self, text):
        for color in self.colors:
            print('{}: {}'.format(color, self.colorize(text, color)))

    def print_colorized_all_with_codes(self, text):
        for color in self.colors:
            print('{}: {}'.format(self.colors[color], self.colorize(text, color)))

    def print_colorized_all_with_names_and_codes(self, text):
        for color in self.colors:
            print('{}: {} ({})'.format(color, self.colorize(text, color), self.colors[color]))

    def print_colorized_all_with_names_and_codes_and_backgrounds(self, text):
        for color in self.colors:
            for background in self.colors:
                print('{}: {} ({}) ({})'.format(color, self.colorize(text, color), self.colors[color], self.colors[background]))

    def print_colorized_all_with_names_and_codes_and_backgrounds_and_bold(self, text):
        for color in self.colors:
            for background in self.colors:
                print('{}: {} ({}) ({}) ({})'.format(color, self.colorize(text, color), self.colors[color], self.colors[background], self.get_bold()))

    def get_bold(self):
        return '\033[1m'

    def get_underline(self):
        return