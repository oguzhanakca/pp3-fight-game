from game import start_option
from sheets import *

def welcome():
    """
    Displays when users starts game.
    """
    title = ["           _____  ______ _   _          ","     /\   |  __ \|  ____| \ | |   /\    ","    /  \  | |__) | |__  |  \| |  /  \   ","   / /\ \ |  _  /|  __| | . ` | / /\ \  ","  / ____ \| | \ \| |____| |\  |/ ____ \ "," /_/    \_\_|  \_\______|_| \_/_/    \_\\","                                        ","                                        "]
    for line in title:
        print(line)
    
    start_option()

def test():
    """
    test function
    """
    
#test()
welcome()