import colorama
from colorama import Fore, Back, Style
import time

colorama.init(autoreset=True)

def print_colorful_pattern():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    for i in range(10):
        for j in range(10):
            color = colors[(i + j) % len(colors)]
            print(f'{color}▒', end=' ')
            time.sleep(0.05)
        print()

print_colorful_pattern()
