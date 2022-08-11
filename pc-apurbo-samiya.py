import pyfiglet
from colorama  import Fore , Back , Style
import time,os,sys
import pyperclip

def type(text):
    for charecter in text:
        sys.stdout.write(charecter)
        sys.stdout.flush()
        time.sleep(0.02)



logo = pyfiglet.figlet_format("APURBO" , font = "graffiti")
ig = Fore.GREEN + logo
type(ig)
type( Fore.BLUE + "A Tool From APURBO............\n")
type(Fore.YELLOW + "Inspired By SAMIYA.........\n")
type(Fore.GREEN + "IMPRESS YOUR GIRLFRIEND BY THIS TOOL\n")
type("        1> TYPE WITH NUMBER\n")
type("        2> TYPE WITHOUT NUMBER\n")


ip = input("SELECT A NUMBER->    ")
ipt = int(ip)

if ipt == int(1):
    text = input(Fore.RED + "What You Want To Type->    ")
    num = input(Fore.BLUE + "Number Of Times You Want To Print->    ")
    numi = int(num)
    nm = numi + 1
    for i in range(1 , nm):
        boss =  print(Fore.GREEN + text , i)
        pyperclip.copy(boss)
        
        
        
        
        
if ipt == int(2):
    text = input(Fore.RED + "What You Want To Type->    ")
    num = input(Fore.BLUE + "Number Of Times You Want To Print->    ")
    numi = int(num)
    for i in range(numi):
        boss =  print(Fore.GREEN + text)
        pyperclip.copy(boss)
        
    




    