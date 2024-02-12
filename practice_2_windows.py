# Practice_2

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 2', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
number = []

# Value Input
number1 = int(input('Enter Number1 => '))
number2 = int(input('Enter Number2 => '))
number3 = int(input('Enter Number3 => '))
number4 = int(input('Enter Number4 => '))
number5 = int(input('Enter Number5 => '))

# Add Values ​​To The List
number.append(number1)
number.append(number2)
number.append(number3)
number.append(number4)
number.append(number5)

# Start Program
print(colored('==========================================================', color='magenta'))
print(f'Your List ===> {number}')
number.sort()
print(f'List You In Order ===> {number}')
number.sort(reverse=True)
print(f'List Your Order In Reverse Order ===> {number}')
print(colored('==========================================================', color='magenta'))

# Finish
# Create By Moein Heshmati