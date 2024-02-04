# main.py

from resistor import Resistor
from resistor_values import is_valid_color

def main():
    print("Resistor Color Code Reader")
    resistor = Resistor()

    while True:
        colors = input("Enter resistor colors separated by space (or 'exit' to quit): ").split()
        
        if colors[0].lower() == 'exit':
            break

        if all(is_valid_color(color) for color in colors):
            resistance = resistor.calculate_resistance(colors)
            print(f"Resistance Value: {resistance} ohms")
        else:
            print("Invalid colors entered. Please try again.")

        print()
        
if __name__ == "__main__":
    main()
