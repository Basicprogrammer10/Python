import sys
RED     = "\033[1;31m"  
BLUE    = "\033[1;34m"
CYAN    = "\033[1;36m"
GREEN   = "\033[0;32m"
RESET   = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
def color(x):
    '''Changs the color of the text printed to terminal'''
    sys.stdout.write(x)

def cprint(text, color):
    '''Prints text to terminal in color'''
    sys.stdout.write(color)
    print(text)
    sys.stdout.write(RESET)
 
# Example
# sys.stdout.write(RED)
# cprint("TEST", RED)