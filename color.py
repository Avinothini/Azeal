from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import os
init()
os.system('cls')
print(Fore.RED+Back.GREEN + "{:^80}".format("Enter Student Mark"),end='')
print(Back.RESET+'',end='')
print("Enter Student Name       : ")
print("Enter Registration Number: ")
print("Enter Tamil Mark         : ")
print("Enter English Mark       : ")
print("Enter Maths Mark         : ")
print("Enter Science Mark       : ")
print("Enter Social Science Mark: ")
print("\033[2;30H",end="")
name=input()
print("\033[3;30H",end="")
reg=input()
print("\033[4;30H",end="")
t=input()
print("\033[5;30H",end="")
e=input()
print("\033[6;30H",end="")
m=input()
print("\033[7;30H",end="")
s=input()
print("\033[8;30H",end="")
ss=input()
tot=int(t)+int(e)+int(m)+int(s)+int(ss)
avg=tot/5
print(Fore.YELLOW)
print("\nStudent Name       : ",name)
print("Registration Number: ",reg)
print("Tamil Mark         : ",t)
print("English Mark       : ",e)
print("Maths Mark         : ",m)
print("Science Mark       : ",s)
print("Social Science Mark: ",ss)
print(Fore.BLUE+'',end='')
print("\033[35m\033[47m",end='')
print("Total              : ",tot)
print("Average            : ",avg)





