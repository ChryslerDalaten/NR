# resistor.py

from resistor_values import color_codes, is_valid_color

class Resistor:
    def calculate_resistance(self, colors):
        try:
            values = [color_codes[color.lower()] for color in colors]
            resistance_value = int("".join(map(str, values[:-1])))
            multiplier = 10 ** values[-1]
            return resistance_value * multiplier
        except KeyError:
            return "Invalid color entered"
        except Exception as e:
            return f"An error occurred: {e}"
