from termcolor import cprint,colored

def print_screen (file_name):
    with open (file_name) as screen:
        screen = screen.read()
        if file_name == "WinScreen.txt":
            print (colored(screen, 'green', attrs = ['bold']))
        
        elif file_name == "LooseScreen.txt":
            print (colored(screen, 'red', attrs = ['bold']))

